# VLA Research

This directory contains the code to replicate the tabs and columns in the [VLA Research
spreadsheet](https://docs.google.com/spreadsheets/d/1N_6qIVe8vLGBmZB5IRBkM9DnKUfUpglwDW9BFvbwz50/edit),
from crawling data to analyses and creating a new Google Sheets version.
One script handles crawling, rebuilding the seven tabs, checking their contents,
and publishing. Reviewed spreadsheet inputs and crawl snapshots are not included
in the repository. Supply copies you are authorized to use.

## Rebuild from your inputs

```bash
python -m pip install -r requirements.txt
python safety_search.py analyze \
  --reference /path/to/reviewed_snapshot.json \
  --crawl /path/to/crawl_snapshot.csv
python -m unittest discover -s tests -q
```

`--reference` accepts a seven-tab JSON snapshot or Excel export with the tab
names and headers in `sheet_schema.json`. `--crawl` accepts a CSV with the
`Raw Papers` headers from that schema. `analyze` rebuilds a workbook from the
supplied values, reads it back, and checks every cell. It writes:

- `output/tabs/`: seven CSVs with exact Google tab names and headers.
- `output/VLA Research.xlsx`: rebuilt workbook. Excel shortens three tab names
  to its 31-character limit; `sheet_schema.json` keeps the full Google names.
- `output/alignment_report.json`: corpus differences, duplicate IDs,
  classification gaps, and cross-tab inconsistencies.
- `output/manifest.json`: input, code, schema, and per-tab SHA-256 hashes.

| Tab | Reviewed input |
| --- | --- |
| Raw Papers | Crawled metadata, provenance, scores, and collected evidence |
| Sorted Borderline Papers | Lifecycle classifications and rationale |
| Sorted Master Papers | Lifecycle classifications and rationale |
| Sorted Master Papers _ landscape+note | Safety scenarios, dimensions, evidence, and embodiment labels |
| Safety-Only Master Papers _ verbatim | Quotations, normalization mappings, and source locations |
| Sorted Master Papers _ technical | Technical safety coding, metrics, and evidence |
| Milestone Papers | Milestone sources, figure roles, and treatment |

Research classifications, full-text quotations, normalization, and milestone
choices are explicit reviewed inputs. They are not inferred from an abstract.
The historical crawl queries and original review process are not reconstructed;
reproducing a particular version requires its reviewed snapshot and crawl CSV.
JSON can preserve native text, including control characters and line endings
that can change in a spreadsheet export.

## Crawl and build a new corpus version

```bash
python safety_search.py crawl \
  --query 'all:"vision language action" AND all:"safety"' \
  --start-date 20260101 --end-date 20261005 \
  --max-results 20 --output output/crawl.csv
python safety_search.py analyze \
  --reference /path/to/reviewed_snapshot.json \
  --crawl output/crawl.csv --use-crawl --output-dir output/new
```

This uses the new crawl as Raw Papers and retains existing reviewed analyses
for matching IDs. Newly found papers appear in Raw Papers and the report's
`unclassified_output_ids`; their classifications and evidence require review.
Milestones are retained as context and may refer to sources outside the crawl.
Scores, hit counts, and full-text evidence remain blank until measured.
The crawl's `.manifest.json` records the query, date bounds, pagination, response
hashes, and CSV hash. Freeze the CSV to repeat an analysis; live API results can
change.

To provide new reviewed analyses, edit the six analysis CSVs exported by a
previous run, keeping their exact filenames, headers, and column widths. Store
these together, then run:

```bash
python safety_search.py analyze \
  --reference /path/to/reviewed_snapshot.json \
  --crawl output/crawl.csv --use-crawl \
  --reviewed-dir reviewed --output-dir output/new
```

All six CSVs are required with `--reviewed-dir`; header-only files represent
empty tabs. Include rationale, source URLs, evidence, and source locations where
those columns apply. Save the crawl and reviewed CSVs alongside the manifest to
reproduce that version. A JSON reference must have a top-level `sheets` object
with all seven tabs in schema order, each starting with its header row. An Excel
export may already have changed some characters.

## Create a native Google Sheets version

Enable the Google Drive and Sheets APIs in your Google Cloud project. Supply an
OAuth access token authorized for `https://www.googleapis.com/auth/drive`, with
access to the reference Sheet and destination folder:

```bash
# Set GOOGLE_ACCESS_TOKEN in your environment using your OAuth login.
python safety_search.py publish \
  --output-dir output --title 'VLA Research - reproduced'
```

`publish` copies the native reference to the `ChatGPT` folder in My Drive,
applies changed values from the generated CSVs, and compares every output cell
with the destination. Formatting and validation come from the native template.
Changed cells containing formulas or smart chips require review and stop the
publish. Use `--folder-id FOLDER_ID` for another destination.

Each run creates a distinct spreadsheet. `output/published_version.json`
records its URL, manifest hash, and verification status. If publication fails,
the receipt identifies the incomplete copy for inspection. Authentication stays
in the environment and is never saved in the output files.
