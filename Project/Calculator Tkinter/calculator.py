from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import *

def add_number(number):
    output = field_write.get()
    if output[0] == '0' and len(output)==1:
        output = output[1:]
    field_write.delete(0, END)
    field_write.insert(0, output+str(number))
    
def add_operation(operation):
    output = field_write.get()
    if operation == "√":
        operation = "sqrt("+ output +")"
        field_write.delete(0, END)
        field_write.insert(0, operation)
        return
    elif operation == "^":
        operation = output + "**"
        field_write.delete(0, END)
        field_write.insert(0, operation)
        return
    elif output[-1] in '-+/*':
        output = output[:-1]
    elif '+' in output or '-' in output or '/' in output or '*' in output or '**' in output or "sqrt" in output:
        calculate()
        output = field_write.get()
    field_write.delete(0, END)
    field_write.insert(0, output + operation)

def calculate():
    value = field_write.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    field_write.delete(0, END)
    try:
        field_write.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("ERROR", "You write other symbol")
        field_write.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo("ERROR", "Cannot divide by zero")
        field_write.insert(0, 0)

def clear_input():
    field_write.delete(0, END)
    field_write.insert(0, 0)

def press_key(event):
    if event.char.isdigit():
        add_number(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

def make_button(number):
    return Button(text=number, font=("Arial", 20), foreground="black", background="white",\
                    command=lambda: add_number(number))
 
def make_operation_button(operation):
    return Button(text=operation, font=("Arial", 20), foreground="black", background="white",\
                    command=lambda: add_operation(operation))

def make_button_result(operation):
    return Button(text=operation, font=("Arial", 20), foreground="black", background="white",\
                    command=calculate)

def make_clean_button(symbol):
    return Button(text=symbol, font=("Arial", 20), foreground="black", background="white",\
                    command=clear_input)


main_menu = Tk()

#Visual for the window
main_menu.geometry("268x300+1500+100")
main_menu.resizable(False, False)
main_menu.title("CALCULATOR")
main_menu.iconbitmap(default="D:\Developments\Python\GIT\mini-project\Project\Calculator Tkinter\icon.ico")
main_menu.attributes("-alpha", 1)
main_menu["bg"] = "white"

#bind on number
main_menu.bind('<Key>', press_key)

#main input field 
field_write = ttk.Entry(main_menu, justify=RIGHT, font=("", 15,))
field_write.insert(0, 0)
field_write.grid(row=0, column=0, columnspan=4, sticky="wens")

#created buttons with numbers from 9 to 0
make_button(7).grid(row=1, column=0, sticky="wens",padx=2, pady=2)
make_button(8).grid(row=1, column=1, sticky="wens",padx=2, pady=2) 
make_button(9).grid(row=1, column=2, sticky="wens",padx=2, pady=2) 
make_button(4).grid(row=2, column=0, sticky="wens",padx=2, pady=2) 
make_button(5).grid(row=2, column=1, sticky="wens",padx=2, pady=2) 
make_button(6).grid(row=2, column=2, sticky="wens",padx=2, pady=2) 
make_button(1).grid(row=3, column=0, sticky="wens",padx=2, pady=2) 
make_button(2).grid(row=3, column=1, sticky="wens",padx=2, pady=2) 
make_button(3).grid(row=3, column=2, sticky="wens",padx=2, pady=2) 

make_button(0).grid(row=4, column=0, columnspan=2, sticky="wens",padx=2, pady=2)

#created buttons with operation
make_operation_button("+").grid(row=1, column=3, sticky="wens", padx=2, pady=2)
make_operation_button("-").grid(row=2, column=3, sticky="wens", padx=2, pady=2)
make_operation_button("/").grid(row=3, column=3, sticky="wens", padx=2, pady=2)
make_operation_button("*").grid(row=4, column=3, sticky="wens", padx=2, pady=2)

#math operation
make_operation_button("^").grid(row=4, column=4, sticky="wens", padx=1, pady=2) #pow
make_operation_button(".").grid(row=2, column=4, sticky="wens", padx=1, pady=2) #dot 
make_operation_button("√").grid(row=3, column=4, sticky="wens", padx=1, pady=2) #sqrt

make_button_result("=").grid(row=1, column=4, sticky="wens", padx=1, pady=2)
make_clean_button("C").grid(row=4, column=2, sticky="wens", padx=1, pady=2)

#increase size number

main_menu.grid_rowconfigure(0, minsize=60)

for i in range(1, 7):
    main_menu.grid_rowconfigure(i, minsize=60)
for j in range(3):
    main_menu.grid_columnconfigure(j, minsize=60)

main_menu.mainloop()