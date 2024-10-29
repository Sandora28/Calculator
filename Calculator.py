class Calculator:
    def add(self, a, b):
        """Return the sum of a and b, handling edge cases."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers.")
        return a + b

    def multiply(self, a, b):
        """Return the product of a and b, handling edge cases."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers.")
        return a * b