import random
NUM_ROUNDS = 1
point=0

print("""Welcome to the High-Low Game!
--------------------------------""")
while NUM_ROUNDS <= 3:
    print(f"\nRround {NUM_ROUNDS} ")
    computer_number:int =random.randint(1, 100)
    # print(f"The computer number is {computer_number}")

    user_number:int=int(input("Your Number is "))
    user_choice=input("Enter your choice ")
    if user_choice == "loer" and user_number < computer_number:
        point += 1
        print(f"Do you think your number is higher or lower than the computer's?: lower")
        print(f"You were right! The computer's number was {computer_number}")
    elif user_choice == "loer" and user_number > computer_number:
        print(f"Do you think your number is higher or lower than the computer's?: lower")
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    elif user_choice == "higher" and user_number > computer_number:
        point += 1
        print(f"Do you think your number is higher or lower than the computer's?: higher")
        print(f"You were right! The computer's number was {computer_number}")
    elif user_choice == "higher" and user_number < computer_number:
        print(f"Do you think your number is higher or lower than the computer's?: higher")
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    NUM_ROUNDS += 1


if point == NUM_ROUNDS:
    print(f"Your score is now {point}")
    print("Wow! You played perfectly!")
elif point == int(NUM_ROUNDS / 2):
    print(f"Your score is now {point}")
    print("Good job, you played really well!")    
elif point < int(NUM_ROUNDS / 2):
    print(f"Your score is now {point}")
    print("Better luck next time!")

