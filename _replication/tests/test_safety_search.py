import csv
import importlib.util
import json
import tempfile
import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
from types import SimpleNamespace

import safety_search as app


def make_inputs(root: Path) -> tuple[Path, Path]:
    """Create a small synthetic seven-tab reference and crawl for tests."""
    sheets = {}
    for title, headers in app.schema()["sheets"].items():
        rows = []
        if title == "Raw Papers":
            for paper_id, paper_title in (
                ("2601.00001v1", "Safety paper"),
                ("2601.00001v1", "Safety paper duplicate"),
                ("2601.00002v1", "Another paper"),
            ):
                row = [""] * len(headers)
                row[:2] = [paper_id, paper_title]
                rows.append(row)
        elif title == "Sorted Master Papers":
            row = [""] * len(headers)
            row[headers.index("ArXiv ID")] = "2601.00001v1"
            rows.append(row)
        elif title == "Sorted Master Papers _ landscape+note":
            row = [""] * len(headers)
            row[headers.index("ArXiv ID")] = "2601.00003v1"
            rows.append(row)
        sheets[title] = [headers] + rows
    reference = root / "reference.json"
    reference.write_text(json.dumps({"sheets": sheets}), encoding="utf-8")
    crawl = root / "crawl.csv"
    crawl_rows = []
    for paper_id in ("2601.00002v1", "2601.00003v1"):
        row = [""] * len(app.schema()["sheets"]["Raw Papers"])
        row[0] = paper_id
        crawl_rows.append(row)
    app.write_csv(crawl, app.schema()["sheets"]["Raw Papers"], crawl_rows)
    return reference, crawl


