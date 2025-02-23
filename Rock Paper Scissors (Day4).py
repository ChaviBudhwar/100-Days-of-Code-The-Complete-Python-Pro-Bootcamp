import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

comp_options = [rock, paper, scissors]
comp_choice = random.choice(comp_options)

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if choice == "0":
    print(f"Your choice: {rock}")
elif choice == "1":
    print(f"Your choice: {paper}")
else:
    print(f"Your choice: {scissors}")

print(f"Computer's choice: {comp_choice}")

if comp_choice == rock and choice == "0":
    print("It's a draw!")
elif comp_choice == rock and choice == "2":
    print("You lost...")
elif comp_choice == rock and choice == "1":
    print("You Win!!")

elif comp_choice == paper and choice == "1":
    print("It's a draw!")
elif comp_choice == paper and choice == "0":
    print("You lost...")
elif comp_choice == paper and choice == "2":
    print("You Win!")

elif comp_choice == scissors and choice == "2":
    print("It's a draw!")
elif comp_choice == scissors and choice == "1":
    print("You lost...")
elif comp_choice == scissors and choice == "0":
    print("You Win!")
