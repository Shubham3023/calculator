"""Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>"""
from tkinter import *

root = Tk()
root.title("Calculator")


e = Entry(root, width=58, borderwidth=15)
e.grid(row=0, column=0, columnspan=4)

#create function to add numbers on screen by pressing them
def button_add(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

#function to clear the screen
def clear():
    e.delete(0, END)

#create functions for different operations
def sum():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "add"
    f_num = int(first_num)


def multiplication():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "mul"
    f_num = int(first_num)


def subtraction():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "sub"
    f_num = int(first_num)


def division():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    global math
    math = "div"
    f_num = int(first_num)

#create function to calculate answer
def equal():
    second_num = e.get()
    e.delete(0, END)
    #we assigned values to "math" for following operations
    if math == "add":
        answer = f_num + int(second_num)
        e.insert(0, answer)
    elif math == "sub":
        answer = f_num - int(second_num)
        e.insert(0, answer)
    elif math == "mul":
        answer = f_num * int(second_num)
        e.insert(0, answer)
    elif math == "div":
        answer = f_num / int(second_num)
        e.insert(0, answer)

#create,display and arrange buttons on screen
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))
button_sum = Button(root, text="+", padx=40, pady=20, command=sum)
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtraction)
button_mul = Button(root, text="x", padx=39, pady=20, command=multiplication)
button_div = Button(root, text="/", padx=40, pady=20, command=division)
button_clear = Button(root, text="clear", padx=79, pady=20, command=clear)
button_equal = Button(root, text="=", padx=185, pady=20, command=equal)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=1)
button_sum.grid(row=4, column=0)

button_clear.grid(row=4, column=2, columnspan=2)
button_equal.grid(row=5, column=0, columnspan=4)

root.mainloop()
