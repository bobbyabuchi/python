from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(figure.get())
        rate = int(exchange.get())
        amount.set(rate * value)
    except ValueError:
        pass

root = Tk()
root.title("Global Currency Converter")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

figure = StringVar()
exchange = StringVar()
amount = StringVar()

figure_entry = ttk.Entry(mainframe, width=7, textvariable=figure)
figure_entry.grid(column=1, row=2, sticky=(W, E))

exchange_entry = ttk.Entry(mainframe, width=7, textvariable=exchange)
exchange_entry.grid(column=1, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Global Currency Converter").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Enter Figure").grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Exchange Rate").grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text=">>>>>>> Amount :").grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, textvariable=amount).grid(column=3, row=4, sticky=(W, E))
#ttk.Label(mainframe, textvariable=exchange).grid(column=1, row=5, sticky=(W, E))
ttk.Label(mainframe, text="author: alientask").grid(column=3, row=6, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

figure_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
