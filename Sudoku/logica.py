sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]

def resolver_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for valor in range(1, 10):
                    permitido = es_permitido(i, j, valor, sudoku)
                    if permitido:
                        sudoku[i][j] = valor
                        resolver_sudoku(sudoku)
                        sudoku[i][j] = 0
                return
    escribir_sudoku_archivo(sudoku)
    return

def es_permitido(i, j, valor, sudoku):
    if valor in sudoku[i]:
        return False

    columna = [fila[j] for fila in sudoku]

    if valor in columna:
        return False

    subgrid = to_subgrid(i, j, sudoku);
    if valor in subgrid:
        return False

    return True


def to_subgrid(i, j, sudoku):
    sub_fila = subgrid_pos(i)
    sub_col = subgrid_pos(j)

    sub_grid = []

    for row in sudoku[sub_fila * 3: sub_fila * 3 + 3]:
        col = row[sub_col * 3: sub_col * 3 + 3]
        for number in col:
            sub_grid.append(number)

    return sub_grid

def subgrid_pos(pos):
    if pos < 3:
        return 0
    elif pos < 6:
        return 1
    else:
        return 2

def validar_solucion(sudoku):
    return validar_columnas(sudoku) and validar_filas(sudoku) and validar_subgrids(sudoku)

def validar_subgrids(sudoku):
    subgrids = [0, 3, 6]
    for i in subgrids:
        for j in subgrids:
            for value in range(1, 10):
                subgrid = to_subgrid(i, j, sudoku)
                if not value in subgrid:
                    return False

    return True

def validar_columnas(sudoku):
    for i in range(9):
        for j in range(1, 10):
            if not j in [fila[i] for fila in sudoku]:
                return False

    return True

def validar_filas(sudoku):
    for i in range(9):
        for j in range(1,10):
            if not j in sudoku[i]:
                return False

    return True

def string_sudoku(sudoku):
    cadena = ""
    for i in sudoku:
        for j in i:
            cadena += f"{j}"
        cadena += "\n"

    return cadena

def escribir_sudoku_archivo(sudoku):
    file = open("respuesta.txt", "w")
    file.write(string_sudoku(sudoku))
    file.close()


##### funciones para trabajar el input del usuario

def validar_fila(sudoku, i, valor):
    return valor in sudoku[i]

def validar_columna(sudoku, j, valor):
    return valor in [fila[j] for fila in sudoku]

def validar_subgrid(sudoku, i, j, valor):
    subgrid = to_subgrid(i, j, sudoku)
    return valor in subgrid

