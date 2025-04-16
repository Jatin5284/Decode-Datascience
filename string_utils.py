# string_utils.py

def reverse_string(s):
    """Return the reversed version of the string."""
    return s[::-1]

def capitalize_string(s):
    """Capitalize the first letter of the string."""
    return s.capitalize()

def to_uppercase(s):
    """Convert the entire string to uppercase."""
    return s.upper()

def to_lowercase(s):
    """Convert the entire string to lowercase."""
    return s.lower()

def is_palindrome(s):
    """Check if the string is a palindrome (ignoring case and spaces)."""
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]
