import random 

print("Hello everyone,This is a number gussing game and you have 7 chances to find the number. \n Tip: number is between 0-100")

number_to_guss = random.randrange(100)
chance = 7

guess_counter = 0

while guess_counter < chance:
    guess_counter += 1
    myguss = int(input("Enter your guess: "))

    if myguss == number_to_guss:
        print(f"You guessed it right, the number was {number_to_guss}")
        break

    elif guess_counter >= number_to_guss:
        print(f"Oops sorry,You Lost and the {number_to_guss} is the number")
        break

    elif myguss < number_to_guss:
        print(f"Too low, try again. You have {chance - guess_counter} chances")

    elif myguss > number_to_guss:
        print(f"Too high, try again. You have {chance - guess_counter} chances")
