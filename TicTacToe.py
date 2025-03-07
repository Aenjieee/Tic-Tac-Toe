from tkinter import *
from tkinter import messagebox
import random

def with_player(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player

        # Set background color based on the player's turn
        color = "lightblue" if player == "O" else "lightcoral"
        buttons[row][column]['bg'] = color

        if len([button['text'] for row in buttons for button in row if button['text'] != ""]) >= 3:
            if check_winner():
                messagebox.showinfo("Game Over", f"Player {player} wins!")
                new_game()
                return

        if not empty_spaces():
            messagebox.showinfo("Game Over", "It's a Tie!")
            new_game()
        else:
            player = players[1] if player == players[0] else players[0]
            update_turn_label()

def update_turn_label():
    turn_label.config(text=f"Turn: {player}")

def empty_spaces():
    return any(buttons[row][column]['text'] == "" for row in range(3) for column in range(3))

def check_winner():
    for line in [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]:
        if all(buttons[row][column]['text'] == player for row, column in line) and buttons[line[0][0]][line[0][1]]['text'] != "":
            return True

    for x in range(3):
        if all(buttons[x][o]['text'] == player for o in range(3)) or all(
                buttons[o][x]['text'] == player for o in range(3)):
            return True

    return False

def new_game():
    global player
    player = random.choice(players)

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="SystemButtonFace")

    update_turn_label()

def set_custom_cursor():
    if player == "X":
        window.config(cursor="plus")
    else:
        window.config(cursor="hand2")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def confirm_exit():
    result = messagebox.askquestion("Confirm Exit", "Are you sure you want to exit?")
    if result == 'yes':
        window.destroy()


window = Tk()
window.title("Tic-Tac-Toe")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")  # Adjust the dimensions as needed
window.resizable(True, True)  # Allow window resizing
window.protocol("WM_DELETE_WINDOW", confirm_exit)  # Confirm exit on close

# Set up players and initial player
players = ["X", "O"]
player = random.choice(players)

# Header Label
label = Label(window, text="Tic-Tac-Toe", font=('Arial', 36, 'bold'), background="#ADD8E6")  # Light Blue
label.pack(pady=20)

# Game Board Frame
game_frame = Frame(window, background="#B0E57C")  # Light Green
game_frame.pack(pady=20)

# Buttons
buttons = [[0, 0, 0] for _ in range(3)]

for x in range(3):
    for o in range(3):
        buttons[x][o] = Button(game_frame, text="", font=('Arial', 20, 'bold'),
                               command=lambda x=x, o=o: with_player(x, o), bg="SystemButtonFace", cursor="hand2")
        buttons[x][o].grid(row=x, column=o, padx=10, pady=10, ipadx=40, ipady=30)

# Turn Label
turn_label = Label(window, text=f"Turn: {player}", font=('Arial', 24), background="#ADD8E6")  # Light Blue
turn_label.pack(pady=20)

# Control Buttons
control_frame = Frame(window, background="#ADD8E6")  # Light Blue
control_frame.pack(pady=20)

restart_button = Button(control_frame, text="Restart", command=new_game, font=('Arial', 16))
restart_button.grid(row=0, column=0, padx=10, pady=10)

exit_button = Button(control_frame, text="Exit", command=confirm_exit, font=('Arial', 16))
exit_button.grid(row=0, column=1, padx=10, pady=10)

# Center the window
center_window(window)

# Set custom cursor
set_custom_cursor()

window.mainloop()
#Updated
