import tkinter as tk

# Create the root window
root = tk.Tk()
root.geometry("300x100")
root.title("Entry Widget Example")

# Create a label and an entry widget
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button to submit the entry widget
def submit():
    name = entry.get()
    if len(name) > 0:
        greeting.config(text="Hello, " + name + "!")
    else:
        greeting.config(text="Please enter your name.")

button = tk.Button(root, text="Submit", command=submit)
button.pack()

# Create a label to display the greeting
greeting = tk.Label(root, text="")
greeting.pack()

root.mainloop()
