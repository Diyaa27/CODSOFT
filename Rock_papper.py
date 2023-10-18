import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices
choices = ["rock", "paper", "scissors"]

# Function to play the game
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    # Display computer's choice
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    
    # Display the result
    result_label.config(text=f"Result: {result}")
    user_score_label.config(text=f"User Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Frame to center the buttons horizontally
center_frame = tk.Frame(window)
center_frame.pack()

# User's choices
rock_button = tk.Button(center_frame, text="Rock", width=10, height=3, command=lambda: play_game("rock"))
paper_button = tk.Button(center_frame, text="Paper", width=10, height=3, command=lambda: play_game("paper"))
scissors_button = tk.Button(center_frame, text="Scissors", width=10, height=3, command=lambda: play_game("scissors"))

rock_button.pack(side="left")
paper_button.pack(side="left")
scissors_button.pack(side="left")

# Result and score labels
computer_choice_label = tk.Label(window, text="Computer chose: ")
result_label = tk.Label(window, text="Result: ")
user_score_label = tk.Label(window, text="User Score: ")
computer_score_label = tk.Label(window, text="Computer Score: ")

computer_choice_label.pack()
result_label.pack()
user_score_label.pack()
computer_score_label.pack()

# Run the GUI application
window.mainloop()
