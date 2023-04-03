import tkinter as tk

# Create the root window
root = tk.Tk()
root.geometry("300x300")
root.title("Checkbutton Widget Example")

# Create a label
label = tk.Label(root, text="Select your favourite programming languages:")
label.pack()

languages = ["Python", "Java", "JavaScript", "C++"]
vars = []

# Create a checkbutton for each language
for lang in languages:
    var = tk.BooleanVar()
    vars.append(var)
    cb = tk.Checkbutton(root, text=lang, variable=var)
    cb.pack()

# Create a button to submit the checkbuttons
def submit():
    selected = []
    for i in range(len(languages)):
        if vars[i].get():
            selected.append(languages[i])
    if selected:
        message.config(text="Your favourite languages are: " + ", ".join(selected))
    else:
        message.config(text="Please select at least one language.")

button = tk.Button(root, text="Submit", command=submit)
button.pack()

# Create a label to display the message
message = tk.Label(root, text="")
message.pack()

root.mainloop()
