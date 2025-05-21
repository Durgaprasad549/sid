print("Hello")
class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add' or self.operation == '+':
            return self.a + self.b
        elif self.operation == 'subtract' or self.operation == '-':
            return self.a - self.b
        elif self.operation == 'multiply' or self.operation == '*':
            return self.a * self.b
        elif self.operation == 'divide' or self.operation == '/':
            if self.b == 0:
                raise ValueError("Cannot divide by zero.")
            return self.a / self.b
        else:
            raise ValueError(f"Unsupported operation '{self.operation}'. Supported operations: add, subtract, multiply, divide")

# Example usage
if __name__ == "__main__":
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        operation = input("Enter operation (add, subtract, multiply, divide or +, -, *, /): ")

        calc = Calculator(a, b, operation)
        result = calc.calculate()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

