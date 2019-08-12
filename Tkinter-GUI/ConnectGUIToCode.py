#PLEASE NOTE: For this code we would usually implement error checking to make sure that all of the class values are unique. This has not been done in this case to save time.

#YOU WILL NOT BE ABLE TO RUN THIS PROGRAM IN REPL.IT AS IT DOES NOT SUPPORT GUI APPLICATIONS. PLEASE COPY AND PASTE THE CODE INTO A .PY FILE ON YOUR OWN MACHINE.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Student:
	name = ""
	studentID = ""
	yearLevel = 0
	classes = []

	def __init__(self, name, studentID, yearLevel, class1, class2, class3, class4, class5):
		self.name = name
		self.studentID = studentID
		self.yearLevel = yearLevel
		self.classes = [class1, class2, class3, class4, class5]

	def PrintDetails(self):
            #this method holds all of the calculatey stuff for the student
		numOfClasses = 0
		classesString = ""
		while (numOfClasses < 5):
				classesString += self.classes[numOfClasses]
				if (numOfClasses <4):
					classesString += ", "
				numOfClasses += 1
                #we need to create a new string to give the gui later on
		#this is the string that the GUI will show to the user once they make a new student
		detailsString = "Hello, my name is " + self.name + ", my student ID is " + self.studentID + ", and my year level is " + str(self.yearLevel) + ". I take the following classes: " + classesString + "."
		#I will print this string to the console so that I can test it and make sure that everything is running okay
		print(detailsString)
		#I need to give the GUI something back when it finishes running this method.
		#I use the "return" statement to give back the user a string to display in the GUI.
		return detailsString

class Window:
    
    #set up instance variables
    # MAKE SURE THAT YOU ALWAYS DECALRE YOUR ROOT/PARENT WINDOW FIRST
    window = tk.Tk()
    nameentry = ttk.Entry()
    identry = ttk.Entry()
    textlabel = ttk.Label()
    yearvalue = tk.IntVar()
    classonevalue = tk.StringVar()
    classtwovalue = tk.StringVar()
    classthreevalue = tk.StringVar()
    classfourvalue = tk.StringVar()
    classfivevalue = tk.StringVar()
    
    def __init__(self):

        self.window.title("My Window")

        self.window.geometry("600x600+0+0")
        titlelabel = ttk.Label(self.window, text="Students At Pap High", foreground="red", font=("Helvetica", 58))
        titlelabel.pack()

        namelabel = ttk.Label(self.window, text="Please enter your name:")
        namelabel.pack()
        self.nameentry = ttk.Entry(self.window)
        self.nameentry.insert(0, "name")
        self.nameentry.pack()
        
        idlabel = ttk.Label(self.window, text="Please enter your student ID:")
        idlabel.pack()
        self.identry = ttk.Entry(self.window)
        self.identry.pack()

        yearlabel = ttk.Label(self.window, text="What year are you?")
        yearlabel.pack()
        yearnine = ttk.Radiobutton(self.window, text="9", variable=self.yearvalue, value=9).pack()
        yearten = ttk.Radiobutton(self.window, text="10", variable=self.yearvalue, value=10).pack()
        yeareleven = ttk.Radiobutton(self.window, text="11", variable=self.yearvalue, value=11).pack()
        yeartwelve = ttk.Radiobutton(self.window, text="12", variable=self.yearvalue, value=12).pack()
        yearthirteen = ttk.Radiobutton(self.window, text="13", variable=self.yearvalue, value=13).pack()

        chooselabel = ttk.Label(self.window, text="Choose your classes below:")
        chooselabel.pack()
        
        #Create list of option choices:
        classoptions = [
            "DTP",
            "DTW",
            "Health",
            "PE",
            "English",
            "Stats",
            "Calc",
            "Dance",
            "Chem",
            "Bio",
            "Physics",
            "Photography",
            "Media",
            "Social"
        ]
    
        #Variable to hold the option chosen for class one
        #STRINGVAR
        classonechoice = tk.OptionMenu(self.window, self.classonevalue, *classoptions)
        classonechoice.pack()

        classtwochoice = tk.OptionMenu(self.window, self.classtwovalue, *classoptions)
        classtwochoice.pack()

        classthreechoice = tk.OptionMenu(self.window, self.classthreevalue, *classoptions)
        classthreechoice.pack()

        classfourchoice = tk.OptionMenu(self.window, self.classfourvalue, *classoptions)
        classfourchoice.pack()
        
        classfivechoice = tk.OptionMenu(self.window, self.classfivevalue, *classoptions)
        classfivechoice.pack()

        enterbutton = ttk.Button(self.window, text="Add Student", command=self.RunMethods)
        enterbutton.pack()
        
        self.textlabel = ttk.Label(self.window)
        self.textlabel.pack()
        
    def RunMethods(self):
        #get required information from the gui
        #first, get the name of the student from the name entry field
        name = self.nameentry.get()
        #next, get the id of the student from the id entry field
        id = self.identry.get()
        year = self.yearvalue.get()
        #get the name of the first class from the class value
        classone = self.classonevalue.get()
        classtwo = self.classtwovalue.get()
        classthree = self.classthreevalue.get()
        classfour = self.classfourvalue.get()
        classfive = self.classfivevalue.get()
        
        #next, we want to create a student object so that we are able to use it's methods
        student = Student(name, id, year, classone, classtwo, classthree, classfour, classfive)
        #we need to make a variable to hold the result of the PrintDetails method. This is the thing that comes out of the "return" statement
        studentString = student.PrintDetails()
        #in the messagebox we are going to show the text that came out of the printdetails method.
        messagebox.showinfo("You have created a student!", studentString)
        
    def ShowWindow(self):
        tk.mainloop()
        
window = Window()
window.ShowWindow()

