#Examples https://github.com/dimitri/sudoku/blob/master/sudoku.txt
#https://stackoverflow.com/questions/71277090/how-can-i-create-a-matrix-from-users-input-in-dialog-box-using-tkinter
#https://stackoverflow.com/questions/61875723/get-input-values-from-a-grid-with-several-entry-widgets-on-tkinter

import random
import numpy as np
import tkinter as tk



"""
Método que obtiene los datos ingresados en el sudoku
"""


def get_data():

    for r, row in enumerate(all_entries):
        for c, entry in enumerate(row):
            text = entry.get()
            demand2[r,c] = int(text)

    l = demand2.tolist()

    print(l)



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





def convertirListaInt(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    return lista






def pintar_sudoku2():

    all_entries.clear()
    numeroSudoku = random.randint(0,49)
    sudoku = listaSudokus[numeroSudoku]

    for r in range(rows):
        entries_row = []
        cells_row = []
        for c in range(cols):

            if (sudoku[r][c]!=0):

                e = tk.Entry(window, width=5)  # 5 chars
                e.insert('end', sudoku[r][c])
                e.config(state="readonly")
                e.grid(row=r, column=c)
                demand[(r, c)]=e
                entries_row.append(e)
            else:
                e = tk.Entry(window,width=5)
                e.insert('end', sudoku[r][c])
                e.grid(row=r, column=c)
                demand[(r, c)]=e
                entries_row.append(e)

        all_entries.append(entries_row)



def pintar_sudoku():

    all_entries.clear()
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

                """
                e = tk.Entry(window, width=5)  # 5 chars
                e.insert('end', sudoku[r][c])
                e.config(state="readonly")
                e.grid(row=r, column=c)
                demand[(r, c)]=e
                entries_row.append(e)
                """

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


if __name__ == '__main__':
    listaSudokus = []
    rows = 9
    cols = 9

    demand = {}
    demand2 = np.zeros((rows, cols),dtype=int)
    window = tk.Tk()
    obtener_sudokus()
    all_entries = []
    all_cells =[]
    pintar_sudoku()
    b = tk.Button(window, text='Verificar', command=get_data)
    xd = tk.Button(window, text='Obtener sudoku', command=pintar_sudoku)
    b.grid(row=rows+1, column=0, columnspan=cols)
    xd.grid(row=rows+2, column=0, columnspan=cols)
    window.mainloop()





