# Girls Tic Tac Toe

# Load tkinter, random, and pygame (for sound)
from tkinter import *
import random
import pygame


# Initialize pygame mixer
pygame.mixer.init()

# Load the sound files (Change the path here to where you downloaded the files)
play_drum = pygame.mixer.Sound("xxx/Snare Drum Hit 01.wav")
play_bongo = pygame.mixer.Sound("xxx/Low Tom Hit 01.wav")
play_sheep = pygame.mixer.Sound("xxx/pp.wav")
play_bell = pygame.mixer.Sound("xxx/bgg.wav")

# Function to start new game
def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " Turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#FF69B4", state=NORMAL)

# Function to create the next turn
def next_turn(row, column):
    global player

    # Check if the selected cell is empty and the game is not over
    if buttons[row][column]["text"] == "" and check_winner() is False:
        buttons[row][column]["text"] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " Turn")
            
            # Play the corresponding sound based on the player's turn
            if player == "X":
                play_drum.play()
            elif player == "O":
                play_bongo.play()

        elif check_winner() is True:
            label.config(text=player + " Wins")
            play_bell.play()

        elif check_winner() == "Tie":
            label.config(text="Tie!")
            play_sheep.play()

# Function to check if there is a winner or a tie
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    elif not empty_spaces():
        return "Tie"
    else:
        return False

# Function to check if there are any empty spaces on the board
def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] == "":
                return True
    return False

# Create the main game window
window = Tk()
window.title("Girls Tic-Tac-Toe")
window.configure(bg="#FF69B4") 
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Create the label for displaying the current player's turn
label = Label(text=player + " Turn", bg= "#FF69B4", font=("impact", 40))
label.pack(side="top")

# Create the button to restart the game
reset_button = Button(text="Restart", font=("comic sans ms", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

# Create the buttons for the game board
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=("comic sans ms", 40), width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# The main loop to run the game
window.mainloop()


