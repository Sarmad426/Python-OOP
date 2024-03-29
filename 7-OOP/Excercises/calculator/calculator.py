"""
Python class simple calculator program
"""


class Calculator:
    """Class representing a calculator object"""

    def __init__(self) -> None:
        self.num1: int = int(input("Enter value 1:"))
        self.num2: int = int(input("Enter value 2:"))

    def add(self) -> int:
        """
        Add two numbers and return them
        """
        return self.num1 + self.num2

    def sub(self) -> int:
        """
        Subtract two numbers and return them
        """
        return self.num1 - self.num2

    def mul(self) -> int:
        """
        Multiply two numbers and return them
        """
        return self.num1 * self.num2

    def div(self) -> float:
        """
        Divide two numbers and return them
        """
        return self.num1 / self.num2


calculator = Calculator()
print(calculator.add())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())
