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

animalvalue = 0
animalone = ttk.Radiobutton(window, text="Cats", variable=animalvalue, value=1)
animaltwo = ttk.Radiobutton(window, text="Definitely cats", variable=animalvalue, value=2)
animalthree = ttk.Radiobutton(window, text="Cats are the best", variable=animalvalue, value=3)
animalone.pack()
animaltwo.pack()
animalthree.pack()

#A button is made the same way as other widgets
#The first option is the parent, which in this example is "window"
#"Text" can be used to specify the text that will be displayed on the button
enterbutton = ttk.Button(window, text = "Click Me!")
enterbutton.pack()

window.mainloop()