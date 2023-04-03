import tkinter as tk

# create the root window
root = tk.Tk()

# set the size and title of the window
root.geometry("300x300")
root.title("Listbox Widget Example")

# create a Label widget
label = tk.Label(root, text="Select your favorite fruits:")
label.pack()

# create a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Orange", "Strawberry"]

# create a Listbox widget with the fruits
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for fruit in fruits:
    listbox.insert(tk.END, fruit)
listbox.pack()

# define the submit function
def submit():
    # get the indices of the selected items in the Listbox widget
    selected = [fruits[i] for i in listbox.curselection()]
    if selected:
        # if at least one fruit is selected, update the message Label widget
        message.config(text="Your favorite fruits are: " + ", ".join(selected))
    else:
        # if no fruit is selected, display a message asking the user to select at least one fruit
        message.config(text="Please select at least one fruit.")

# create a Button widget to submit the selected fruits
button = tk.Button(root, text="Submit", command=submit)
button.pack()

# create a Label widget for the message
message = tk.Label(root, text="")
message.pack()

# start the main event loop
root.mainloop()