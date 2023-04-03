---
layout: default
title: Week 6 - How to Interact with the User
nav_order: 6
permalink: /weekly-content/week-6
---

# Week 6 - How to Interact with the User
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## `Tkinter` - A GUI toolkit

Tkinter is an Application Programming Interface for accessing the `Tk` GUI functions supported by many programming languages 
- It provides functions for creating windows
containing interactive widgets
- Tkinter programs react to events initiated
by the user 

### Creating a window

The following code creates a window and a button in that window.

```python
# Get the Tkinter functions
from tkinter import *

# Create the window
my_window = Tk()

# Create a button for the window
my_button = Button(my_window, text="Push Me")

# Pack the button into the window
my_button.pack()

# Wait for the user to do something
my_window.mainloop()
```

### Binding events to widgets

The following code creates a window, a button, and a message in that window. When the user clicks the button, the message is displayed showing how many times the button has been clicked.

```python
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
```

## Common Widgets:

- **Label**: Displays text or an image
- **Button**: Executes a command when clicked
- **Entry**: Allows the user to enter text
- **Text**: Allows the user to enter multiple lines of text
- **Canvas**: Displays graphics and images
- **Listbox**: Displays a list of options
- **Radiobutton**: Allows the user to select one option from a group of options
- **Checkbutton**: Allows the user to select one or more options from a group of options
- **Scale**: Allows the user to select a value from a range
- **Spinbox**: Allows the user to select a value from a list of values
- **Menu**: Displays a drop-down menu
- **Menubutton**: Displays a drop-down menu when clicked
- **Message**: Displays text with word wrapping and justification
- **Scrollbar**: Allows the user to scroll through a widget

## Common Methods:

- **Widget.pack()**: Places the widget in the parent widget
- **Widget.grid()**: Places the widget in the parent widget using a grid layout
- **Widget.place()**: Places the widget in the parent widget using x and y coordinates
- **Widget.config()**: Configures the widget with a dictionary of options
- **Widget.bind()**: Binds an event to a function
- **Widget.destroy()**: Removes the widget from the parent widget
- **Widget.get()**: Returns the current value of the widget
- **Widget.set()**: Sets the value of the widget
- **StringVar()**: Creates a variable to hold a string value
- **IntVar()**: Creates a variable to hold an integer value
- **DoubleVar()**: Creates a variable to hold a floating-point value

## Common Options:

- **text**: The text to display in a Label widget
- **command**: The function to execute when a Button widget is clicked
- **variable**: The variable to hold the current value of a widget
- **value**: The value to assign to the variable when a Radiobutton or Checkbutton widget is selected
- **width**: The width of a widget in characters
- **height**: The height of a widget in characters or pixels
- **bg**: The background color of a widget
- **fg**: The foreground (text) color of a widget
- **font**: The font of a widget
- **padx**: The padding on the left and right sides of a widget
- **pady**: The padding on the top and bottom sides of a widget
- **relief**: The border style of a widget (e.g. "groove", "raised", "sunken")
- **anchor**: The position of the text within a widget (e.g. "center", "w", "e")
