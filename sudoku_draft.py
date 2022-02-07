import json
import random


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

def VerificaExistencia(file):
    try:
        with open(file, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def new_value(value):
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    true_value = False
    if value in list:
        true_value = True
    return true_value

def Search(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == '0':
                return i, j
    return False

def ReviewValue(sudoku, num, row, col):
    for i in range(9):
        if sudoku[row][i] == num and col != i:
            return False
        if sudoku[i][col] == num and row != i:
            return False

    value_x = col // 3
    value_y = row // 3
    for i in range(value_y*3, value_y*3 + 3):
        for j in range(value_x * 3, value_x*3 + 3):
            if sudoku[i][j] == num and (i, j) != (row, col):
                return False

    return True


#BackTracking
def ResuelveCifra(sudoku):
    find = Search(sudoku)
    if not find:
        return True
    else:
        row, col = find
    list=['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in list:
        if ReviewValue(sudoku, num, row, col):
            sudoku[row][col] = num
            if ResuelveCifra(sudoku):
                return True
            sudoku[row][col] = '0'
    return False

# JSON
if not VerificaExistencia('sudoku.json'):
    DBsudoku = open('sudoku.json', 'w+')
    dicNuevo = dict()
    json.dump(dicNuevo, DBsudoku)
    DBsudoku.close()


def leeSudokus():
    global jBoard, jName
    jName = []
    jBoard = []
    jFile = open('sudoku.json', 'r')
    jSud = json.load(jFile)
    jFile.close()
    jSudNom = jSud.keys()
    jSudTab = jSud.values()
    for i in jSudNom:
        jName.append(i)
    for i in jSudTab:
        jBoard.append(i)


def IntroduceJSON():
    DICtemp = dict()
    jFile = open('sudoku.json', 'w')
    for i in range(len(jBoard)):
        DICtemp[jName[i]] = jBoard[i]
        if jBoard[i] == 'vacío':
            del DICtemp[jName[i]]
    json.dump(DICtemp, jFile)
    jFile.close()


# Menus
def MenuPrincipal():
    print()
    print(Clr.WH + ' - - SUDOKU - - ' + Clr.END)
    print(Clr.CN + '                                          ' + Clr.END)
    print(Clr.CN + '    ' + Clr.END, Clr.YW + '' + Clr.END,
          Clr.BL + Clr.BD + ' MENU' + Clr.END + Clr.END, Clr.YW + '           ' + Clr.END,
          Clr.CN + f'' + Clr.END)
    print(Clr.CN + '                                          ' + Clr.END)
    print(Clr.CN + '    ' + Clr.END, Clr.WH + Clr.END,
          Clr.GR2 + Clr.BD + '(1) New Game' + Clr.END + Clr.END, '        ', Clr.CN + '' +  Clr.END)
    print(Clr.CN + '    ' + Clr.END, Clr.WH + Clr.END,
          Clr.GR2 + Clr.BD + '(2) End' + Clr.END + Clr.END, ' ', Clr.CN + '' + Clr.END)
    # print(Clr.CN + '    ' + Clr.END, Clr.WH + Clr.END, Clr.GR2 + Clr.BD + '(3) Finalizar' + Clr.END + Clr.END,
    #       '                  ', Clr.CN + '' + Clr.END)
    print(Clr.CN + '                                          ' + Clr.END)
    print(Clr.DC + ' ------------------ ' + Clr.END)
    opcion = input()
    return menuOpciones(opcion)


def menuOpciones(opcion):
    if opcion == '1':
        print(Clr.DC + ' --------------------' + Clr.END)
        print(Clr.DC + '|' + Clr.END, ' 👇', Clr.BD + Clr.WH + ' Sudoku' + Clr.END + Clr.END, end='')
        print(Clr.DC + '    |' + Clr.END)
        print(Clr.DC + '|' + Clr.END, Clr.BD + '(1)', Clr.GR + ' Easy   () ' + Clr.END + Clr.END,
              Clr.DC + '|' + Clr.END)
        print(Clr.DC + '|' + Clr.END, Clr.BD + '(2)', Clr.YW + ' Medium   () ' + Clr.END + Clr.END,
              Clr.DC + '|' + Clr.END)
        print(Clr.DC + '|' + Clr.END, Clr.BD + '(3)', Clr.RD + ' Hard () ' + Clr.END + Clr.END,
              Clr.DC + '|' + Clr.END)
        print(Clr.DC + ' --------------------' + Clr.END)
        dificultad = input()
        sudoku = CreaMatrizInicial()
        RellenaCuadrante(sudoku)
        ResuelveCifra(sudoku)
        mode = ['1', '2', '3']
        if dificultad in mode:
            RellenaCeros(sudoku, dificultad)
        else:
            print('Choose the level >:)')
            return menuOpciones(opcion)
        continuaTablero(sudoku)
        print()
        print()
        return sudoku

    elif opcion == '2':
        print()
        print('New Board...', end='')
        Menu1()

    elif opcion == '3':
        print(Clr.WH + Clr.BD + '- - End - -')
        return IntroduceJSON()
    else:
        print('Please choose and option between 1 & 3\n')
        print()
        return MenuPrincipal()


def Menu1():
    leeSudokus()
    print()
    print()
    print(Clr.BD + ' ____________________' + Clr.END)
    print(Clr.BD + '|' + Clr.END, '\033[03m' + Clr.BD + '\033[93m' + 'Saved Boards' + Clr.END,
          Clr.BD + '|' + Clr.END)
    print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
    c = 0
    for i in jName:
        if jBoard[c] != 'empty':
            Clr().colorAlAzar()
            print('\033[03m' + i + Clr.END)
            print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        c += 1

    # Comprobar si no hay matrices
    EstaVacio = True
    for i in jBoard:
        if i != 'vacío':
            EstaVacio = False

    if EstaVacio:
        print('o boards')
        print('(0) Menu')
        print('(1) End')
        opcion = input()
        if opcion == '0':
            return MenuPrincipal()
        elif opcion == '1':
            print('- - End - -')
            return IntroduceJSON()
        else:
            print('Wrong Option :)')
            return Menu1()

    else:
        print('New Board? ')
        print('(1) Yes')
        print('(2) Return to Menu')
        opcion = input('')

        if opcion == '1':
            cargaPartida()

        elif opcion == '2':
            print()
            print('Menu...')
            print()
            print()
            return MenuPrincipal()

        else:
            print('Wrong Option')
            return Menu1()


def continuaTablero(sudoku):
    MuestraTablero(sudoku)
    print()
    print(Clr.YW + '◤--', '                 ', '--◥')
    print(Clr.YW + '|', Clr.WH + '(0) Keep Playing' + Clr.END, '   ', Clr.YW + '|')
    print(Clr.YW + '|', Clr.WH + '(1) Answers' + Clr.END, Clr.YW + '|')
    print(Clr.YW + '|', Clr.WH + '(2) Menu' + Clr.END, '   ', Clr.YW + '|')
    print(Clr.YW + '◣--', '                 ', '--◢')
    opcion = input()
    if opcion == '0':
        return modValor(sudoku)
    elif opcion == '1':
        if Search(sudoku):
            ResuelveCifra(sudoku)
            if Search(sudoku):
                print('No Solition :c')
        else:
            print('It is solve:)')
        return continuaTablero(sudoku)
    elif opcion == '2':
        print()
        print('Menul...')
        print()
        print()
        return MenuPrincipal()
    else:
        print('Please choose and option between 1 & 3')
        return continuaTablero(sudoku)

def borraPartida(nombre):
    IndexM = jName.index(nombre)
    jBoard[IndexM] = 'vacío'
    IntroduceJSON()
    return Menu1()


def MuestraTablero(tablero_principal):
    print(Clr.WH + Clr.BD + '  | 1  2  3  | 4  5  6  | 7  8  9 |' + Clr.END + Clr.END)
    for i in range(9):
        if i % 3 == 0:
            print(Clr.WH + '➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖' + Clr.END)
            print(Clr.WH + '------------------------------------' + Clr.END)
        print(Clr.WH + Clr.BD + f'{i + 1}' + Clr.END + Clr.END, end=' ')
        for j in range(9):
            if j % 3 == 0:
                print(Clr.WH + Clr.BD + '| ' + Clr.END + Clr.END, end='')
            if j == 8:
                if tablero_principal[i][j] == '0':
                    print(Clr.WH + Clr.BD + str(tablero_principal[i][j]) + Clr.END + Clr.END,
                          Clr.WH + Clr.BD + '|' + Clr.END + Clr.END)
                else:
                    print(Clr.PP + tablero_principal[i][j] + Clr.END, Clr.WH + Clr.BD + '|' + Clr.END + Clr.END)
            else:
                if tablero_principal[i][j] == '0':
                    print(Clr.WH + Clr.BD + str(tablero_principal[i][j]) + Clr.END + Clr.END + '  ', end='')
                else:
                    print(Clr.PP + str(tablero_principal[i][j]) + Clr.END + '  ', end='')
        if i == 8:
            print(Clr.WH + '➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖' + Clr.END)


# Funcionalidades
def CreaMatrizInicial():
    tablero = []
    for i in range(9):
        tablero.append([])
        for j in range(9):
            tablero[i].append('0')
    return tablero


def RellenaCuadrante(tabla):
    for n in range(3):
        disponibles = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(n * 3, (n * 3) + 3):
            for j in range(n * 3, (n * 3) + 3):
                tabla[i][j] = random.choice(disponibles)
                disponibles.remove(tabla[i][j])


def RellenaCeros(tabla, nivel):
    maxceros = 0
    if nivel == '1':
        maxceros = 30
    elif nivel == '2':
        maxceros = 40
    elif nivel == '3':
        maxceros = 60
    for i in range(maxceros):
        n = random.randint(0, 8)
        m = random.randint(0, 8)
        tabla[n][m] = '0'


def modValor(matriz):
    row = input('👉 Row value   : ')
    columna = input('👉 Column value : ')
    value = input('👉 Value   : ')
    print()
    filaB = new_value(row)
    columnaB = new_value(columna)
    valorB = new_value(value)

    if filaB and columnaB and valorB:
        if ReviewValue(matriz, value, int(row), int(columna)):
            matriz[int(row) - 1][int(columna) - 1] = value
        else:
            print('This value is already used:) \n')
    else:
        if filaB:
            print('Row value between 1 & 9 :) \n')
        if columnaB:
            print('Column value  between 1 & 9 :) \n')
        if valorB:
            print('Wrong value :) \n')

    return continuaTablero(matriz)

MenuPrincipal()