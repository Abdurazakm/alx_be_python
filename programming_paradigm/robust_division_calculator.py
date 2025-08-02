# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with proper error handling.

    Args:
        numerator (str): The numerator value as a string.
        denominator (str): The denominator value as a string.

    Returns:
        str: The result of the division or an appropriate error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
