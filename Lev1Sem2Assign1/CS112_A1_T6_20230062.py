#program: Two-square game : a game where two users enter a numbers representing rectangle on a board and the last one who playes wins the game
#Author : Islam Waleed Salah AbdElMotaleb
#     ID: 20230062
#     SECTION: NO SECTIONS DETERMINED TILL NOW
#version: 6.0
#Date: 28/2/2024
#

#explain the game
print("Welcome to the Two_square_game")



print("the game is as following :")
print("two players take turns to enter two numbers")
print("those numbers represent a rectangle on the shown board")
print("the last player who plays wins the game")
print("have fun!")

"""
main idea is as following :
1. make a 2d array representing the board
2. check if the player has choosen valid input
3. check if a player has won
4. cover the two squares
5. print the board
6. return to number 1  
"""
board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
two_squares = [-1, -1]
def print_board():
    row = ""
    for i in range(4):
        for j in range(4):
            if type(board[i][j]) == int:
                row += str(board[i][j]) + "  " if board[i][j] <= 9 else (str(board[i][j])) + " "
            else:
                row += board[i][j] + " "
        print(row)
        row = ""



def take_input():
    two_squares[0] = input("enter a rectangle: ")
    two_squares[1] = input()

    #note this trick that if it is not numeric the loop will go without checking the rest of the expression, so no errors happen
    while not two_squares[0].isnumeric() or not two_squares[1].isnumeric() or not (0 < int(two_squares[0]) <= 16) or not (0 < int(two_squares[1]) <= 16):
        print("invalid input")
        print("player", player, "it's your turn")
        two_squares[0] = input("enter a rectangle ")
        two_squares[1] = input()
    #should be casted to int so we can use it later
    two_squares[0] = int(two_squares[0])
    two_squares[1] = int(two_squares[1])
    return

#check if the two squares are Contiguous
def valid_rectangle(num1, num2) :

    #make sure we don't use 4 and 5 for example because subtraction is 1 but they can not form a rectangle
    if num1 % 4 == 0 and num1 - num2 == -1:
        return False
    if num2 % 4 == 0 and num2 - num1 == -1:
        return False

    if abs(num1 - num2) == 4 or abs(num1 - num2) == 1 :
        return True
    else: return False


#check if there is no rectangles left on the board
def win_check():

    # this function basically returns the number of rectangles available on the board
    count = 0;
    # check columns
    for i in range(4):
        for j in range(3):
            if isinstance(board[i][j], int) and isinstance(board[i][j + 1], int): return False

    # check rows
    for i in range(3):
        for j in range(4):
            if isinstance(board[i][j], int) and isinstance(board[i + 1][j], int): return False

    return True

"""
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
"""

def cover_squares(num):
    x = num // 4
    if x != 0 and num % 4 == 0:
        x = num // 4 - 1

    y = -1 if num % 4 == 0 else num % 4 - 1

    if board[x][y] == 'X ':
        return False

    if num <= 9:
        board[x][y] = 'X '
    else:
        board[x][y] = 'X '

    return True




#main proccessing
while True:
    query = input("Enter a choice: \nA:Enter the game\nB:Exit\n").upper()
    if query == 'A':

        #declerations
        board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        player = 1
        two_squares = [-1, -1]

        while True:
            print_board()
            print("player,", player, "it's your turn.")

            take_input()

            #make sure if the given two numbers can form a rectangle
            while not valid_rectangle(two_squares[0], two_squares[1]):
                print("can not form a rectangle")
                take_input()

            #to cover the first square with x and make sure the square is not already taken at the same time
            while not cover_squares(two_squares[0]) :
                print("already taken")
                take_input()

            #to cover the second square
            while not cover_squares(two_squares[1]):
                print("already taken")
                take_input()

            if win_check():
                print("player ", player, "has won!")
                break

            if player == 1:
                player = 2
            else:
                player = 1

    elif query == 'B':
        exit()
    else:
        print("invalid input")