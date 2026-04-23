from pathlib import Path

def save_report(report_content: str, filename: str) -> str:
    """Public: Save report text to a file and return the absolute path"""
    path = Path(filename)
    path.write_text(report_content, encoding="utf-8")
    return str(path.absolute())

def read_back(filepath: str) -> str:
    """Public: Read file content back into a string"""
    path = Path(filepath)
    return path.read_text(encoding="utf-8")

if __name__ == "__main__":
    print("Module: storage.py")
    print("Purpose: Handles saving and loading reports to/from disk.")
    print("Public functions: save_report(report_content, filename), read_back(filepath)")
    print("\nExample Usage:")
    print("  path = save_report('Test Report', 'test.txt')")
    print("  content = read_back(path)")