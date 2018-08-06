import tkinter as tk
from tkinter import ttk
window = tk.Tk()

window.title("My Window")
window.geometry("600x600+0+0")

namelabel = ttk.Label(window, text="Miss P", foreground="red", font=("Helvetica", 58))
namelabel.pack()

whatisnamelabel = ttk.Label(window, text="Hello, what is your name?")
whatisnamelabel.pack()

nameentry = ttk.Entry(window)
nameentry.insert(0, "DEFAULT")
nameentry.pack()

whatisanimallabel = ttk.Label(window, text="What is your favourite animal?")
whatisanimallabel.pack()

#To use radiobuttons, we first need a variable that will hold the selected answer. For this, we could use text, but to keep it simple, we will use numbers today.
#I am going to call this variable "animalvalue"
animalvalue = 0
#Next, we are going to make the radiobuttons to add.
#The first optin is the parent - in this case, we have called it "window".
#"Text" allows us to choose what text will be displayed next to the button
#"Variable" tells us what variable the option choice is going to modify - in this case, all three buttons will modify the "animalvalue" variable
#"Value" tells the computer what to set the variable that we previously chose to.
animalone = ttk.Radiobutton(window, text="Cats", variable=animalvalue, value=1)
animaltwo = ttk.Radiobutton(window, text="Definitely cats", variable=animalvalue, value=2)
animalthree = ttk.Radiobutton(window, text="Cats are the best", variable=animalvalue, value=3)

#Don't forget to pack them!
animalone.pack()
animaltwo.pack()
animalthree.pack()

window.mainloop()