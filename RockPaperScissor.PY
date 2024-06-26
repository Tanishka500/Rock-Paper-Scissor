import tkinter as tk
import random

# Define choices
choices = ["Rock", "Paper", "Scissors"]

# Game logic to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You Win!"
    else:
        return "You Lose!"

# Function to update the scores
def update_scores(result):
    global user_score, computer_score
    if result == "You Win!":
        user_score += 1
    elif result == "You Lose!":
        computer_score += 1

# Function to handle the user's choice and play the game
def play_game(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    update_scores(result)
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\nResult: {result}")
    score_label.config(text=f"Your Score: {user_score}  Computer's Score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="", bg="#FFB6C1")
    score_label.config(text=f"Your Score: {user_score}  Computer's Score: {computer_score}", bg="#FFB6C1")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("450x500")
root.config(bg="#FFB6C1")  # Set the background color to baby pink here

# Set fonts for the widgets
title_font = ("Helvetica", 18, "bold")
button_font = ("Helvetica", 14, "bold")
result_font = ("Helvetica", 16, "italic")
score_font = ("Helvetica", 14, "bold")

# Create and place the instruction label
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=title_font, bg="#FFB6C1")
instruction_label.pack(pady=20)

# Create and place the buttons for user choices with their original colors
button_frame = tk.Frame(root, bg="#FFB6C1")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("Rock"), font=button_font, bg="#FFDDC1", activebackground="#FFABAB", width=10)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("Paper"), font=button_font, bg="#C1FFD7", activebackground="#ABFFC4", width=10)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("Scissors"), font=button_font, bg="#D1C1FF", activebackground="#C4ABFF", width=10)
scissors_button.grid(row=0, column=2, padx=10)

# Create and place the result label with bold black text
result_label = tk.Label(root, text="", font=result_font, bg="#FFB6C1", fg="black")
result_label.pack(pady=20)

# Create and place the score label with bold black text
score_label = tk.Label(root, text=f"Your Score: {user_score}  Computer's Score: {computer_score}", font=score_font, bg="#FFB6C1", fg="black")
score_label.pack(pady=20)

# Create and place the reset button with bold black text and medium red background
reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=button_font, bg="#FF6666", activebackground="#FF3333", fg="black", width=15)
reset_button.pack(pady=20)

# Start the main event loop
root.mainloop()
