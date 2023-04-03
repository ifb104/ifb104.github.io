import tkinter as tk

# create the root window
root = tk.Tk()

# set the size and title of the window
root.geometry("300x200")
root.title("Radiobutton Widget Example")

# create a Label widget
label = tk.Label(root, text="Select your gender:")
label.pack()

# define the function to display the selected gender
def display_gender():
    message.config(text="Your gender is " + gender_var.get() + ".")

# create a StringVar object to hold the selected gender
gender_var = tk.StringVar()

# create Radiobutton widgets for the gender options
options = ["Male", "Female", "Other"]
radio_buttons = []
for option in options:
    new_radio = tk.Radiobutton(root, text=option, variable=gender_var, value=option, command=display_gender)
    new_radio.pack()

# create a Label widget for the message
message = tk.Label(root, text="")
message.pack()

# start the main event loop
root.mainloop()
