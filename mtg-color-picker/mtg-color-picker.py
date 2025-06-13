#Vision: a prompt is given to the user to pick a random number, which will be assigned to one of the colors you can play in MTG
#The user enters one of the numbers provided, which then spits out the color
#It asks the user if they would like another color
#This continues until 1. The colors are all used 2. The user says no


#So.... I think I just, write sudo-code?

#lets see, I'll need a variable to store the colors and numbers
#I'll need to do a print and a request call to the user

#From there, it should ask a couple questions to itself
#Is the number outside the range? If yes, say that's invalid and get new input
#Is the number inside the range and been selected previously? If yes, say that number has been selected
#Is the number inside the range and unselected? If yes, give the color assigned to that number
import random
print ('Welcome, please select a number')

inputSelect = input()




def colorSelection():
    colorList = ["White, ", "Blue ", "Black ", "Red ", "Green "]
    random.choice(colorList)
    return colorList



colorSelected = colorSelection()
print(colorSelected[1])
#print("Your color is " + colorSelected)










#Later case ideas, if all colors are selected in that instance, say that's all the colors available, good luck champ o7