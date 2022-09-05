import PySimpleGUI as sg
import tkinter as tk
import numpy as np

#Examples https://github.com/dimitri/sudoku/blob/master/sudoku.txt
#https://stackoverflow.com/questions/71277090/how-can-i-create-a-matrix-from-users-input-in-dialog-box-using-tkinter

def get_data():
    for r, row in enumerate(all_entries):
        for c, entry in enumerate(row):
            entry.insert(0)
            text = entry.get()
            demand[r,c] = float(text)

    print(demand)


def obtener_sudokus():
    f = open("sudokus.txt",r)
    linea = ""
    for i in f.readlines():
        linea = i



# --- main ---

rows = 9
cols = 9

demand = np.zeros((rows, cols))

window = tk.Tk()

all_entries = []
for r in range(rows):
    entries_row = []
    for c in range(cols):
        e = tk.Entry(window, width=5)  # 5 chars
        e.insert('end', 0)
        e.grid(row=r, column=c)
        entries_row.append(e)
    all_entries.append(entries_row)

b = tk.Button(window, text='Verificar', command=get_data)
xd = tk.Button(window, text='Obtener sudoku', command=get_data)
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