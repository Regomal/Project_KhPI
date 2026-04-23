"""
Report Tool - A structured numeric report generator
"""

# We only import public functions
from .data import parse_numbers, analyze_numbers
from .formatter import build_report, build_sorted_report
from .storage import save_report, read_back

# We explicitly specify what is available during import (from report_tool import *)
__all__ = [
    "parse_numbers",
    "analyze_numbers",
    "build_report",
    "build_sorted_report",
    "save_report",
    "read_back",
]