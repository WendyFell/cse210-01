"""
Tic-Tac_Toe game
Author: Wendy Fellows
Your program must also meet the following requirements.
The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main.
"""

def main():
    create_board()
# What functions do I need:
# Function to replace a number with an x or an o
# Function to make the board
# Function to check if win or draw

def create_board():

    board = ['1','2','3','4','5','6','7','8','9']
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")



if __name__ == "__main__":
    main()