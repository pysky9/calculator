from calculator.operator import Operator

class Utils():
    def __init__(self, calculate_data):
        self.calculate_data = calculate_data

    def string_to_num(self, calculate_data):
        self.data = []
        for _ in self.calculate_data.split(","):
            self.data.append(eval(_))
        return self.data

    def operator_calculate(self, choose_operator):
        math_operator = Operator()
        if choose_operator == "+":
            print(f'the addtion value of {self.calculate_data} is {math_operator.add(self.data)}')
        elif choose_operator == "-":
            print(f'the substraction value of {self.calculate_data} is {math_operator.substraction(self.data)}')
        elif choose_operator == "*":
            print(f'the multiplied value of {self.calculate_data} is {math_operator.multiply(self.data)}')
        else:
            print(f'the division value of {self.calculate_data} is {math_operator.division(self.data)}')