import tkinter as tk
from tkinter import ttk
window = tk.Tk()

window.title("My Window")
window.geometry("600x600+0+0")

namelabel = ttk.Label(window, text="Miss P", foreground="red", font=("Helvetica", 58))
namelabel.pack()

whatisnamelabel = ttk.Label(window, text="Hello, what is your name?")
whatisnamelabel.pack()

#Entry for one line of text input, Text for multiple lines of text input, Label for uneditable text
#The entry uses the "window" as the parent. Make sure that you put the name of the parent inside the brackets
#Don't forget to include ttk before the fullstop!
nameentry = ttk.Entry(window)

#Would you like to add a defult value? This value will be displayed by default if the user has not written anything inside the box yet.
nameentry.insert(0, "DEFAULT")
nameentry.pack()

window.mainloop()