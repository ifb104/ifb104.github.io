import tkinter as tk

# create a new window
window = tk.Tk()
window.title("Calculator")

# create a function for calculating the result
def calculate():
    # get the input values from the Entry widgets
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    # calculate the result based on the selected operation
    if var.get() == 1:
        result = num1 + num2
    elif var.get() == 2:
        result = num1 - num2
    elif var.get() == 3:
        result = num1 * num2
    elif var.get() == 4:
        result = num1 / num2

    # set the result in the Label widget
    label_result.config(text="Result: " + str(result))

# create a label for the first number
label1 = tk.Label(window, text="First number")
label1.grid(row=0, column=0, padx=10, pady=10)

# create an Entry widget for the first number
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=10)

# create a label for the second number
label2 = tk.Label(window, text="Second number")
label2.grid(row=1, column=0, padx=10, pady=10)

# create an Entry widget for the second number
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=10)

# create a variable to hold the selected operation
var = tk.IntVar()

# create a label for the operations
label_op = tk.Label(window, text="Select an operation")
label_op.grid(row=2, column=0, padx=10, pady=10)

# create Radiobutton widgets for the operations
rb_add = tk.Radiobutton(window, text="+", variable=var, value=1)
rb_add.grid(row=3, column=0, padx=10, pady=5)

rb_sub = tk.Radiobutton(window, text="-", variable=var, value=2)
rb_sub.grid(row=3, column=1, padx=10, pady=5)

rb_mul = tk.Radiobutton(window, text="*", variable=var, value=3)
rb_mul.grid(row=4, column=0, padx=10, pady=5)

rb_div = tk.Radiobutton(window, text="/", variable=var, value=4)
rb_div.grid(row=4, column=1, padx=10, pady=5)

# create a button to calculate the result
button = tk.Button(window, text="Calculate", command=calculate)
button.grid(row=5, column=0, padx=10, pady=10)

# create a label to display the result
label_result = tk.Label(window, text="Result: ")
label_result.grid(row=5, column=1, padx=10, pady=10)

# start the main event loop
window.mainloop()
