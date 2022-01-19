import tkinter
from tkinter import *


def btn_num(num):
    current = Display.get()
    Display.delete(0, END)

    value.set(str(current) + str(num))


def add():
    first_number = Display.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    Display.delete(0, END)


def substraction():
    first_number = Display.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    Display.delete(0, END)


def multiplication():
    first_number = Display.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    Display.delete(0, END)


def division():
    first_number = Display.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    Display.delete(0, END)


def equal():
    second_number = Display.get()
    Display.delete(0, END)
    if math == "addition":
        value.set(f_num + int(second_number))

    elif math == "substraction":
        value.set(f_num - int(second_number))

    elif math == "multiplication":
        value.set(f_num * int(second_number))

    else:
        value.set(f_num / int(second_number))


def clear():
    Display.delete(0, END)


window = Tk()
window.title("iphone calculator")

operator = ''
value = StringVar(value="")

Display = Entry(window, font=("arial", 15, "bold"), fg="black", bg="light blue", justify="right", textvariable=value)
Display.grid(columnspan=4)

# 設定按鈕
btn7 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='7',
              command=lambda: btn_num(7)).grid(row=1, column=0)
btn8 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='8',
              command=lambda: btn_num(8)).grid(row=1, column=1)
btn9 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='9',
              command=lambda: btn_num(9)).grid(row=1, column=2)
btn_plus = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='+', command=add).grid(
    row=1, column=3)

btn4 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='4',
              command=lambda: btn_num(4)).grid(row=2, column=0)
btn5 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='5',
              command=lambda: btn_num(5)).grid(row=2, column=1)
btn6 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='6',
              command=lambda: btn_num(6)).grid(row=2, column=2)
btn_minus = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='-',
                   command=substraction).grid(row=2, column=3)

btn1 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='1',
              command=lambda: btn_num(1)).grid(row=3, column=0)
btn2 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='2',
              command=lambda: btn_num(2)).grid(row=3, column=1)
btn3 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='3',
              command=lambda: btn_num(3)).grid(row=3, column=2)
btn_multiply = Button(window, padx=30, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='x',
                      command=multiplication).grid(row=3, column=3)

btn0 = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='0',
              command=lambda: btn_num(0)).grid(row=4, column=0)
# btn_dot = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='●', command=lambda:btn_num('.')).grid(row=4, column=1)
btn_division = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='÷',
                      command=division).grid(row=4, column=2)
btn_clear = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='AC',
                   command=clear).grid(row=4, column=3)

btn_equal = Button(window, padx=20, pady=10, bd=10, fg='black', font=('arail', 15, 'bold'), text='=',
                   command=equal).grid(row=5, column=0)

window.mainloop()
