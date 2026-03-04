def format_currency(amount: float, currency: str = "USD") -> str:
    """Format amount as currency string"""
    return f"{currency} {amount:.2f}"

def validate_email(email: str) -> bool:
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
