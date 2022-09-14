

""""
Sudoku creado por Sebastian David Rendon Soto y Esteban Sanchez Carranza

con referencias de

#Examples https://github.com/dimitri/sudoku/blob/master/sudoku.txt
#https://stackoverflow.com/questions/71277090/how-can-i-create-a-matrix-from-users-input-in-dialog-box-using-tkinter
#https://stackoverflow.com/questions/61875723/get-input-values-from-a-grid-with-several-entry-widgets-on-tkinter
# https://www.youtube.com/watch?v=KWP90gAsOa8


"""


import random
import numpy as np
import tkinter as tk
from tkinter import messagebox
import logica as lg





"""
Método que verifica la solucion segun los datos 
ingresados en el sudoku
"""
def validar_solucion():

    if   lg.validar_solucion(get_data())==True:
        tk.messagebox.showinfo("FELICIDADES",
        "Felicitaciones crack!, solucionaste el sudoku")
    else:
        tk.messagebox.showwarning("SIGUE INTENTANDO",
        "Sigue intentando, se que tu puedes")



"""
Método que obtiene los datos ingresados en el sudoku
"""

def get_data():

    for r, row in enumerate(all_entries):
        for c, entry in enumerate(row):
            text = entry.get()
            demand2[r,c] = int(text)

    l = demand2.tolist()



    return l




"""
Método que escribe un archivo txt con la solucion del sudoku
"""
def get_solucion():

    lg.resolver_sudoku(get_data())





"""
Método que lee un archivo con 50 sudokus y los separa en una lista
"""
def obtener_sudokus():

    f = open("sudokus.txt","r")
    con = 0


    sudoku = []
    for i in f.readlines():
        linea = i
        if (i[0:1]!='G'):

            linea_sudoku = list(linea)
            linea_sudoku.pop(-1)
            linea_sudoku=convertirListaInt(linea_sudoku)
            sudoku.insert(con,linea_sudoku)
            con+=1


    for i in range(50):
        sudoku_separado = []
        for row in range(9):
            sudoku_separado.append(sudoku[row + i*9])

        listaSudokus.append(sudoku_separado)


"""
Método que lee el archivo de respuesta.txt que contiene la respuesta de un sudoku y lo transforma en listas
"""

def obtener_sudoku_respuesta():

    f = open("respuesta.txt","r")
    con = 0


    sudoku = []
    for i in f.readlines():
        linea = i
        linea_sudoku = list(linea)
        linea_sudoku.pop(-1)
        linea_sudoku=convertirListaInt(linea_sudoku)
        sudoku.insert(con,linea_sudoku)
        con+=1

    return sudoku


"""
Método que convierte una lista de 
strings en lista de enteros
"""

def convertirListaInt(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    return lista





"""
Método que dibuja la respuesta de una matrix en la interfaz
"""
def pintar_sudoku_respuesta():

    get_solucion()

    all_entries.clear()
    all_cells.clear()
    sudoku = obtener_sudoku_respuesta()

    for r in range(rows):
        entries_row = []
        cells_row = []
        for c in range(cols):
            if ((r in (1-1,2-1,3-1,7-1,8-1,9-1) and c in (4-1,5-1,6-1)) or (r in (4-1,5-1,6-1) and c in (1-1,2-1,3-1,7-1,8-1,9-1))):
                kleur='black'
            else:
                kleur='white'


            cell = tk.Frame(window, bg='white', highlightbackground=kleur,
                            highlightcolor=kleur, highlightthickness=2,
                            width=50, height=50,  padx=3,  pady=3, background='black')

            if (sudoku[r][c]!=0):


                cell.grid(row=r, column=c)
                cells_row.append(cell)
                e = tk.Entry(cell, width=4, bg='white', highlightthickness=0, fg='black',justify=tk.CENTER)
                e.insert('end', sudoku[r][c])
                e.config(state="readonly")
                e.pack()
                entries_row.append(e)
            else:
                cell.grid(row=r, column=c)
                cells_row.append(cell)
                e = tk.Entry(cell, width=4, bg='white', highlightthickness=0, fg='blue',justify=tk.CENTER)
                e.insert('end', sudoku[r][c])
                e.pack()
                entries_row.append(e)

        all_entries.append(entries_row)
        all_cells.append(cells_row)



"""
Método que dibuja la interfaz del sudoku obteniendo un sudoku aleatorio
"""

def pintar_sudoku():

    all_entries.clear()
    all_cells.clear()
    numeroSudoku = random.randint(0,49)
    sudoku = listaSudokus[numeroSudoku]

    for r in range(rows):
        entries_row = []
        cells_row = []
        for c in range(cols):
            if ((r in (1-1,2-1,3-1,7-1,8-1,9-1) and c in (4-1,5-1,6-1)) or (r in (4-1,5-1,6-1) and c in (1-1,2-1,3-1,7-1,8-1,9-1))):
                kleur='black'
            else:
                kleur='white'


            cell = tk.Frame(window, bg='white', highlightbackground=kleur,
                         highlightcolor=kleur, highlightthickness=2,
                         width=50, height=50,  padx=3,  pady=3, background='black')

            if (sudoku[r][c]!=0):


                cell.grid(row=r, column=c)
                cells_row.append(cell)
                e = tk.Entry(cell, width=4, bg='white', highlightthickness=0, fg='black',justify=tk.CENTER)
                e.insert('end', sudoku[r][c])
                e.config(state="readonly")
                e.pack()
                entries_row.append(e)
            else:
                cell.grid(row=r, column=c)
                cells_row.append(cell)
                e = tk.Entry(cell, width=4, bg='white', highlightthickness=0, fg='blue',justify=tk.CENTER)
                e.insert('end', sudoku[r][c])
                e.pack()
                entries_row.append(e)

        all_entries.append(entries_row)
        all_cells.append(cells_row)


# --- main ---

"""
Método principal que dibuja la ventana e invoca la obtencion de sudokus y pintar sudokus que dibuja la interfaz inicial con un sudoku aleatorio
"""
if __name__ == '__main__':
    listaSudokus = []
    rows = 9
    cols = 9


    demand2 = np.zeros((rows, cols),dtype=int)
    window = tk.Tk()
    obtener_sudokus()
    all_entries = []
    all_cells =[]
    pintar_sudoku()
    b = tk.Button(window, text='Verificar', command=validar_solucion)
    obtener = tk.Button(window, text='Obtener sudoku', command=pintar_sudoku)
    solucionar = tk.Button(window, text='Solucionar sudoku', command=pintar_sudoku_respuesta)
    b.grid(row=rows+1, column=0, columnspan=cols)
    obtener.grid(row=rows+2, column=0, columnspan=cols)
    solucionar.grid(row=rows+3, column=0, columnspan=cols)
    window.mainloop()





