import tkinter as tk
from tkinter import ttk
window = tk.Tk()

window.title("My Window")
window.geometry("600x600+0+0")
namelabel = ttk.Label(window, text="Miss P", foreground="red", font=("Helvetica", 58))
namelabel.pack()

window.mainloop()