from typing import Union


def parse_numbers(text: str) -> list[float]:
    """Public: parse a string of comma/semicolon separated numbers"""
    pieces = text.replace(";", ",").split(",")
    return [float(p.strip()) for p in pieces if p.strip()]


def analyze_numbers(numbers: list[float]) -> dict[str, Union[int, float]]:
    """Public: calculate basic stats for a list of numbers"""
    if not numbers:
        raise ValueError("Numbers must not be empty")

    total = sum(numbers)
    count = len(numbers)

    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": total / count,
    }


if __name__ == "__main__":
    print("Module: data.py")
    print("Purpose: Parses text into numbers and calculates basic statistics.")
    print("Public functions: parse_numbers(text), analyze_numbers(numbers)")
    print("\nExample Usage:")
    print("  numbers = parse_numbers('10, 20, 30')")
    print("  stats = analyze_numbers(numbers)")
    print("  print(stats)")