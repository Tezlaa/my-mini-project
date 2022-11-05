from tkinter import *
from tkinter import ttk


def add_number(number):
    output = field_write.get() + str(number)
    field_write.delete(0, END)
    field_write.insert(0, output)

def make_button(number):
    return Button(text=number, font=("", 20), bd=12, command=lambda: add_number(number))
 
def make_operation_button(operation):
    return Button(text=operation, font=("", 20), foreground="black", bd=12, command=lambda: add_number(operation))

def make_result(operation):
    return Button(text=operation, font=("", 20), foreground="black", bd=12, command=lambda: add_number(operation))

main_menu = Tk()

"""Visual for the window"""
main_menu.geometry("250x400+1500+100")
main_menu.resizable(False, False)
main_menu.title("CALCULATOR")
main_menu.iconbitmap(default="D:\Developments\Python\GIT\mini-project\Project\Calculator Tkinter\icon.ico")
main_menu.attributes("-alpha", 1)
main_menu["bg"] = "#fff3bf"

#main input field 
field_write = ttk.Entry(main_menu, justify=RIGHT, font=("", 20,), width=15)
field_write.grid(row=0, column=0, columnspan=4, sticky="we")

#created buttons with numbers from 9 to 0
make_button(1).grid(row=1, column=0, sticky="wens",padx=2, pady=2)
make_button(2).grid(row=1, column=1, sticky="wens",padx=2, pady=2) 
make_button(3).grid(row=1, column=2, sticky="wens",padx=2, pady=2) 
make_button(4).grid(row=2, column=0, sticky="wens",padx=2, pady=2) 
make_button(5).grid(row=2, column=1, sticky="wens",padx=2, pady=2) 
make_button(6).grid(row=2, column=2, sticky="wens",padx=2, pady=2) 
make_button(7).grid(row=3, column=0, sticky="wens",padx=2, pady=2) 
make_button(8).grid(row=3, column=1, sticky="wens",padx=2, pady=2) 
make_button(9).grid(row=3, column=2, sticky="wens",padx=2, pady=2) 

make_button(0).grid(row=4, column=0, columnspan=2, sticky="wens",padx=2, pady=2)

#created buttons with operation
make_operation_button("+").grid(row=1, column=3, sticky="wens", padx=2, pady=2)
make_operation_button("-").grid(row=2, column=3, sticky="wens", padx=2, pady=2)
make_operation_button("/").grid(row=3, column=3, sticky="wens", padx=2, pady=2)
make_operation_button("*").grid(row=4, column=3, sticky="wens", padx=2, pady=2)

make_result("=").grid(row=4, column=2, sticky="wens", padx=2, pady=2)

#increase size number
for i in range(1, 7):
    main_menu.grid_rowconfigure(i, minsize=60)
for j in range(3):
    main_menu.grid_columnconfigure(j, minsize=60)

main_menu.mainloop()