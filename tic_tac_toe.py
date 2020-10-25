import random
import os

def init_board(): #Skondensowałem
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
   
    print(f"""   1   2   3\nA  {board[0][0]} | {board[0][1]} | {board[0][2]}\n  ---+---+---\nB  {board[1][0]} | {board[1][1]} | {board[1][2]}\n  ---+---+---\nC  {board[2][0]} | {board[2][1]} | {board[2][2]}""")

    return board


def get_move(board, player, avilable_coordinate):
    """Returns the coordinates of a valid move for player on board."""
    coordinates = {"A1":[0, 0], "A2":[0, 1], "A3":[0, 2], "B1":[1, 0], "B2":[1,1], "B3":[1, 2], "C1":[2, 0], "C2":[2, 1], "C3":[2, 2]}
    
    while True:

        print(f"Avilable coordinate: {avilable_coordinate}")
        player_input = input("Please enter the coordinates: ")

        if player_input.upper() == "quit".upper():
            quit()

        elif player_input.upper() in avilable_coordinate:
            user_coordinate = coordinates.get(player_input.upper())
            row = user_coordinate[0]
            col = user_coordinate[1]
            avilable_coordinate.remove(player_input.upper())
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


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col): # Uprościłem tutaj nieco kod. Zostawiam do dyskusji.
    """Marks the element at row & col on the board for player."""
    if "." in board[row][col]:
        board[row][col] = player
    else:
        pass

    # if "." in board[col][row]:
    #     if player == "O":
    #         board[col][row] = "O"
    #     else:
    #         board[col][row] = "X"
    # else:
    #     pass

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

    # win_player_1 = ["X", "X", "X"]
    # win_player_2 = ["O", "O", "O"]

    win_list = [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3], [a1, b1, c1], [a2, b2, c2], [a3, b3, c3], [a1, b2, c3], [a3, b2, c1]]

    win_player = [player, player, player]
    for element in win_list:
        if element == win_player:
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


def tictactoe_game(mode='HUMAN-HUMAN'): # Propozycja kodu dla tej funkcji. W tic_tac_toe2.py fajnie to działa
    os.system("cls || clear") #Dzięki temu fajnie się czyści wyświetlany obraz gry
    board = init_board()
    player = "O" #Skróciłem nieco.
    avilable_coordinate = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    
    while is_full(board) is False and has_won(board, player) is False: #dałem tutaj False, poniewa >0 nie uwzględniało wygranej wcześniej ni wszystkie moliwości są wykorzystane.
        if player == "O": #Przeniosłem to tutaj, bo inaczej program nie działał poprawnie.
            player = "X"
        else:
            player = "O"
        row, col = get_move(board, player, avilable_coordinate)
        os.system("cls || clear")#Dzięki temu widzimy tylko aktualny stan gry
        board = mark(board, player, row, col)
        print_board(board)
    else: #Tutaj będziemy drukować ju wynik końcowy
        if is_full(board):
            print("Let's call it a tie")
        elif has_won(board, player):
            print_result(player)
    
    
    # board = init_board()
    # player_1 = "X"
    # player_2 = "O"
    # player = player_1
    # avilable_coordinate = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    # # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    # print_board(board)
    # # tu powinna być pętla
    # while len(avilable_coordinate) > 0:
    #     row, col = get_move(board, player, avilable_coordinate)
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
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
