class myMath(object):
    def __init__(self, num1, num2):
        """Initializes the myMath class."""
        self.num1 = int(num1)
        self.num2 = int(num2)
    def add(self):
        """Returns the sum of a and b."""
        return self.num1 + self.num2
    def sub(self):
        """Returns the difference of a and b."""
        return self.num1 - self.num2

    def multiply(self):
        """Returns the product of a and b."""
        return self.num1 * self.num2

    def divide(self):
        """Returns the quotient of a and b. Raises ValueError if b is zero."""
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return None  # Return None if division by zero

    def divide2(self):
        """Returns the quotient of a and b. Raises ValueError if b is zero."""
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            raise ValueError("Division by zero is not allowed")