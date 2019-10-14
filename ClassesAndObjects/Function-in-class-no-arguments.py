#Explanation and example of single function with no arguments
#kiwi class
class Kiwi:
    def __init__(self, nameVariable, ageVariable, ownerVariable, colourVariable):
        self.name = nameVariable
        self.age = ageVariable
        self.owner = ownerVariable
        self.colour = colourVariable
    
    #Kiwis need a function that allow them to change their age when it's their birthday!
    #Because we are using attributes that belong to the kiwi that calls the function(it's this specific kiwi's birthday, not every kiwi in the world's birthday!), we need to pass "self" as the first argument. That way, we can use "self" to refer to the specific kiwi who called the function in the code.
    #After the dot, we can put any attribute (or function) that exists in the object that we are accessing. In this example, we want to access the "age" attribute, so we use self (this specific object) followed by ".age" - this also works with functions as seen below!
    def birthday(self):
        self.age = self.age + 1

#main
sallyTheKiwi = Kiwi("Sally", 13, "Miss P", "blue")
hemiTheKiwi = Kiwi("Hemi", 6, "Miss P", "yellow")

#print Sally's age before we call the "birthday()" function. Let's print Hemi's too, so that we can make sure that ONLY Sally ages up
print("Sally's age is:", sallyTheKiwi.age)
print("Hemi's age is:", hemiTheKiwi.age)

#Now we will use the "sallyTheKiwi" object to call the birthday function. This means that ONLY sally should age by one year.
sallyTheKiwi.birthday()

#print Sally and Hemi's ages again so that we can check that Sally's age has gone up, and Hemi's has stayed the same.
print("Sally's age is:", sallyTheKiwi.age)
print("Hemi's age is:", hemiTheKiwi.age)
