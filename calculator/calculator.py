total = float(input("enter the number: "))

while True:
    operator = input("enter the operator like +,-,*,/,= ")
    if operator == "+":
        num = float(input("enter the number: "))
        total += num
    elif operator == "*":
        num = float(input("enter the number: "))
        total *= num
    elif operator == "-":
        num = float(input("enter the number: "))
        total -= num
    elif operator == "/":
        num = float(input("enter the number: "))
        total /= num
    elif operator == "=":
        print(total)
        break
    print(total)


