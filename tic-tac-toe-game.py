"""
Tic-Tac_Toe game
Author: Wendy Fellows with a little help from pencilprogramming.com
"""

def main():
    print()
    print("Let's play Tic-Tac-Toe!")
   
    playgame = True
    while playgame == True:
        board = ['1','2','3','4','5','6','7','8','9']
        empty = [0,1,2,3,4,5,6,7,8]
        player = 0
        
        while empty and check_win(board):    
            create_board(board)
            player_input(player, board, empty)
            player = int(not player)
        if not empty:
            print("NO WINNER!")

        yes_no = play_again()
        
        if yes_no == "no":
            playgame = False
            print("Thank you for playing today!")
            break
 
def create_board(board):
    """Make a tic tac toe board with each field using a number for the players to fill in with x or o
    Parameter: none
    Return nothing
    """
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def player_input(player, board, empty):
    """Function to ask player to enter a number on the board to enter their X or O according to which player they are. Then puts the X or O into the correct spot on the board.
    Parameters: player
    
    """
    player_symbol = ['X','O']
    correct_input = True

    print()
    position = int(input("player {playerNo}'s turn. Choose a numbered spot to fill an {symbol}: ".format(playerNo = player +1, symbol = player_symbol[player])))

    if board[position-1] == 'X' or board[position-1] == 'O':
        correct_input = False

    if not correct_input:
        print()
        print("That spot has been used, try again.")
        print()
        player_input(player)
    else:
        empty.remove(position-1)
        board[position-1] = player_symbol[player] 
        return 1


def check_win(board):
    """Looks through board to see if any matching X's or O's are in a certain winning pattern.
    Parameters: none

    """
    # Define players symbols and winning positions
    player_symbol = ['X','O']
    winning_positions =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    # Check all winning positions for matching placements
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
                    create_board(board)
                    print("Player 1 is the Winner!")
                    print()
                   
                else:
                    create_board(board)
                    print("Player 2 is the Winner!")
                    print()
                break
        else:
            won = False
    if won:
        return 0
    else:
        return 1


def play_again():
    """Function to ask if players would like to play again.
    """
    user_input = input("Would you like to play again? Type 'yes' or 'no': ")
    print()
    return user_input.lower


if __name__ == "__main__":
    main()