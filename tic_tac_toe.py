import random
import os
from termcolor import colored  # do kolorowania 
import time

def init_board(): #Skondensowałem
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    
    print_board(board)
    # print(f"""   1   2   3\nA  {board[0][0]} | {board[0][1]} | {board[0][2]}\n  ---+---+---\nB  {board[1][0]} | {board[1][1]} | {board[1][2]}\n  ---+---+---\nC  {board[2][0]} | {board[2][1]} | {board[2][2]}""")

    return board


def get_move(board, player, available_coordinate, coordinates):
    """Returns the coordinates of a valid move for player on board."""
    
    
    while True:

        print(f"Avilable coordinate: {available_coordinate}")
        player_input = input("Please enter the coordinates: ")

        if player_input.upper() == "quit".upper():
            quit()

        elif player_input.upper() in available_coordinate:
            user_coordinate = coordinates.get(player_input.upper())
            row = user_coordinate[0]
            col = user_coordinate[1]
            available_coordinate.remove(player_input.upper())
            return row, col

        elif player_input[0].upper() not in ["A", "B", "C"] and player_input[1] not in ["1", "2", "3"]:
            print("Please enter the correct coordinates from the available coordinates:")

        elif player_input[0].upper() not in ["A", "B", "C"]:
            print("Enter the coordinates correctly, they should contain A, B or C") 

        elif player_input[1] not in ["1", "2", "3"]:
            print("Enter the coordinates correctly, they should contain 1, 2 or 3")

        else:
            print("Please enter the correct coordinates from the available coordinates:")
    return row, col


def inteligent_AI(board): #Komputer blokuje ewentualne wygrane gracza
    for i in range(3):
        row_check = board[i]
        col_check = [board[0][i], board[1][i], board[2][i]]
        diag_check_1 = [board[0][0], board[1][1], board[2][2]]
        diag_check_2 = [board[2][0], board[1][1], board[0][2]]
        diag_row_index = {0 : 2, 1 : 1, 2 : 0}
        value = False
        if row_check.count("X") == 2 and "." in row_check:
            row = i
            col = row_check.index(".")
            value = True
            break
        elif col_check.count("X") == 2 and "." in col_check:
            row = col_check.index(".")
            col = i
            value = True
            break
        elif diag_check_1.count("X") == 2 and "." in diag_check_1:
            row = diag_check_1.index(".")
            col = row
            value = True
            break
        elif diag_check_2.count("X") == 2 and "." in diag_check_2:
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
    
    AI_choice = inteligent_AI(board)
    if AI_choice is not False:
        row, col = AI_choice
        dict_key = [key for (key, value) in coordinates.items() if value == AI_choice]
        del available_coordinate[dict_key]
    else:
        computer_choice = available_coordinate[random.randint(0, len(available_coordinate) - 1)]
        available_coordinate.remove(computer_choice)
        row, col = coordinates[computer_choice]

    return row, col


def mark(board, player, row, col): # Uprościłem tutaj nieco kod. Zostawiam do dyskusji.
    """Marks the element at row & col on the board for player."""
    
    if "." in board[row][col] and player == "X":
        board[row][col] = colored(player, "red")
    elif "." in board[row][col] and player == "O":
        board[row][col] = colored(player, "yellow")
    else:
        pass

   

    return board


def has_won(board, player): #Propozycja uproszczenia w oparciu o tym co mówiłać na Discordzie. Wcześniejszą wersję dałem w komentarzy, bo z jakiegoś powodu wówczas nie działa właściwie i nie mogę znaleźć przyczyny.
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

    #win_player = [player, player, player]
    for element in win_list:
        if element == win_player_1 or element == win_player_2:
            return True
    else:
        return False

    # for element in win_list:
    #     if element == win_player_1:
    #         print("Player X win")
    #         return True
    #     elif element == win_player_2:
    #         print("Player O win")
    #         return True
    #     else:
    #         return False


def is_full(board):  #To zmieniłem całkowicie bo nie działało tak jak powinno
    """Returns True if board is full."""
    value = True
    for i in board:
        if "." in i:
            value = False
        else:
            continue
    return value


