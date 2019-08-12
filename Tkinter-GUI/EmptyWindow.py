#Import the Tkinter module - this is the package that allows us to build a GUI for python
#By importing it AS "tk" it means that we are able to refer to it as "tk" throughout the code which is shorter and easier to type
#Make sure you spell "tkinter" in LOWERCASE
import tkinter as tk

#We need to create an instance(object) of the Tk class to make an actual window to work in
#Make sure that you use "tk" to the left of the fullstop to talk about Tkinter (see above) and "Tk" to talk about the class that are creating an instance of
window = tk.Tk()

#Run the "mainloop" method to make your window appear on the screen!
window.mainloop()
