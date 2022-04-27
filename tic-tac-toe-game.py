"""
Tic-Tac_Toe game
Author: Wendy Fellows using code from pencilprogramming.com
Your program must also meet the following requirements.
The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main.
"""
board = ['1','2','3','4','5','6','7','8','9']
empty = [0,1,2,3,4,5,6,7,8]

def main():
    startGame()
    # player = 0
    # while empty and check_win():    
    #     create_board()
    #     player_input(player)
    #     player = int(not player)
    # if not empty:
    #     print("NO WINNER!")

def create_board():
    """Make a tic tac toe board with each field using a number for the players to fill in with x or o
    Parameter: none
    Return nothing
    """    
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_input(player):
    """Function to ask player to enter a number on the board to enter their X or O according to which player they are. Then puts the X or O into the correct spot on the board.
    Parameters: player
    
    """
    player_symbol = ['X','O']
    correct_input = True

    position = int(input('player {playerNo}s turn. Choose spot to fill {symbol}: '.format(playerNo = player +1, symbol = player_symbol[player])))

    if board[position-1] == 'X' or board[position-1] == 'O':
        correct_input = False

    if not correct_input:
        print("Position already equipped")
        player_input(player)
    else:
        empty.remove(position-1)
        board[position-1] = player_symbol[player] 
        return 1

#function checks if any player won
def check_win():
    #define players symbols and winning positions
    player_symbol = ['X','O']
    winning_positions =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    #check all winning positions for matching placements
    for check in winning_positions:
        first_symbol = board[check[0]]
        if first_symbol != ' ':
            won = True
            for point in check:
                if board[point] !=  first_symbol:
                    won = False
                    break
            if won:
                if first_symbol == player_symbol[0]:
                    print('player 1 won')
                else:
                    print('player 2 won')
                break
        else:
            won = False
    if won:
        return 0
    else:
        return 1

def restart():
    user_input = input("Would you like to play again? Type 'Yes' or 'No' ")

    if user_input.lower() == "no": # Converts input to lowercase for comparison
        return False
    elif user_input.lower() == "yes":
        return True

def startGame():
    while True:
        player = 0
        while empty and check_win():    
            create_board()
            player_input(player)
            player = int(not player)
        if not empty:
            print("NO WINNER!")
            if not restart():
                return



if __name__ == "__main__":
    main()