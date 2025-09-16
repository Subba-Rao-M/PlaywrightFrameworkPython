class BasicCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1+self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero"

calculator = BasicCalculator(10, 5)
print("Addition: {}+{}={}".format(calculator.num1, calculator.num2, calculator.addition()))
print("Subtraction: {}-{}={}".format(calculator.num1, calculator.num2, calculator.subtraction()))
print("Multiplication: {}*{}={}".format(calculator.num1, calculator.num2, calculator.multiplication()))
print("Division: {}/{}={}".format(calculator.num1, calculator.num2, calculator.division()))
print("*******************")
print(f"Addition: {calculator.num1} + {calculator.num2} = {calculator.addition()}")
print(f"Subtraction: {calculator.num1} - {calculator.num2} = {calculator.subtraction()}")
print(f"Multiplication: {calculator.num1} * {calculator.num2} = {calculator.multiplication()}")
print(f"Division: {calculator.num1} / {calculator.num2} = {calculator.division()}")