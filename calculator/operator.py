class Operator():

    def add(self, data):
        return sum(data)

    def substraction(self, data):
        value = 0
        for num in data:
            value -= num
        return value

    def multiply(self, data):
        value = 1
        for num in data:
            value *= num
        return value

    def division(self, data):
        value = data[0]
        for num in data[1:]:
            value /= num
        return value