from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("calculator.ico")

e = Entry(root, width=35, justify="right")
e.grid(columnspan=4)


# function of button
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = eval(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = eval(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = eval(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "dividsion"
    f_num = eval(first_number)
    e.delete(0, END)


def button_sqt():
    number = eval(e.get())
    e.delete(0, END)
    e.insert(0, f"{number ** 0.5}")
    global math
    math = "square root"


def button_square():
    number = eval(e.get())
    e.delete(0, END)
    e.insert(0, f"{number ** 2}")
    global math
    math = "square"


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f"{f_num + eval(second_number)}")

    if math == "subtraction":
        e.insert(0, f"{f_num - eval(second_number)}")

    if math == "multiplication":
        e.insert(0, f"{f_num * eval(second_number)}")

    if math == "dividsion":
        try:
            e.insert(0, f"{f_num / eval(second_number)}")
        except ZeroDivisionError:
            e.insert(0,"錯誤")

    if math == "square root":
        number = eval(second_number)
        e.insert(0, f"{number ** 0.5}")

    if math == "square":
        number = eval(second_number)
        e.insert(0, f"{number ** 2}")


# Define the buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_dot = Button(root, text="●", padx=38, pady=20, command=lambda: button_click("."))

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=89, pady=20, command=button_equal)
button_clear = Button(root, text="AC", padx=36, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

button_sqt = Button(root, text="\u221A", font=("arail", 10), padx=39, pady=20, command=button_sqt)
button_square = Button(root, text="X\u00B2", font=("arail", 10), padx=39, pady=20, command=button_square)

# put all buttons on the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_dot.grid(row=5, column=1)

button_clear.grid(row=1, column=0)
button_sqt.grid(row=1, column=1)
button_square.grid(row=1, column=2)
button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=2, columnspan=2)

button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

root.mainloop()
