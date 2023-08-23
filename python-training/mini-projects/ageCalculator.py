from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = int(year.get())
        age.set(2018 - value)
    except ValueError:
        pass

root = Tk()
root.title("Age Calculator 2018")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

year = StringVar()
#meters = StringVar()
age = StringVar()

year_entry = ttk.Entry(mainframe, width=7, textvariable=year)
year_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=age).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Year of Birth").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Age is").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Enter Year of Birth").grid(column=3, row=5, sticky=W)
ttk.Label(mainframe, text="Author: Alientask").grid(column=3, row=6, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

year_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
