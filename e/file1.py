import tkinter as tk
import random

def play_round(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"You chose {player_choice}, Computer chose {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")

rock_button = tk.Button(root, text="Rock", command=lambda: play_round("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_round("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_round("scissors"))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()