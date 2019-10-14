#In this sample, we will create a class that holds the attributes (and functions - we'll get to that later) of a given kiwi object

#By convention user-defined classes have names that start with a capital letter. Any further words in the class name also start with a capital letter with no underscores.
class Kiwi:
    #create a constructor for the kiwi class. This is a special function that is run every time a new "instance" of the kiwi class is created.
    #"Instance" in this context means this particular object
    #We need to call our function __init__ (2 underscores + "init" + 2 underscores) so that the computer knows that THIS FUNCTION is the constructor. It's a special word in python, just like "print" or "input"
    #The first "argument"/"input parameter" you need to need to have in your class is called "self". This literally refers to the object itself
    def __init__(self, nameVariable, ageVariable, ownerVariable, colourVariable):
        #When we use the keyword "self" here we are telling the computer to take the variable and stick it to the object in the slot we want
        #For example, the code below is going to take whatever we put in the "nameVariable" variable and then put it inside of this new object's "name" slot. These "slots" can be called "properties" or "attributes"
        #The kiwi is going to have a number of different attributes. These include the name (string), age (int), owner (string), and colour (string)
        self.name = nameVariable
        self.age = ageVariable
        self.owner = ownerVariable
        self.colour = colourVariable

#create some kiwis!
#When we create a new object, we need to follow the same order of arguments/input parameters as the __init__ function, otherwise the computer will get confused.
#Self is automatically there, we don't need to include it when we create an object.
#Here we have Sally (name) the kiwi. She is 13 years old, Miss P is her owner, and she is the colour blue.
sallyTheKiwi = Kiwi("Sally", 13, "Miss P", "blue")
hemiTheKiwi = Kiwi("Hemi", 1, "Miss P", "yellow")

#Below, we're just going to print the name attribute of the sallyTheKiwi object so that we can check that it was saved correctly.
print("The name of the kiwi is", sallyTheKiwi.name)
