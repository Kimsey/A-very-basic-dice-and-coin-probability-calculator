# Classical Probability
# Number of Outcomes Contained in the event E / total number of outcomes in the sample size
# Example Problem Of Coins tossed
import random

# Coin Flip
from Practice_Project_2 import chance

coin = ["H", "T"]
heads = "H"
again = True
while again:
    try:
        num_of_flips = int(input("How number of coin flips: "))
    except ValueError:
        print("Please try again")
    else:
        again = False
update = 0
head = 0
while num_of_flips > update:
    flip = coin[random.randint(0, 1)]
    print("Flip", update + 1, ":", flip)
    if flip == heads:
        head += 1
    update += 1
print("The amount of heads you got:", head)


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


factorial_of_num_of_flips = int(factorial(num_of_flips))
factorial_of_amt_of_heads = int(factorial(head))
total_of_tails = (num_of_flips - head)
factorial_of_amt_of_tails = int(factorial(total_of_tails))
combine = int(factorial_of_num_of_flips / (factorial_of_amt_of_heads * factorial_of_amt_of_tails))
exp = pow(2, num_of_flips)
percent = (combine / exp) * 100
print("The probability of getting that amount of heads in that amount of flips is", format(percent, ".2f"), "%")

# Dice
redo = True
while redo:
    try:
        roll = int(input("How number of dice rolls, but please under a number 5: "))
        while roll > 5:
            print("Please enter a number under 5")
            roll = int(input("How number of dice rolls, but please under a number 5: "))
    except ValueError as k:
        print("Please try again")
    else:
        redo = False
counter = 0
total = 0
while roll > counter:
    land = random.randint(1, 6)
    print("Roll", counter + 1, ":", land)
    total += land
    counter += 1

print("The Sum is: ", total)
Mean = ((6 * roll) + roll) / 2
print("The Mean is ", Mean)
poss = 1
math = chance(roll, total, poss)
print("Combo: ", chance(roll, total, poss))
exp1 = pow(6, roll)
percentage = (math / exp1) * 100
print("The probability of getting that sum of", total, "in", roll, "roll is", format(percentage, ".2f"), "%")
