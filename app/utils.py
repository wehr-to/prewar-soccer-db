import re
from flask import flash

# Input validation helpers

def sanitize_string(value: str) -> str:
    """
    Sanitize string input by stripping whitespace and 
    removing potentially dangerous characters.
    Prevents injection attacks and sloppy data.
    """
    if not value:
        return ""
    # Remove HTML tags (basic safeguard, Jinja escapes too)
    clean_value = re.sub(r"<.*?>", "", value)
    return clean_value.strip()


def is_valid_year(year: str) -> bool:
    """
    Check if a year string looks like a valid year for card sets.
    Pre-war/vintage soccer ranges roughly 1880–1979.
    """
    if not year.isdigit():
        return False
    y = int(year)
    return 1880 <= y <= 1979

# Collection / progress helpers

def calculate_completion(owned_count: int, total_count: int) -> float:
    """
    Calculate % completion for a set.
    Returns 0.0 if total_count is 0 to avoid division by zero.
    """
    if total_count == 0:
        return 0.0
    return round((owned_count / total_count) * 100, 2)


def format_pop_report(raw: str) -> str:
    """
    Format population report string consistently.
    Example: 'PSA 6 (12), PSA 7 (5)' > standardized output.
    """
    if not raw:
        return "N/A"
    return raw.strip()

# Flash message helpers

def success(message: str):
    """Standardize success flash messages."""
    flash(message, "success")


def error(message: str):
    """Standardize error flash messages."""
    flash(message, "error")
