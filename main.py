import json
import random
import os


class Clr:
    PP = '\033[95m'
    CN = '\033[96m'
    DC = '\033[36m'
    BL = '\033[94m'
    GR = '\033[92m'
    GR2 = '\033[34m'
    YW = '\033[93m'
    RD = '\033[91m'
    BD = '\033[1m'
    UL = '\033[4m'
    END = '\033[0m'
    WH = '\033[97m'

    def colorAlAzar(self):
        index = random.randint(0, 10)
        colorList = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[91m', '\033[92m',
                       '\033[93m', '\033[94m', '\033[95m', '\033[96m', ]
        return print(colorList[index], end="")


matrix_name = list()
matrix_board = list()

def Verification(file):
    try:
        with open(file, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def BetweenOneNine(value):
    number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    correct = False
    if value in number_list:
        correct = True
    return correct

def EmptySpace(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == "0":
                return i, j
    return False

def Validation(sudoku, num, row, col):
    for i in range(9):
        if sudoku[row][i] == num and col != i:
            return False
        if sudoku[i][col] == num and row != i:
            return False
    space_x = col // 3
    space_y = row // 3
    for i in range(space_y*3, space_y*3 + 3):
        for j in range(space_x * 3, space_x*3 + 3):
            if sudoku[i][j] == num and (i, j) != (row, col):
                return False
    return True

#BackTracking
def Solution(sudoku):
    find = EmptySpace(sudoku)
    if not find:
        return True
    else:
        row, col = find
    number_list=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in number_list:
        if Validation(sudoku, num, row, col):
            sudoku[row][col] = num
            if Solution(sudoku):
                return True
            sudoku[row][col] = "0"
    return False

# JSON
if not Verification("sudoku.json"):
    DBsudoku = open("sudoku.json", "w+")
    dicNuevo = dict()
    json.dump(dicNuevo, DBsudoku)
    DBsudoku.close()

def read():
    global matrix_board, matrix_name
    matrix_name = []
    matrix_board = []
    archi = open("sudoku.json", "r")
    jSud = json.load(archi)
    archi.close()
    jSudNom = jSud.keys()
    jSudTab = jSud.values()
    for i in jSudNom:
        matrix_name.append(i)
    for i in jSudTab:
        matrix_board.append(i)

def IntroduceJSON():
    DICtemp = dict()
    archi = open("sudoku.json", "w")
    for i in range(len(matrix_board)):
        DICtemp[matrix_name[i]] = matrix_board[i]
        if matrix_board[i] == "empty":
            del DICtemp[matrix_name[i]]
    json.dump(DICtemp, archi)
    archi.close()

# Menus
def PrincipalMenu():
    print()
    print(Clr.WH + " - - SUDOKU - - " + Clr.END)
    print(Clr.CN + "                                         " + Clr.END)
    print(Clr.CN + "   " + Clr.END, Clr.YW + "" + Clr.END,
          Clr.BL + Clr.BD + " MENU" + Clr.END + Clr.END, Clr.YW + "           " + Clr.END,
          Clr.CN + f"" + Clr.END)
    print(Clr.CN + "                                         " + Clr.END)
    print(Clr.CN + "   " + Clr.END, Clr.WH + "" + Clr.END,
          Clr.GR2 + Clr.BD + "(1) New Game" + Clr.END + Clr.END, "        ", Clr.CN + "" + Clr.END)
    print(Clr.CN + "   " + Clr.END, Clr.WH + "" + Clr.END,
          Clr.GR2 + Clr.BD + "(2) View/Play saved board" + Clr.END + Clr.END, " ", Clr.CN + "" + Clr.END)
    print(Clr.CN + "   " + Clr.END, Clr.WH + "" + Clr.END, Clr.GR2 + Clr.BD + "(3) End" + Clr.END + Clr.END,
          "                  ", Clr.CN + "" + Clr.END)
    print(Clr.CN + "                                         " + Clr.END)
    print(Clr.DC + " ------------------ " + Clr.END)
    opcion = input()
    return MenuOptions(opcion)


def MenuOptions(opcion):
    if opcion == "1":
        print(Clr.DC + " --------------------" + Clr.END)
        print(Clr.DC + "|" + Clr.END, Clr.BD + Clr.WH + " Difficulty" + Clr.END + Clr.END, end="")
        print(Clr.DC + "    |" + Clr.END)
        print(Clr.DC + "|" + Clr.END, Clr.BD + "(1)", Clr.GR + " Easy" + Clr.END + Clr.END,
              Clr.DC + "|" + Clr.END)
        print(Clr.DC + "|" + Clr.END, Clr.BD + "(2)", Clr.YW + " Medium" + Clr.END + Clr.END,
              Clr.DC + "|" + Clr.END)
        print(Clr.DC + "|" + Clr.END, Clr.BD + "(3)", Clr.RD + " Hard" + Clr.END + Clr.END,
              Clr.DC + "|" + Clr.END)
        print(Clr.DC + " --------------------" + Clr.END)
        difficulty = input()
        sudoku = NewMatrix()
        CompleteSpaces(sudoku)
        Solution(sudoku)
        mode = ["1", "2", "3"]
        if difficulty in mode:
            completezeros(sudoku, difficulty)
        else:
            print("Choose difficulty")
            return MenuOptions(opcion)
        continueBoard(sudoku)
        print()
        print()
        return sudoku

    elif opcion == "2":
        print()
        print("Loading boards...", end="")
        Menu1()

    elif opcion == "3":
        print(Clr.WH + Clr.BD + "- - End Game - -")
        return IntroduceJSON()
    else:
        print("Choose values between 1 & 3\n")
        print()
        return PrincipalMenu()


def Menu1():
    read()
    print()
    print()
    print(Clr.BD + " ____________________" + Clr.END)
    print(Clr.BD + "|" + Clr.END, "\033[03m" + Clr.BD + "\033[93m" + "TABLEROS GUARDADOS" + Clr.END,
          Clr.BD + "|" + Clr.END)
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    c = 0
    for i in matrix_name:
        if matrix_board[c] != "empty":
            Clr().colorAlAzar()
            print("\033[03m" + i + Clr.END)
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        c += 1

    # Comprobar si no hay matrices
    ItIsEmpty = True
    for i in matrix_board:
        if i != "empty":
            ItIsEmpty = False

    if ItIsEmpty:
        print("No game with that name")
        print("• (0) Menu")
        print("• (1) End")
        opcion = input()
        if opcion == "0":
            return PrincipalMenu()
        elif opcion == "1":
            print("- - End Game - -")
            return IntroduceJSON()
        else:
            print("Wrong Option")
            return Menu1()

    else:
        print("Board Details? ")
        print("♦ (1) Yes")
        print("♦ (2) No, Menu")
        opcion = input("")

        if opcion == "1":
            loadGame()

        elif opcion == "2":
            print()
            print("Menu...")
            print()
            print()
            return PrincipalMenu()

        else:
            print("Wrong Option")
            return Menu1()


def Menu2(NameTotal, tab):
    print()
    print("|", "n (1) Loading Game", Clr.CN + "🔻" + Clr.END)
    print("|", "n (2) Erase Game", "\033[31m" + "❌" + Clr.END)
    print("|", "n (3) Saved Games", Clr.BD + "↩" + Clr.END)
    opcion = input("")
    if opcion == "1":
        return continueBoard(tab)
    elif opcion == "2":
        return eraseGame(NameTotal)
    elif opcion == "3":
        print()
        return Menu1()
    else:
        print()
        print("Wrong Option")
        print()
        return Menu2(NameTotal, tab)


def continueBoard(sudoku):
    showBoard(sudoku)
    print()
    print(Clr.YW + "◤--", "                 ", "--◥")
    print(Clr.YW + "|", Clr.WH + "(0) Continue" + Clr.END, "   ", Clr.YW + "|")
    print(Clr.YW + "|", Clr.WH + "(1) Solution" + Clr.END, Clr.YW + "|")
    print(Clr.YW + "|", Clr.WH + "(2) Save Game" + Clr.END, "  ", Clr.YW + "|")
    print(Clr.YW + "|", Clr.WH + "(3) Menu" + Clr.END, "   ", Clr.YW + "|")
    print(Clr.YW + "◣--", "                 ", "--◢")
    opcion = input()
    if opcion == "0":
        return modvalue(sudoku)
    elif opcion == "1":
        if EmptySpace(sudoku):
            Solution(sudoku)
            if EmptySpace(sudoku):
                print("There is not solution")
        else:
            print("It is already solved :)")
        return continueBoard(sudoku)
    elif opcion == "2":
        return saveGame(sudoku)
    elif opcion == "3":
        print()
        print("Menu...")
        print()
        print()
        return PrincipalMenu()
    else:
        print("Choose a value between 1 & 3 ☻")
        return continueBoard(sudoku)


def saveGame(matrix):
    read()
    player_name = input("What is the player name?: ").upper()
    board_name = input("What is the game name?: ").lower()
    total = player_name + ": " + board_name
    if total not in matrix_name:
        matrix_board.append(matrix)
        matrix_name.append(total)
        IntroduceJSON()
    else:
        print("The name is already used: ")
        print("(1) Yes")
        print("(2) No")
        opcion = input()
        if opcion == "1":
            index = int()
            for i in matrix_name:
                if i == total:
                    index = matrix_name.index(i)
            matrix_board[index] = matrix
            IntroduceJSON()
        elif opcion == "2":
            saveGame(matrix)
        else:
            print("Choose a valid option")

    return continueBoard(matrix)


def loadGame():
    player_name = input("What is the player name?: ").upper()
    game_name = input("What is the game name?: ").lower()
    total = player_name + ": " + game_name
    if total in matrix_name:
        position = int(matrix_name.index(total))
        matrix_solution = matrix_board[position]
        print()
        showBoard(matrix_solution)
        return Menu2(total, matrix_solution)
    else:
        print(f"Sorry, we could not find the name of that game {game_name} player {player_name}")
        return Menu1()


def eraseGame(nombre):
    IndexM = matrix_name.index(nombre)
    matrix_board[IndexM] = "empty"
    IntroduceJSON()
    return Menu1()


def showBoard(board_principal):
    print(Clr.WH + Clr.BD + "  | 1  2  3  | 4  5  6  | 7  8  9 |" + Clr.END + Clr.END)
    for i in range(9):
        if i % 3 == 0:
            print(Clr.WH + "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖" + Clr.END)
            print(Clr.WH + "------------------------------------" + Clr.END)
        print(Clr.WH + Clr.BD + f"{i + 1}" + Clr.END + Clr.END, end=" ")
        for j in range(9):
            if j % 3 == 0:
                print(Clr.WH + Clr.BD + "| " + Clr.END + Clr.END, end="")
            if j == 8:
                if board_principal[i][j] == "0":
                    print(Clr.WH + Clr.BD + str(board_principal[i][j]) + Clr.END + Clr.END,
                          Clr.WH + Clr.BD + "|" + Clr.END + Clr.END)
                else:
                    print(Clr.PP + board_principal[i][j] + Clr.END, Clr.WH + Clr.BD + "|" + Clr.END + Clr.END)
            else:
                if board_principal[i][j] == "0":
                    print(Clr.WH + Clr.BD + str(board_principal[i][j]) + Clr.END + Clr.END + "  ", end="")
                else:
                    print(Clr.PP + str(board_principal[i][j]) + Clr.END + "  ", end="")
        if i == 8:
            print(Clr.WH + "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖" + Clr.END)


# Funcionalidades
def NewMatrix():
    tablero = []
    for i in range(9):
        tablero.append([])
        for j in range(9):
            tablero[i].append("0")
    return tablero

# def NewMatrix():
#     tablero = []
#     file = input(f'What is the file name? ')
#     try: #Open file
#         with open(file, encoding = 'utf8') as f:
#             information = json.load(f) #method can be used to parse a valid JSON string and convert it into a Python Dictionary
#             for line in information['array']: #verify if the name match with an existing JSON file
#                 tablero.append(line)
#         return tablero
#     except IOError:
#         exit(f'{file} not found. \n')

def CompleteSpaces(tabla):
    for n in range(3):
        disponibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(n * 3, (n * 3) + 3):
            for j in range(n * 3, (n * 3) + 3):
                tabla[i][j] = random.choice(disponibles)
                disponibles.remove(tabla[i][j])


def completezeros(tabla, nivel):
    maxzeros = 0
    if nivel == "1":
        maxzeros = 30
    elif nivel == "2":
        maxzeros = 40
    elif nivel == "3":
        maxzeros = 60
    for i in range(maxzeros):
        n = random.randint(0, 8)
        m = random.randint(0, 8)
        tabla[n][m] = "0"


def modvalue(matrix):
    row = input("Choose row    : ")
    column = input("Choose column : ")
    value = input("Choose value   : ")
    print()
    rowB = BetweenOneNine(row)
    columnB = BetweenOneNine(column)
    valueB = BetweenOneNine(value)

    if rowB and columnB and valueB:
        if Validation(matrix, value, int(row), int(column)):
            matrix[int(row) - 1][int(column) - 1] = value
        else:
            print("The value must not be repeated in a row, column or quadrant :) \n")
    else:
        if rowB:
            print("Row value must be between 1 & 9 :) \n")
        if columnB:
            print("Column value must be between 1 & 9 :) \n")
        if valueB:
            print("The value must be between 1 & 9 :) \n")

    return continueBoard(matrix)

PrincipalMenu()