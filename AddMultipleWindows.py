import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Window:
    
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Window One")
        label = ttk.Label(self.window, text="WINDOW 1", foreground="red", font=("Helvetica", 58))
        label.pack()
        
        changeWindowButton = ttk.Button(self.window, text="Change Window", command=self.OpenWindow2)
        changeWindowButton.pack()
        
    def ShowWindow(self):
        tk.mainloop()
        
    def OpenWindow2(self):
        window2 = SecondWindow()
        self.window.destroy()
        
class SecondWindow:
    
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Window Two")
        label = ttk.Label(self.window, text="WINDOW 2", foreground="red", font=("Helvetica", 58))
        label.pack()
        
        changeWindowButton = ttk.Button(self.window, text="Change Window", command=self.OpenWindow1)
        changeWindowButton.pack()
        
    def ShowWindow(self):
        tk.mainloop()
        
    def OpenWindow1(self):
        window1 = Window()
        self.window.destroy()
        
window = Window()
window.ShowWindow()
