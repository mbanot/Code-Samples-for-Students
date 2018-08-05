import tkinter as tk
#We need to import another part of Tkinter called "ttk" in order to build the components of our GUI
#ttk is "themed tkinter" which helps us make our GUI look beautiful
from tkinter import ttk

window = tk.Tk()
window.title("Labels")

#To add WIDGETS to the window we need to make sure that we are writing code AFTER the instance was created but BEFORE we display the window to the user
#We are going to put a label inside our window
label0 = ttk.Label(window, text="A Label").grid(column=0, row=0)

window.mainloop()