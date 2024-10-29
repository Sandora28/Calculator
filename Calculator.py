class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b."""
        self._validate_input(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def _validate_input(self, a, b):
        """Validate that both inputs are numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers.")