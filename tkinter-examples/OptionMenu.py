import tkinter as tk

# create the root window
root = tk.Tk()

# set the size and title of the window
root.geometry("300x200")
root.title("Menubutton Widget Example")

# create a Label widget
label = tk.Label(root, text="Select your favorite color:")
label.pack()

# define the function to display the selected color
def display_color(color):
    message.config(text="Your favorite color is " + color + ".")
    message.config(bg=color)

# create an OptionMenu widget
color_var = tk.StringVar()
color_var.set("Red")
color_menu = tk.OptionMenu(root, color_var, "Red", "Green", "Blue", "Purple", "Black", command=display_color)
color_menu.pack()

# create a Label widget for the message
message = tk.Label(root, text="", fg="white")
message.pack()

# start the main event loop
root.mainloop()