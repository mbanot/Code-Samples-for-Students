#Explanation and example of multiple functions with and without arguments
#kiwi class
class Kiwi:
    def __init__(self, nameVariable, ageVariable, ownerVariable, colourVariable):
        self.name = nameVariable
        self.age = ageVariable
        self.owner = ownerVariable
        self.colour = colourVariable

    def birthday(self):
        self.age = self.age + 1
    
    #This time, we want to create a function that will take a specific piece of information and apply it to one of our kiwi's attributes
    #In this function, we want to be able to change the colour of a kiwi for when they get a haircut!
    #The first argument we need is "self" because we want to run this method with a specific kiwi! Our next argument needs to be the thing we are using in the method - this will be our new hair colour!
    def changeColour(self, colour):
        #Here we are saying the the colour attribute of the kiwi that called this function should be assigned to the value of the argument called "colour"
        self.colour = colour

#main
sallyTheKiwi = Kiwi("Sally", 13, "Miss P", "blue")
hemiTheKiwi = Kiwi("Hemi", 6, "Miss P", "yellow")

print("Sally's age is:", sallyTheKiwi.age)
print("Hemi's age is:", hemiTheKiwi.age)

sallyTheKiwi.birthday()

print("Sally's age is:", sallyTheKiwi.age)
print("Hemi's age is:", hemiTheKiwi.age)

print("Hemi's colour is:", hemiTheKiwi.colour)

hemiTheKiwi.changeColour("green")

print("Hemi's colour is:", hemiTheKiwi.colour)
