# Report Tool

A simple, structured Python package for parsing numeric strings, analyzing them to extract basic statistics (count, sum,
min, max, mean), and generating formatted textual reports.

## What the tool does

This package provides a clean public API to:

- Parse strings of comma or semicolon-separated numbers into lists of floats.
- Calculate essential mathematical statistics.
- Generate formatted text reports (with or without sorted number lists).
- Safely save those reports to your local file system and read them back.

## How to run it

You can run the tool as a standalone module to view its description, capabilities, and minimal usage instructions. Run
the following command in your terminal from the directory containing the `src` folder:

```bash
python -m report_tool
```

## How to use it

To use the tool in your own code, import the necessary functions directly from the package. The internal logic is
hidden, providing you with a clean and predictable API.

### Example Workflow

```python
from report_tool import parse_numbers, analyze_numbers, build_sorted_report, save_report

# 1. Parse a string into a list of numbers
text_input = "4, 8, 15, 16, 23, 42"
numbers = parse_numbers(text_input)

# 2. Analyze the numbers to generate stats
stats = analyze_numbers(numbers)

# 3. Build a formatted text report
report_text = build_sorted_report(numbers, stats)

# 4. Save the report to a file
output_path = save_report(report_text, "my_report.txt")
print(f"Report successfully saved to: {output_path}")
```