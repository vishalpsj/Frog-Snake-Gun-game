import random
'''
1 for snake 
-1 for frog
0 for gun
'''
#let the computer select a random number among -1, 0 and 1

computer = random.choice([-1, 0, 1])

print("Let's play Snake, Frog and Gun game!".center(50))
print("Press S for Snake or press F for Frog or press G for Gun")

#Recieving user input
user_input = input("Enter your choice:  ")
user = user_input.lower()

#Creating a dictionary
dictionary = {"s": 1, "f": -1, "g": 0}
revese_dict = {1:"Snake", -1: "Frog", 0:"Gun"}



if user in dictionary:
    player = dictionary[user]
    print(f"You chose: {revese_dict[player]}")
    print(f"Computer chose: {revese_dict[computer]}")

    if computer == player:
        print("It's a draw!!")
        print(f"{revese_dict[computer]} and {revese_dict[player]} said it's okay!")
    elif computer == 1 and player == -1:
        print(f"{revese_dict[computer]} killed {revese_dict[player]}")
        print("You lose!!")
    elif computer == 1 and player == 0:
        print(f"{revese_dict[player]} killed {revese_dict[computer]}")
        print("Hurray...You Win!!")
    elif computer == -1 and player == 0:
        print(f"{revese_dict[player]} killed {revese_dict[computer]}")
        print("Hurray...You Win!!")
    elif computer == -1 and player == 1:
        print(f"{revese_dict[player]} killed {revese_dict[computer]}")
        print("Hurray...You Win!!")
    elif computer == 0 and player == -1:
        print(f"{revese_dict[computer]} killed {revese_dict[player]}")
        print("You lose!!")
    elif computer == 0 and player == 1:
        print(f"{revese_dict[computer]} killed {revese_dict[player]}")
        print("You lose!!")


else:
    print("Something went wrong!! \nThe valid inputs are s, f and g.")