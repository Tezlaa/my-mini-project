from tkinter import *
from tkinter import ttk
from math import *

def add_number(number):
    output = field_write.get()
    if output[0] == '0':
        output = output[1:]
    field_write.delete(0, END)
    field_write.insert(0, output+str(number))
    
def add_operation(operation):
    output = field_write.get()
    if output[-1] in '-+/*^.√':
        output = output[:-1]
    elif '+' in output or '-' in output or '/' in output or '*' in output:
        calculate()
        output = field_write.get()
    field_write.delete(0, END)
    field_write.insert(0, output + operation)
    
def calculate():
    value = field_write.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    field_write.delete(0, END)
    field_write.insert(0, eval(value))

def make_button(number):
    return Button(text=number, font=("Arial", 20), foreground="black", background="white",\
                    command=lambda: add_number(number))
 
def make_operation_button(operation):
    return Button(text=operation, font=("Arial", 20), foreground="black", background="white",\
                    command=lambda: add_operation(operation))

def make_button_result(operation):
    return Button(text=operation, font=("Arial", 20), foreground="black", background="white",\
                    command=calculate)

main_menu = Tk()

#Visual for the window
main_menu.geometry("266x400+1500+100")
main_menu.resizable(False, False)
main_menu.title("CALCULATOR")
main_menu.iconbitmap(default="D:\Developments\Python\GIT\mini-project\Project\Calculator Tkinter\icon.ico")
main_menu.attributes("-alpha", 1)
main_menu["bg"] = "white"

#main input field 
field_write = ttk.Entry(main_menu, justify=RIGHT, font=("", 20,), width=13)
field_write.insert(0, '0')
field_write.grid(row=0, column=0, columnspan=4, sticky="we")

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
make_operation_button("^").grid(row=2, column=4, sticky="wens", padx=1, pady=2) #pow
make_operation_button(".").grid(row=3, column=4, sticky="wens", padx=1, pady=2) #dot 
make_operation_button("√").grid(row=4, column=4, sticky="wens", padx=1, pady=2) #sqrt

make_button_result("=").grid(row=1, column=4, sticky="wens", padx=1, pady=2)

#increase size number
for i in range(1, 7):
    main_menu.grid_rowconfigure(i, minsize=60)
for j in range(3):
    main_menu.grid_columnconfigure(j, minsize=60)

main_menu.mainloop()