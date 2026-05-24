# ================== All-in-One Mini Games ==================

from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title(" All-in-One Mini Games")
root.geometry("400x450")
root.config(bg="lightgrey")

# ================== SNAKE & LADDER ==================
def snake_ladder_game():
    win = Toplevel(root)
    win.title("Snake & Ladder")
    win.geometry("400x400")
    win.config(bg="lightyellow")

    Label(win, text=" Snake & Ladder ", font=("Times New Roman", 18, "bold"), bg="lightyellow").pack(pady=10)

    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    players = [0, 0]
    turn = [0]

    lbl_pos = Label(win, text="Player 1 = 0 | Player 2 = 0", font=("Times New Roman", 14), bg="lightyellow")
    lbl_pos.pack(pady=10)
    
    lbl_msg = Label(win, text="", font=("Times New Roman", 12), bg="lightyellow")
    lbl_msg.pack(pady=10)

    def roll_dice():
        dice = random.randint(1, 6)
        i = turn[0]
        players[i] += dice

        if players[i] > 100:
            players[i] -= dice
            lbl_msg.config(text="Need exact number to reach 100!")
        elif players[i] in snakes:
            players[i] = snakes[players[i]]
            lbl_msg.config(text=f"Snake bite! Go to {players[i]}")
        elif players[i] in ladders:
            players[i] = ladders[players[i]]
            lbl_msg.config(text=f"Ladder! Climb to {players[i]}")
        else:
            lbl_msg.config(text=f" You rolled {dice}, now at {players[i]}")

        lbl_pos.config(text=f"Player 1 = {players[0]} | Player 2 = {players[1]}")

        if players[i] == 100:
            messagebox.showinfo("Winner", f" Player {i+1} wins!")
            win.destroy()
            return

        turn[0] = 1 - turn[0]

    Button(win, text="Roll Dice", font=("Times New Roman", 14), bg="lightblue", command=roll_dice).pack(pady=15)
    Button(win, text="Back to Menu", bg="lightyellow", command=win.destroy).pack(pady=10)


# ================== TIC TAC TOE ==================
def tic_tac_toe_game():
    win = Toplevel(root)
    win.title("Tic Tac Toe")
    win.geometry("350x400")
    win.config(bg="lightblue")

    Label(win, text="❌ Tic Tac Toe ⭕", font=("Times New Roman", 18, "bold"), bg="lightblue").pack(pady=10)

    player = ["X"]
    board = [["" for _ in range(3)] for _ in range(3)]

    def check_winner():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return True
            if board[0][i] == board[1][i] == board[2][i] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
            return True
        return False

    def press(r, c):
        if buttons[r][c]["text"] == "":
            buttons[r][c]["text"] = player[0]
            board[r][c] = player[0]
            if check_winner():
                messagebox.showinfo("Game Over", f" Player {player[0]} wins!")
                win.destroy()
                return
            elif all(board[i][j] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a draw!")
                win.destroy()
                return
            player[0] = "O" if player[0] == "X" else "X"

    frame = Frame(win, bg="lightblue")
    frame.pack()

    buttons = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            b = Button(frame, text="", width=6, height=3, font=("Arial", 20, "bold"),
                       command=lambda r=i, c=j: press(r, c))
            b.grid(row=i, column=j, padx=5, pady=5)
            buttons[i][j] = b

    Button(win, text="Back to Menu", bg="lightyellow", command=win.destroy).pack(pady=10)


# ================== ROCK PAPER SCISSORS ==================
def rock_paper_scissors_game():
    win = Toplevel(root)
    win.title("Rock Paper Scissors")
    win.geometry("350x300")
    win.config(bg="lightyellow")

    Label(win, text="Rock Paper Scissors", font=("Times New Roman", 16, "bold"), bg="lightyellow").pack(pady=10)

    result = StringVar()

    def play(user_choice):
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        if user_choice == comp_choice:
            result.set(f"Computer chose {comp_choice}. It's a Draw!")
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result.set(f"Computer chose {comp_choice}. You Win! ")
        else:
            result.set(f"Computer chose {comp_choice}. You Lose!")

    frame = Frame(win, bg="lightyellow")
    frame.pack(pady=20)

    Button(frame, text=" Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
    Button(frame, text=" Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
    Button(frame, text=" Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

    Label(win, textvariable=result, font=("Times New Roman", 13), bg="lightgreen").pack(pady=15)
    Button(win, text="Back to Menu", bg="lightgreen", command=win.destroy).pack(pady=10)


# ================== TREASURE HUNT ==================
def treasure_hunt_game():
    win = Toplevel(root)
    win.title("Treasure Hunt")
    win.geometry("350x350")
    win.config(bg="white")

    Label(win, text="Treasure Hunt ", font=("Times New Roman", 18, "bold"), bg="white").pack(pady=10)
    Label(win, text="Enter X and Y between 0–4", font=("Times New Roman", 12),bg="white").pack(pady=5)

    treasure_x = random.randint(0, 4)
    treasure_y = random.randint(0, 4)
    attempts = [5]

    x_entry = Entry(win, width=5)
    y_entry = Entry(win, width=5)
    x_entry.pack(pady=5)
    y_entry.pack(pady=5)

    msg = Label(win, text="", font=("Times New Roman", 12), bg="white")
    msg.pack(pady=10)

    def check():
        if not x_entry.get().isdigit() or not y_entry.get().isdigit():
            msg.config(text=" Enter numbers only!")
            return
        x = int(x_entry.get())
        y = int(y_entry.get())

        if x == treasure_x and y == treasure_y:
            messagebox.showinfo("Congratulations!", " You found the treasure!")
            win.destroy()
        else:
            attempts[0] -= 1
            if attempts[0] == 0:
                messagebox.showinfo("Game Over", f" Out of attempts! Treasure was at ({treasure_x},{treasure_y})")
                win.destroy()
            else:
                msg.config(text=f"Wrong! Attempts left: {attempts[0]}")

    Button(win, text="Check", bg="lightgreen", command=check).pack(pady=10)
    Button(win, text="Back to Menu", bg="lightcoral", command=win.destroy).pack(pady=10)


# ================== MAIN MENU ==================
Label(root, text=" All-in-One Mini Games ", font=("Times New Roman", 25, "bold"), bg="beige").pack(pady=20)

Button(root, text="1 Snake & Ladder", width=25, height=2, bg="beige",font=("Times New Roman", 12,"bold"), command=snake_ladder_game).pack(pady=8)
Button(root, text="2 Tic Tac Toe", width=25, height=2, bg="lightblue",font=("Times New Roman", 12,"bold"), command=tic_tac_toe_game).pack(pady=8)
Button(root, text="3 Rock Paper Scissors", width=25, height=2, bg="lightyellow",font=("Times New Roman", 12,"bold"), command=rock_paper_scissors_game).pack(pady=8)
Button(root, text="4 Treasure Hunt", width=25, height=2, bg="lightgreen",font=("Times New Roman", 12,"bold"), command=treasure_hunt_game).pack(pady=8)
Button(root, text="Exit", width=25, height=2, bg="lightcoral",font=("Times New Roman", 12,"bold"), command=root.destroy).pack(pady=25)

root.mainloop()