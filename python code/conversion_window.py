import tkinter as tk
from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(celsius.get())
        fahrenheit.set(int((9/5*value)+32))
        kelvin.set(int(value+272.15))
        rankine.set(int((value*9/5)+491.67))
    except ValueError:
        pass

root = Tk()
root.title("Celsius to Fahrenheit, Kelvin and Rankine!")

mainframe = ttk.Frame(root, padding=" 5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

celsius = StringVar()
celsius_entry = ttk.Entry(mainframe, width=7, textvariable=celsius)
celsius_entry.grid(column=2, row=1, sticky=(W, E))

fahrenheit = StringVar()
ttk.Label(mainframe, textvariable=fahrenheit).grid(column=2, row=2, sticky=(W, E))

kelvin = StringVar()
ttk.Label(mainframe, textvariable=kelvin).grid(column=2, row=3, sticky=(W, E))

rankine = StringVar()
ttk.Label(mainframe, textvariable=rankine).grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=5, sticky=W)

ttk.Label(mainframe, text="degrees Celsius").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="degrees Fahrenheit").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Kelvin").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="degrees Rankine").grid(column=3, row=4, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

celsius_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
