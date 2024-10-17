# import tkinter
import tkinter as tk

# create the window
root = tk.Tk()
# create the title
root.title("Simple calculator")
# set the size 
root.geometry('500x400')
# Create the entry widgit
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
# Crweate Global expression
expression = ""
# Function to update expression in entry
def button_click(number):
    global expression
    expression += str(number)
    entry.delete(0, tk.END)
    entry.insert(tk.END,expression)

# Function to clear the entry
def button_clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)
    # entry.insert(tk.END,expression)

# function to evaluate the expression
def button_equal():
    try:
        global expression
        # eval() evaluate the string expression
        result = str(eval(expression)) 
        entry.delete(0, tk.END)
        entry.insert(tk.END,result)
        # reset the expression to the result
        expression = result 
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')

# function for handle arithmetric operations
def button_operation(operator):
    global expression
    expression += operator
    entry.delete(0, tk.END)
    entry.insert(tk.END,expression)

# Button definations
# Create button from 1 till 0 
button_1 = tk.Button(root, text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2 = tk.Button(root, text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3 = tk.Button(root, text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4 = tk.Button(root, text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5 = tk.Button(root, text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6 = tk.Button(root, text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7 = tk.Button(root, text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8 = tk.Button(root, text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9 = tk.Button(root, text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0 = tk.Button(root, text="0",padx=40,pady=20,command=lambda:button_click(0))

# Create button for the mathematical operation
button_add = tk.Button(root, text="+",padx=40,pady=20,command=lambda:button_operation('+'))
button_substract = tk.Button(root, text="-",padx=40,pady=20,command=lambda:button_operation('-'))
button_multiply = tk.Button(root, text="*",padx=40,pady=20,command=lambda:button_operation("*"))
button_divide = tk.Button(root, text="/",padx=40,pady=20,command=lambda:button_operation('/'))

# create button for clear and equal
button_equal = tk.Button(root, text="=",padx=40,pady=20,command=button_equal)
button_clear = tk.Button(root, text="c",padx=40,pady=20,command=button_clear)

# define the position for the buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

button_add.grid(row=1,column=3)
button_substract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)

button_equal.grid(row=5,column=1, columnspan=2)
button_clear.grid(row=4,column=1, columnspan=2)



root.mainloop()