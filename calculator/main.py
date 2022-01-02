import tkinter as tk

from calculator.utils import Utils


def main():
    window = tk.Tk()
    window.title('calculator')
    window.geometry('800x600')
    window.configure(background = 'white')
    window.mainloop()
    choose_operator = input("Please choose the operator from +, -, *, / ")
    calculate_data = input("Please give the data list such as 1,2,3,4 : ")
    calculate_math = Utils(calculate_data )
    calculate_math.string_to_num(calculate_data)
    calculate_math.operator_calculate(choose_operator)


if __name__ == '__main__':
    main()