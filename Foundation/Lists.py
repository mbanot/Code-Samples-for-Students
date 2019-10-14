#Python lists are collections which are both ordered and changeable.
#Lists are recognizable because of their square brackets.

#A list is defined as shown below:

newList = ["red", "green", "Blue"]

#Items in a list can be accessed by using the item index as shown below:

greenListItem = newList[1]

#Negative indexing can be used to reference list items starting from the last item to the first:

blueListItem = newList[-1]
redListItem = newList[-3]

#An entire range in a list can be accessed, for example list[n:m] accesses items in list from index n to index m-1:

colourRange = newList[1,3]

#A range of indexes can also be accessed using negative indexes when accessing items from the end of the list:

negColourRange = newList[-2,-1]

#A list item can also be changed using the index:

newList[2] = "blue"

#A list can be traversed using a for loop:

count = 0
for x in newList:
  count = count + 1
  
#It is also possible to search for a list item:

redBool = false
if "red" in newList:
  redBool = true
#To get the length of the string, the len function can be used:

listLength = len(newList)

#The append function is used to add items to the end of a list:

newList.append("yellow")

#However, to add the new item at a specified index, the insert function is used:

newList.insert(1, "pink")
newList.insert(0, "purple")

#To remove a list item at the end of the list, the pop function can be used:

newList.pop()

#The remove function is used to remove a specified list item:

newList.remove("pink")

#The del function can be used to remove a list item at a selected index:

newList.del[0]

#The copy function is used to copy an entire list:

colorList = newList.copy()

#Lists can be joined using the addition sign:

differentList = newList + colorList

#The sort function is used to sort the list items:

differentList = colorList.sort()

#Reverse function is used to change the order of the list:

colorList = newList.reverse()

#To clear the entire list, the clear function is used:

colorList.clear()

#The list constructor can also be used to create a list:

colorList = list(("Kwekwe","Harare","Bulawayo"))