def print_board(board):

    print(f"""   1   2   3\nA  {board[0][0]} | {board[0][1]} | {board[0][2]}\n  ---+---+---\nB  {board[1][0]} | {board[1][1]} | {board[1][2]}\n  ---+---+---\nC  {board[2][0]} | {board[2][1]} | {board[2][2]}""")


def print_result(winner):     #Skróciłem kod i naprawiłem kilka błędów.
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "X":
        print("Congratulations, player X win!")
    elif winner == "O":
        print("Congratulations,player O win!")
    

def quit():
    exit()


def tictactoe_game(mode): # Propozycja kodu dla tej funkcji. W tic_tac_toe2.py fajnie to działa
    os.system("cls || clear") #Dzięki temu fajnie się czyści wyświetlany obraz gry
    available_coordinate = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    coordinates = {"A1":[0, 0], "A2":[0, 1], "A3":[0, 2], "B1":[1, 0], "B2":[1,1], "B3":[1, 2], "C1":[2, 0], "C2":[2, 1], "C3":[2, 2]}
    board = init_board()
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

        if mode == "HUMAN-HUMAN":
            row, col = get_move(board, player, available_coordinate, coordinates)
        elif mode == "HUMAN-COMPUTER":
            if player == player_1:
                row, col = get_move(board, player, available_coordinate, coordinates)
            else:
                row, col = get_ai_move(available_coordinate, player, board, coordinates)
        elif mode == "COMPUTER-COMPUTER":
            row, col = get_ai_move(available_coordinate, player, board, coordinates)
            

        os.system("cls || clear")#Dzięki temu widzimy tylko aktualny stan gry
        
        board = mark(board, player, row, col)
        print_board(board)
        time.sleep(3)
        full_board = is_full(board)
        winner = has_won(board, player)


    # if mode == "HUMAN-HUMAN":
    #     while full_board is False and winner is False: #dałem tutaj False, poniewa >0 nie uwzględniało wygranej wcześniej ni wszystkie moliwości są wykorzystane.
    #         if player == player_2: #Przeniosłem to tutaj, bo inaczej program nie działał poprawnie.
    #             player = player_1
    #         else:
    #             player = player_2
    #         row, col = get_move(board, player, available_coordinate, coordinates)
    #         os.system("cls || clear")#Dzięki temu widzimy tylko aktualny stan gry
    #         board = mark(board, player, row, col)
    #         print_board(board)
    #         full_board = is_full(board)
    #         winner = has_won(board, player)

    # elif mode == "HUMAN-COMPUTER":    
    #     while full_board is False and winner is False: #dałem tutaj False, poniewa >0 nie uwzględniało wygranej wcześniej ni wszystkie moliwości są wykorzystane.
    #         if player == player_2: #Przeniosłem to tutaj, bo inaczej program nie działał poprawnie.
    #             player = player_1
    #             row, col = get_move(board, player, available_coordinate, coordinates)
    #         else:
    #             player = player_2
    #             row, col = get_ai_move(available_coordinate, player, board, coordinates)
    #         os.system("cls || clear")#Dzięki temu widzimy tylko aktualny stan gry
    #         board = mark(board, player, row, col)
    #         print_board(board)
    #         full_board = is_full(board)
    #         winner = has_won(board, player)

    if full_board:
        print("Let's call it a tie")
        quit()
    elif winner:
        print_result(player)
        quit()

    # board = init_board()
    # player_1 = "X"
    # player_2 = "O"
    # player = player_1
    # available_coordinate = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    # # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    # print_board(board)
    # # tu powinna być pętla
    # while len(available_coordinate) > 0:
    #     row, col = get_move(board, player, available_coordinate)
    #     print(row)  # do testowania
    #     print (col) # do testowania
    #     mark(board, player, row, col)
    #     print(board)
    #     # gdzieś powinniśmy uwzględnić zmianę gracza, na teraz wydaje mi się to poprawnym miejscem, zaraz po zaznaczeniu na tablicy 
    #     if player == player_1:
    #         player = player_2
    #     else: 
    #         player = player_1


    # winner = 0
    # print_result(winner)




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
        print("Starting the default game mode HUMAN - HUMAN")  # żeby uniknąć pętli while, ale można w sumie ją dodać, można nawet jakoś to połączyć z tym żeby można było ponownie zagrać 
        tictactoe_game("HUMAN-HUMAN")
    


if __name__ == '__main__':
    main_menu()

