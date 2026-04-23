from typing import Any


def build_report(stats: dict[str, Any]) -> str:
    """Public: build a basic text report from stats"""
    lines = [
        "Number Report",
        "-" * 20,
        f"original: {stats['count']}",
        f"count: {stats['count']}",
        f"sum: {stats['sum']}",
        f"min: {stats['min']}",
        f"max: {stats['max']}",
        f"mean: {round(stats['mean'], 2)}"
    ]
    return "\n".join(lines)


def build_sorted_report(numbers: list[float], stats: dict[str, Any]) -> str:
    """Public: build a text report that includes the sorted numbers"""
    base_report = build_report(stats)
    ordered = sorted(numbers)

    return f"{base_report}\nsorted: {ordered}"


if __name__ == "__main__":
    print("Module: formatter.py")
    print("Purpose: Generates text reports from statistics.")
    print("Public functions: build_report(stats), build_sorted_report(numbers, stats)")
    print("\nExample Usage:")
    print("  stats = {'count': 3, 'sum': 6, 'min': 1, 'max': 3, 'mean': 2.0}")
    print("  report = build_report(stats)")
    print("  print(report)")