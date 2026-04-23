from lab09.src.report_tool import parse_numbers, analyze_numbers, build_sorted_report, save_report
from lab09.src.report_tool import read_back


def main():
    print("Running...")

    text = "4, 8, 15, 16, 23, 42"

    # 1. Parse a string into a list of numbers
    numbers = parse_numbers(text)

    # 2. Analyze the numbers to generate stats
    stats = analyze_numbers(numbers)

    # 3. Build a formatted text report
    report = build_sorted_report(numbers, stats)

    # 4. Save the report to a file
    path = save_report(report, "report_output.txt")
    print(f"Success: report saved to {path}\n")

    print("Saved file content:")
    print(read_back(path))


if __name__ == "__main__":
    main()
