import tkinter as tk
from tkinter import ttk
window = tk.Tk()

window.title("My Window")
#Geometry is used to resize the window when it initially opens.
#The first part of teh string ("600x600") refers to the dimensions in pixels - x axis (horizontal) and y axis (vertical)
#The second part refers to the location on the screen where it first opens - again, x axis (horizontal) and then y axis (vertical) the co-ordinates start from the top-left corner of the screen
window.geometry("600x600+0+0")

#See "AddALabel" for more details about labels
#The "foreground" option allows us to set the colour of the text on the label
#The "font" option consists of several parts.
#The first part ("Helvetica") refers to the font family that the text should appear as
#The second part (58) refers to the size of the text
namelabel = ttk.Label(window, text="Miss P", foreground="red", font=("Helvetica", 58))
namelabel.pack()

window.mainloop()