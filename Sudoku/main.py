import random


import tkinter as tk
import numpy as np

#Examples https://github.com/dimitri/sudoku/blob/master/sudoku.txt
#https://stackoverflow.com/questions/71277090/how-can-i-create-a-matrix-from-users-input-in-dialog-box-using-tkinter
#https://stackoverflow.com/questions/61875723/get-input-values-from-a-grid-with-several-entry-widgets-on-tkinter

listaSudokus = []



''''
def get_data():
    for r in range(rows):
        entries_row = []
        for c in range(cols):

            print(demand[(r,c)].get())
'''





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



def pintar_sudoku():

    all_entries.clear()
    numeroSudoku = random.randint(0,49)
    sudoku = listaSudokus[numeroSudoku]

    for r in range(rows):
        entries_row = []
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





# --- main ---

rows = 9
cols = 9

demand = {}
demand2 = np.zeros((rows, cols))
window = tk.Tk()
obtener_sudokus()
all_entries = []
pintar_sudoku()
''''
for r in range(rows):
    #entries_row = []
    for c in range(cols):
        e = tk.Entry(window, width=5)  # 5 chars
        e.insert('end', 0)
        e.grid(row=r, column=c)
        #demand[(r, c)]=e
        #entries_row.append(e)
    #all_entries.append(entries_row)
'''''
b = tk.Button(window, text='Verificar', command=get_data)
xd = tk.Button(window, text='Obtener sudoku', command=pintar_sudoku)
b.grid(row=rows+1, column=0, columnspan=cols)
xd.grid(row=rows+2, column=0, columnspan=cols)
window.mainloop()







'''Ejemplo ventana''
layout = [[sg.Text('Pon algo papu'),sg.Input(key='-IN-')],
          [sg.Text('PEguelo',key='-OUT-')],
          [sg.Button('OK ni'),sg.Button('CHAO')]]

window = sg.Window('TITULO',layout)

while True:
    event, values = window.read()
    if event is None or event == 'CHAO':
        break
    window['-OUT-'].update(values['-IN-'])

window.close()

'''''