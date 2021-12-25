def add(data):
    return sum(data)

def substraction(data):
    value = 0
    for num in data:
        value -= num
    return value

def multiply(data):
    value = 1
    for num in data:
        value *= num
    return value

def division(data):
    value = data[0]
    for num in data[1:]:
        value /= num
    return value

def string_to_num(calculate_data):
    data = []
    for _ in calculate_data.split(","):
        data.append(eval(_))
    return data

def input_operator(choose_operator):
    if choose_operator == "+":
        print(f'the addtion value of {calculate_data} is {add(data)}')
    elif choose_operator == "-":
        print(f'the substraction value of {calculate_data} is {substraction(data)}')
    elif choose_operator == "*":
        print(f'the multiplied value of {calculate_data} is {multiply(data)}')
    else:
        print(f'the division value of {calculate_data} is {division(data)}')

choose_operator = input("Please choose the operator from +, -, *, / ")
calculate_data = input("Please give the data list such as 1,2,3,4 : ")
data = string_to_num(calculate_data)
input_operator(choose_operator)

