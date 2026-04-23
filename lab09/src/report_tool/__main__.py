def main() -> None:
    print("=== Report Tool ===")
    print("A simple package to parse, analyze, format, and save numeric reports.\n")
    print("Main capabilities:")
    print("  - Parse string of numbers into floats")
    print("  - Calculate basic statistics (min, max, mean, sum, count)")
    print("  - Format statistics into clean text reports")
    print("  - Save and read reports to/from disk\n")
    print("Usage instruction:")
    print("  Import functions directly from 'report_tool' in your Python scripts.")
    print("  Example:")
    print("    from report_tool import parse_numbers, analyze_numbers")
    print("    numbers = parse_numbers('1, 2, 3')")
    print("    stats = analyze_numbers(numbers)")
    print("    print(stats)")

if __name__ == "__main__":
    main()