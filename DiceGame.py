# importing module to generate random numbers
import random

# range of the values of a dice
print("Minimum is 1 and Maximum is 6!")
min = 1
max = 6

# To start the loop this should be yes.
roll_again = "yes"

# Loop to roll the Dice
while roll_again.lower() == "yes" or roll_again.lower() == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    # This generates the first random dice
    print(random.randint(min, max))
    
    # This generates the second random dice
    print(random.randint(min, max))
    
    # Asks the user if they want to roll again. Any input besides yes or y will terminate the program
    roll_again = input("Roll the Dices Again?") 
