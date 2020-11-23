import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = display.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    display.delete(0, tk.END)
    display.insert(0, value + digit)

def add_operation(operation):
    value = display.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+'in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = display.get()
    display.delete(0, tk.END)
    display.insert(0, value + operation)

def reset():
    display.delete(0,tk.END)
    display.insert(0, '0')

def calculate():
    value = display.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    display.delete(0, tk.END)
    try:
        display.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Attention', 'Only digits')
        display.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Attention', 'Division by zero')
        display.insert(0, 0)


def create_digit_btn(digit):
    return tk.Button(w, text = digit, width = 5, height = 2, font = ('Arial', 16), relief = tk.GROOVE,
                                 bg = "pink", activebackground = "pink", command = lambda : add_digit(str(digit)))

def create_operation_btn(oper):
    return tk.Button(w, text = oper, width = 5, height = 2, font = ('Arial', 16), relief = tk.GROOVE,
                                 bg = "pink", activebackground = "pink", command = lambda : add_operation(oper))

def press_Key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

w = tk.Tk()
w.geometry("316x320")
w.title("Calculator")
w.resizable(False, False)
w.config(bg='papayawhip')
w.bind('<Key>', press_Key)

display = tk.Entry(w, width = 28, font = "Arial 14", justify = tk.RIGHT, bd = 3)
display.insert(0, 0)
display.grid(row = 0, column = 0, columnspan = 4)

counter = 1
for r in range(1,4):
    for c in range(0,3):
        create_digit_btn(counter).grid(row = r, column = c)
        counter += 1
create_digit_btn('0').grid(row = 4, column = 0)

create_operation_btn('+').grid(row = 1, column = 3)
create_operation_btn('-').grid(row = 2, column = 3)
create_operation_btn('*').grid(row = 3, column = 3)
create_operation_btn('/').grid(row = 4, column = 3)

tk.Button(w,text="=",width = 5, height = 2, font = ('Arial', 16), relief = tk.GROOVE,
        bg = "pink", activebackground = "pink", command = calculate).grid(row = 4, column = 1)
tk.Button(w,text="C",width = 5, height = 2, font = ('Arial', 16), relief = tk.GROOVE,
        bg = "pink", activebackground = "pink", command = reset).grid(row = 4, column = 2)

w.rowconfigure(0, pad = 5)
w.rowconfigure(1, pad = 5)
w.rowconfigure(2, pad = 5)
w.rowconfigure(3, pad = 5)
w.rowconfigure(4, pad = 5)

w.columnconfigure(0, pad = 5)
w.columnconfigure(1, pad = 5)
w.columnconfigure(2, pad = 5)
w.columnconfigure(3, pad = 5)

w.mainloop()
