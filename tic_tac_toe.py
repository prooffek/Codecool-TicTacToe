import random
import os
from termcolor import colored  
import time

def init_board(): 
    """Returns an empty 3-by-3 board (with .)."""

    return [[".", ".", "."], [".", ".", "."], [".", ".", "."]]


def get_move(board, player, available_coordinate, coordinates):
    """Returns the coordinates of a valid move for player on board."""
    
    while True:

        print(f"Avilable coordinate: {available_coordinate}")
        player_input = input("Please enter the coordinates: ")

        if player_input.upper() == "QUIT":
            quit()

        elif player_input.upper() in available_coordinate:
            user_coordinate = coordinates.get(player_input.upper())
            row = user_coordinate[0]
            col = user_coordinate[1]
            available_coordinate.remove(player_input.upper())
            return row, col
            """myślę nad wyrzuceniem tej części zakomentowanej, bo wydaje mi się to trochę bez sensu, 
            ta lista z dostępnymi koordynatami nie daje możliwości wprowadzenia niczego innego 
            (znacząco byśmy uprościli tą funkcję)"""
        
        # elif player_input[0].upper() not in ["A", "B", "C"] and player_input[1] not in ["1", "2", "3"]:
        #     print("Please enter the correct coordinates from the available coordinates:")

        # elif player_input[0].upper() not in ["A", "B", "C"]:
        #     print("Enter the coordinates correctly, they should contain A, B or C") 

        # elif player_input[1] not in ["1", "2", "3"]:
        #     print("Enter the coordinates correctly, they should contain 1, 2 or 3")

        else:
            print("Please enter the correct coordinates from the available coordinates:")
    


def inteligent_AI(board, player): #Komputer blokuje ewentualne wygrane gracza
    for i in range(3):
        row_check = board[i]
        col_check = [board[0][i], board[1][i], board[2][i]]
        diag_check_1 = [board[0][0], board[1][1], board[2][2]]
        diag_check_2 = [board[2][0], board[1][1], board[0][2]]
        diag_row_index = {0 : 2, 1 : 1, 2 : 0}
        
        value = False
        if row_check.count(player) == 2 and "." in row_check:
            row = i
            col = row_check.index(".")
            value = True
            break
        elif col_check.count(player) == 2 and "." in col_check:
            row = col_check.index(".")
            col = i
            value = True
            break
        elif diag_check_1.count(player) == 2 and "." in diag_check_1:
            row = diag_check_1.index(".")
            col = row
            value = True
            break
        elif diag_check_2.count(player) == 2 and "." in diag_check_2:
            col = diag_check_2.index(".")
            row = diag_row_index[col]
            value = True
            break

    if value is True:
        return row, col
    else:
        return value

def get_ai_move(available_coordinate, player, board, coordinates): #komputer sprawdza, czy istnieje zagroenie wygranej gracza, a jeśli takowego nie ma to losuje współrzędne.
    """Returns the coordinates of a valid move for player on board."""
    
    AI_choice = inteligent_AI(board, player)
    if AI_choice is not False:
        row, col = AI_choice
        dict_key = [key for (key, value) in coordinates.items() if value == AI_choice]
    else:
        computer_choice = available_coordinate[random.randint(0, len(available_coordinate) - 1)]
        dict_key = [computer_choice]
        row, col = coordinates[computer_choice]

    available_coordinate.remove(dict_key[0])

    return row, col


def mark(board, player, row, col): 
    """Marks the element at row & col on the board for player."""
    
    if "." in board[row][col] and player == "X":
        board[row][col] = colored(player, "red")
    elif "." in board[row][col] and player == "O":
        board[row][col] = colored(player, "yellow")
    else:
        pass

    return board


def has_won(board, player): 
    """Returns True if player has won the game."""
    a1 = board[0][0]
    a2 = board[0][1]
    a3 = board[0][2]
    b1 = board[1][0]
    b2 = board[1][1]
    b3 = board[1][2]
    c1 = board[2][0]
    c2 = board[2][1]
    c3 = board[2][2]

    colored_player_1 = colored("X", "red")
    colored_player_2 = colored("O", "yellow")
    win_player_1 = [colored_player_1, colored_player_1, colored_player_1]
    win_player_2 = [colored_player_2, colored_player_2, colored_player_2]

    win_list = [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3], [a1, b1, c1], [a2, b2, c2], [a3, b3, c3], [a1, b2, c3], [a3, b2, c1]]

    
    for element in win_list:
        if element == win_player_1 or element == win_player_2:
            return True
    else:
        return False



def is_full(board):  
    """Returns True if board is full."""
    value = True
    for i in board:
        if "." in i:
            value = False
    return value


def print_board(board):

    print(f"""   1   2   3\nA  {board[0][0]} | {board[0][1]} | {board[0][2]}\n  ---+---+---\nB  {board[1][0]} | {board[1][1]} | {board[1][2]}\n  ---+---+---\nC  {board[2][0]} | {board[2][1]} | {board[2][2]}""")


def print_result(winner):    
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "X":
        print("Congratulations, player X win!")
    elif winner == "O":
        print("Congratulations,player O win!")
    

def quit():
    exit()


def tictactoe_game(mode): 
    os.system("cls || clear") 
    available_coordinate = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    coordinates = {"A1":[0, 0], "A2":[0, 1], "A3":[0, 2], "B1":[1, 0], "B2":[1,1], "B3":[1, 2], "C1":[2, 0], "C2":[2, 1], "C3":[2, 2]}
    board = init_board()
    print_board(board)
    player_1 = "X"
    player_2 = "O"
    player = player_2
    full_board = is_full(board)
    winner = has_won(board, player)

    while full_board is False and winner is False:
        if player == player_2:
            player = player_1
        else:
            player = player_2

        print(f"Now player {player} move")

        if mode == "HUMAN-HUMAN":
            row, col = get_move(board, player, available_coordinate, coordinates)
        elif mode == "HUMAN-COMPUTER":
            if player == player_1:
                row, col = get_move(board, player, available_coordinate, coordinates)
            else:
                row, col = get_ai_move(available_coordinate, player, board, coordinates)
        elif mode == "COMPUTER-COMPUTER":
            row, col = get_ai_move(available_coordinate, player, board, coordinates)
            
        os.system("cls || clear")
        board = mark(board, player, row, col)
        print_board(board)
        time.sleep(1)
        winner = has_won(board, player)
        full_board = is_full(board)

    if full_board and winner == False:
        print("Let's call it a tie")
        quit()
    elif winner:
        print_result(player)
        quit()

def main_menu():
    print("""
                    Welcome in the game
                 _______    ______        ______        
                /_  __(_)__/_  __/__ ____/_  __/__  ___ 
                 / / / / __// / / _ `/ __// / / _ \/ -_)
                /_/ /_/\__//_/  \_,_/\__//_/  \___/\__/ 

                Press 1 to play in HUMAN - HUMAN mode
                Press 2 to play in HUMAN - COMPUTER mode
                Press 3 to play in COMPUTER - COMPUTER mode
                Enter quit to exit the game

    """)
    input_user = input()
    if input_user == str(1):
        tictactoe_game("HUMAN-HUMAN")
    elif input_user == str(2):
        tictactoe_game("HUMAN-COMPUTER")
    elif input_user == str(3):
        tictactoe_game("COMPUTER-COMPUTER")
    elif input_user == "quit":
        quit()
    else:
        print("Starting the default game mode HUMAN-COMPUTER")  
        tictactoe_game("HUMAN-COMPUTER")
    


if __name__ == '__main__':
    main_menu()