class SpreadsheetMatchTests(unittest.TestCase):
    def test_raw_columns_and_atom_mapping(self):
        xml = """<feed xmlns="http://www.w3.org/2005/Atom"><entry>
        <id>https://arxiv.org/abs/2601.00001v2</id>
        <title> A  Safety  Paper </title>
        <summary>Safe robot action.</summary>
        <published>2026-01-01T00:00:00Z</published>
        <updated>2026-01-02T00:00:00Z</updated>
        <author><name>First Author</name></author>
        <category term="cs.RO"/>
        </entry></feed>"""
        row = app.parse_atom(xml, 'all:"safety"')[0]
        self.assertEqual(len(app.schema()["sheets"]["Raw Papers"]), len(row))
        self.assertEqual("2601.00001v2", row[0])
        self.assertEqual("A Safety Paper", row[1])
        self.assertEqual("First Author", row[2])
        self.assertEqual("example", row[7])
        self.assertEqual([""] * 4, row[11:15])
        self.assertEqual(["", "", ""], row[16:19])

    def test_all_seven_tab_headers_are_recorded(self):
        sheets = app.schema()["sheets"]
        self.assertEqual(7, len(sheets))
        self.assertEqual("arxiv_id", sheets["Raw Papers"][0])
        self.assertEqual("Classification rationale", sheets["Sorted Master Papers"][-1])
        self.assertIn("Source locations", sheets["Safety-Only Master Papers _ verbatim"])

    @unittest.skipUnless(importlib.util.find_spec("openpyxl"), "openpyxl is optional")
    def test_analysis_exports_exact_tab_names_and_reports_gaps(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            reference, crawl = make_inputs(root)
            output = root / "built"
            app.analyze(SimpleNamespace(
                reference=reference,
                crawl=crawl,
                output_dir=output,
            ))
            tabs = output / "tabs"
            self.assertEqual(
                {f"{name}.csv" for name in app.schema()["sheets"]},
                {path.name for path in tabs.glob("*.csv")},
            )
            for name, headers in app.schema()["sheets"].items():
                with (tabs / f"{name}.csv").open(newline="", encoding="utf-8") as handle:
                    self.assertEqual(headers, next(csv.reader(handle)))
            report = json.loads((output / "alignment_report.json").read_text())
            self.assertEqual(3, report["reference_rows_by_tab"]["Raw Papers"])
            self.assertEqual(1, len(report["crawl_only_ids"]))
            self.assertEqual(1, len(report["reference_duplicate_ids"]))
            self.assertEqual(1, len(report["curation_checks"]["landscape_not_in_master"]))
            self.assertEqual(app.read_reference(reference), app.read_reference(output / "VLA Research.xlsx"))
            manifest = json.loads((output / "manifest.json").read_text())
            self.assertEqual("all cells match", manifest["workbook_round_trip"])

    @unittest.skipUnless(importlib.util.find_spec("openpyxl"), "install requirements.txt")
    def test_new_crawl_and_reviewed_evidence_drive_the_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            reference, crawl = make_inputs(root)
            reviewed = root / "reviewed"
            paper_id = "2610.00001v1"
            for title, headers in app.schema()["sheets"].items():
                row = [""] * len(headers)
                if title == "Raw Papers":
                    row[:2] = [paper_id, "New paper"]
                    app.write_csv(crawl, headers, [row])
                else:
                    if "ArXiv ID" in headers:
                        row[headers.index("ArXiv ID")] = paper_id
                        row[headers.index("Title")] = "New paper"
                    if "Classification rationale" in headers:
                        row[headers.index("Classification rationale")] = "Reviewed rationale"
                    if "All verbatim evidence items" in headers:
                        row[headers.index("All verbatim evidence items")] = "=Literal quoted evidence"
                    app.write_csv(reviewed / f"{title}.csv", headers, [row] if any(row) else [])
            app.analyze(SimpleNamespace(reference=reference, crawl=crawl,
                                        reviewed_dir=reviewed, use_crawl=True, output_dir=root / "built"))
            tabs = app.read_reference(root / "built" / "VLA Research.xlsx")
            self.assertEqual([paper_id], [row[0] for row in tabs["Raw Papers"]])
            self.assertEqual("Reviewed rationale", tabs["Sorted Master Papers"][0][-1])
            self.assertEqual("=Literal quoted evidence", tabs["Safety-Only Master Papers _ verbatim"][0][4])

    def test_csv_rejects_missing_columns(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text("one,two\nonly one\n")
            with self.assertRaisesRegex(ValueError, "Row width"):
                app.read_table(path, ["one", "two"])

    def test_publish_requires_authentication_before_network(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaisesRegex(ValueError, "GOOGLE_ACCESS_TOKEN"):
                app.publish(SimpleNamespace(output_dir=Path("missing")))

    def test_excel_text_preserves_control_characters_and_literal_escape_tokens(self):
        text = "Evidence\x01\uffff\r\n and literal _x0001_"
        self.assertEqual(text, app.decode_excel(app.encode_excel(text)))

    @unittest.skipUnless(importlib.util.find_spec("openpyxl"), "install requirements.txt")
    def test_publish_copies_applies_values_and_verifies_all_tabs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            reference, crawl = make_inputs(root)
            output = root / "built"
            app.analyze(SimpleNamespace(reference=reference, crawl=crawl, output_dir=output))
            expected = app.schema()["sheets"]
            tables = {title: [headers] + app.read_table(output / "tabs" / f"{title}.csv", headers)
                      for title, headers in expected.items()}
            tables["Raw Papers"][1][1] = "Outdated title"
            properties = [{"properties": {"sheetId": index, "title": title,
                           "gridProperties": {"rowCount": len(tables[title]), "columnCount": len(headers)}}}
                          for index, (title, headers) in enumerate(expected.items())]
            calls = []

            def request(method, url, **kwargs):
                calls.append((method, url, kwargs))
                if url.endswith("/copy"):
                    payload = {"id": "new-version"}
                elif url.endswith("/values:batchGet"):
                    payload = {"valueRanges": [{"values": rows} for rows in tables.values()]}
                elif url.endswith(":batchUpdate"):
                    for change in kwargs["json"]["requests"]:
                        update = change["updateCells"]
                        if update["fields"] == "userEnteredValue":
                            start = update["start"]
                            title = list(expected)[start["sheetId"]]
                            value = update["rows"][0]["values"][0]["userEnteredValue"]
                            tables[title][start["rowIndex"]][start["columnIndex"]] = next(iter(value.values()), "")
                    payload = {}
                else:
                    payload = {"sheets": properties}
                response = MagicMock()
                response.json.return_value = payload
                return response

            session = MagicMock()
            session.request.side_effect = request
            session.__enter__.return_value = session
            with patch.dict("os.environ", {"GOOGLE_ACCESS_TOKEN": "test-only"}), patch("requests.Session", return_value=session):
                app.publish(SimpleNamespace(output_dir=output, title="Test version", folder_id="folder"))
            receipt = json.loads((output / "published_version.json").read_text())
            self.assertEqual("verified", receipt["status"])
            self.assertEqual(list(expected), receipt["tabs"])
            self.assertEqual("new-version", receipt["spreadsheet_id"])
            self.assertEqual(app.read_reference(reference)["Raw Papers"][0][1], tables["Raw Papers"][1][1])
            writes = [url for method, url, _ in calls if method == "POST" and url.endswith(":batchUpdate")]
            self.assertTrue(writes)
            self.assertTrue(all("/new-version:" in url for url in writes))


if __name__ == "__main__":
    unittest.main()
