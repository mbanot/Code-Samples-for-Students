import tkinter as tk
from tkinter import ttk
window = tk.Tk()

window.title("My Window")

window.geometry("600x600+0+0")
namelabel = ttk.Label(window, text="Miss P", foreground="red", font=("Helvetica", 58))
namelabel.pack()

#In order to show the image in our program, we first need to know where to find it
#THE IMAGE NEEDS TO BE A GIF TO WORK
#The image component is found in TK, not TTK.
#We use PhotoImage to create a new object of a "PhotoImage"
#"file" tells the computer where to find the image that we a re using. For this I would recommend using relative links inside of a project folder.
#The "r" refers to a "raw" string. It means that the backslashes will be used as part of the actual string and not as an escape character like it would be in a "normal"string
#This essentially tells the computer to read the string as it is, not with any extra formatting
catimage = tk.PhotoImage(file=r"\\phs.local\Users\Home\Staff\jepetersen\Desktop\cat.gif")
#We need to make a new label (to hold the image) and use the "image" option to tell the computer where to find the PhotoImage.
catimagelabel = ttk.Label(window, image=catimage)
catimagelabel.pack()

window.mainloop()