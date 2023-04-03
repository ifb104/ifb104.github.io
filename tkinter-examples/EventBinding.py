from tkinter import *

# Create the window
my_window = Tk()

# Create a button for the window
my_button = Button(my_window, text="Push Me")

# Create a message for the window
my_message = Message(my_window, text="You have not clicked the button yet.")

# Create a counter for the number of times the button has been clicked
counter = 0

# Define a function to be called when the button is clicked
def button_clicked():
    global counter
    counter = counter + 1
    my_message["text"] = "You have clicked the button " + str(counter) + " times."

# Bind the button to the function
my_button["command"] = button_clicked

# Pack the button and message into the window
my_button.pack()
my_message.pack()

# Wait for the user to do something
my_window.mainloop()