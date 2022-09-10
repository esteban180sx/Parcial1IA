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
    """Resuelve el ejercicio del sudoku y al final escribe la solución en un archivo

    Parameters
    ----------
    sudoku: list[list]
        Matriz de números con la informacíon del sudoku

    """
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
    """Revisa dentro del sudoku si es posible poner el número valor en la
    posición i, j dentro de la matriz

    Parameters
    ----------

    i: number
        Posición vertical dentro del parametro sudoku
    j: number
        Posición horizontal dentro del parametro sudoku
    valor: number
        Valor del numero que va a ser insertado en la posición i, j
    sudoku: list[list]
        Tablero de juego del sudoku

    Return
    ------
    boolean
        Al revisar la posición y confirmar si la posición es valida para el
        valor devolvera true

    """
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
    """Devuelve una sub cuadricula de 3x3 del sudoku a la cual pertenece la posición i, j

    Parameters
    ----------
    i: number
        posición vertical del cuadro seleccionado del sudoku
    j: number
        Posición horizontal del cuadro seleccionado del sudoku
    sudoku: list
        Tablero del sudoku con los numeros ingresados

    Returns
    -------
    list
        Contiene los numeros dentro de la cuadricula 3x3

    """
    sub_fila = subgrid_pos(i)
    sub_col = subgrid_pos(j)

    sub_grid = []

    for row in sudoku[sub_fila * 3: sub_fila * 3 + 3]:
        col = row[sub_col * 3: sub_col * 3 + 3]
        for number in col:
            sub_grid.append(number)

    return sub_grid

def subgrid_pos(pos):
    """Devuelve la posición relativa a la cuadricula 3x3 dependiendo del numero
    en pos

    Parameters
    ----------
    pos: number
        Posición no importa la orientación y devuelve la grid 3x3 a la que
        pertenece el valor

    Returns
    -------
    number
        Posición subgrid.
    """
    if pos < 3:
        return 0
    elif pos < 6:
        return 1
    else:
        return 2

def validar_solucion(sudoku):
    """Valida si el sudoku ingresado es valido.

    Parameters
    ----------
    sudoku: list
        Lista con 9 listas dentro con 9 posiciones para simular un sudoku.

    Returns
    -------
    boolean
        True si la solución es valida.

    """
    return validar_columnas(sudoku) and validar_filas(sudoku) and validar_subgrids(sudoku)

def validar_subgrids(sudoku):
    """Valida las 9 sub grid 3x3 dentro del sudoku si están llenadas correctamente.

    Parameters
    ----------
    sudoku: list
        Lista con 9 listas dentro con 9 posiciones para simular un sudoku

    Returns
    boolean
        True si las subgrid son validas.
    """
    subgrids = [0, 3, 6]
    for i in subgrids:
        for j in subgrids:
            for value in range(1, 10):
                subgrid = to_subgrid(i, j, sudoku)
                if not value in subgrid:
                    return False

    return True

def validar_columnas(sudoku):
    """Validas las columnas del sudoku que estén llenadas correctamente.

    Parameters
    ----------
    sudoku: list
        Lista con 9 listas dentro con 9 posiciones para simular un sudoku

    Returns
    boolean
        True si las columnas son validas.
    """
    for i in range(9):
        for j in range(1, 10):
            if not j in [fila[i] for fila in sudoku]:
                return False

    return True

def validar_filas(sudoku):
    """Validas las filas del sudoku que sean validas para la solución

    Parameters
    ----------
    sudoku: list
        Lista con 9 listas dentro con 9 posiciones para simular un sudoku

    Returns
    -------
    boolean
        True si las filas son validas.
    """
    for i in range(9):
        for j in range(1,10):
            if not j in sudoku[i]:
                return False

    return True

def string_sudoku(sudoku):
    """Convierte un sudoku a cadena
    
    Parameters
    ----------
    sudoku:list
        Lista con 9 listas dentro con 9 posiciones

    Returns
    -------
    string
        Cadena con la información del sudoku
    """
    cadena = ""
    for i in sudoku:
        for j in i:
            cadena += f"{j}"
        cadena += "\n"

    return cadena

def escribir_sudoku_archivo(sudoku):
    """Escribe un sudoku en un archivo txt
    
    Parameters
    ----------
    sudoku:list
        Lista con 9 listas dentro con 9 posiciones
    """
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

