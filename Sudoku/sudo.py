from tkinter import *
from main import *




root = Tk()
root.title('Sudoku Solver')
root.geometry('500x400')

mylabel = Label(root, text='Fill in the numbers and click solve').grid(row=0, column=0, columnspan=10)

# Create the grid
def beg():
    global e
    cells = {}
    for row in range(1, 10):
        for column in range(1, 10):
            if ((row in (1,2,3,7,8,9) and column in (4,5,6)) or (row in (4,5,6) and column in (1,2,3,7,8,9))):
                kleur='black'
            else:
                kleur='white'
            cell = Frame(root, bg='white', highlightbackground=kleur,
                         highlightcolor=kleur, highlightthickness=2,
                         width=50, height=50,  padx=3,  pady=3, background='black')
            cell.grid(row=row, column=column)
            cells[(row, column)] = cell
            e = Entry(cells[row, column], width=4, bg='white', highlightthickness=0, fg='black', relief=SUNKEN)
            e.pack()





# Tell the button what to do
def solve():
    global e
    test = e.get()
    print(test)

# Create the buttons and give them a command
clearer = Button(root, text='Clear', command=beg)
solver = Button(root, text='Solve', command=solve)

# Locate the buttons
clearer.grid(row=11, column=3, pady=30)
solver.grid(row=11, column=7, pady=30)

# Run it for the first time
beg()




root.mainloop()