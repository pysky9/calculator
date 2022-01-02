from tkinter import *

def btn(char):
    global operator
    operator += char
    values.set(operator)

def Clear():
    global operator
    operator = ""
    values.set(operator)
    Display.insert(0,"0")

def plus_minus():
    pass

def percentage():
    pass

def Equal():
    global operator
    total = float(eval(operator))
    values.set(total)
    operator = ""

window = Tk()

window.title("計算機")

operator = ""
values = StringVar(value="0")


Display = Entry(window, font=("arial", 20, "bold"), fg="white", bg='black', bd=80, justify="right", textvariable=values)
Display.grid(columnspan=4)

btn_clear = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="light gray", bd=15, text="AC", command=Clear).grid(row=1, column=0)
btn_plus_minus = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="light gray", bd=15, text="+/-").grid(row=1, column=1)
btn_percent = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="light gray", bd=15, text="%").grid(row=1, column=2)
btn_division = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="orange", bd=15, text="÷", command=lambda:btn("/")).grid(row=1, column=3)

btn_7 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="7", command=lambda:btn("7")).grid(row=2, column=0)
btn_8 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="8", command=lambda:btn("8")).grid(row=2, column=1)
btn_9 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="9", command=lambda:btn("9")).grid(row=2, column=2)
btn_multiply = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="orange", bd=15, text="x", command=lambda:btn("*")).grid(row=2, column=3)

btn_4 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="4", command=lambda:btn("4")).grid(row=3, column=0)
btn_5 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="5", command=lambda:btn("5")).grid(row=3, column=1)
btn_6 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="6", command=lambda:btn("6")).grid(row=3, column=2)
btn_minus = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="orange", bd=15, text="-", command=lambda:btn("-")).grid(row=3, column=3)

btn_1 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="1", command=lambda:btn("1")).grid(row=4, column=0)
btn_2 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="2", command=lambda:btn("2")).grid(row=4, column=1)
btn_3 = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="3", command=lambda:btn("3")).grid(row=4, column=2)
btn_plus = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="orange", bd=15, text="+", command=lambda:btn("+")).grid(row=4, column=3)

btn_0 = Button(window, padx=80, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="0", command=lambda:btn("0")).grid(row=5, column=0, columnspan=2)
btn_dot = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="gray", bd=15, text="●", command=lambda:btn(".")).grid(row=5, column=2)
btn_equal = Button(window, padx=20, pady=10, font=("arail", 20, "bold"), fg="white", bg="orange", bd=15, text="=", command=Equal).grid(row=5, column=3)

window.mainloop()