"""
Report Tool - A clean and structured numeric report generator.
"""

# Подтягиваем только публичные функции из наших модулей
from .data import parse_numbers, analyze_numbers
from .formatter import build_report, build_sorted_report
from .storage import save_report, read_back

# Явно указываем, что доступно при импорте со звездочкой (from report_tool import *)
__all__ = [
    "parse_numbers",
    "analyze_numbers",
    "build_report",
    "build_sorted_report",
    "save_report",
    "read_back",
]