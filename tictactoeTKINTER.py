from tkinter import *
from tkinter import messagebox

player1 = 'X'
playing = True
winner = None

def clicked(r,c):
    global player1, winner
    if playing == True and board[r][c]['text']==' ':
        if player1 == 'X':
            board[r][c].config(text='X')
            player1 =  'O'
        else:
            board[r][c].config(text='O')
            player1 =  'X'

    check_winner(board)

def check_winner(board):
    global winner
    global playing

    for i in range(3):

        #for rows
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != ' ':
            playing = False
            winner = messagebox.showinfo("Winner ", board[i][0]['text'] + " Won!!!")
            break

        #for columns
        elif board[0][i]['text'] == board[1][i]['text'] == board[2][i]['text'] != ' ':
            playing = False
            winner =  messagebox.showinfo("Winner ", board[0][i]['text'] + " Won!!!")
            # disableAllButton()
            break

    #for diagonal
    if board[0][0]['text'] == board[1][1]['text'] == board [2][2]['text'] != ' ':
        playing = False
        winner =  messagebox.showinfo("Winner ", board[0][0]['text'] + " Won!!!")


    elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != ' ':
        playing = False
        winner =  messagebox.showinfo("Winner", board[2][0]['text'] + " Won")


    if is_full(board):
        playing = False
        winner =  messagebox.showinfo("tie", "Tie")

def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]['text'] == ' ':
                return False
    return True

def reset_game():
    global player1, playing, winner
    player1 = 'X'
    playing = True
    winner = None
    for i in range(3):
        for j in range(3):
            board[i][j].config(text=' ')

root = Tk()
root.title("Tic Tac Toe")
root.resizable(0,0)

title_label = Label(root, text = "Tic Tac Toe", font=("Helvetica", 24))
title_label.grid(row=0, column=1)

board = [[' ', ' ', ' ' ],[ ' ', ' ', ' '],[' ', ' ', ' ']]

for i in range(3):
    for j in range(3):
        board[i][j] = Button(root, text=' ', height=4, width=8, font=('Helvetica', 20), command=lambda r=i, c=j: clicked(r,c))
        board[i][j].grid(row=i+2, column=j)

reset_b = Button(root, text="Reset The Game", command=reset_game)
reset_b.grid(row=5, column=1)

root.mainloop()