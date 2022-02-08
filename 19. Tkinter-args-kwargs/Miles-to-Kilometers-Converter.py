import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Mile to Kilometer converter")
window.minsize(width=500, height=400)

label_1 = tkinter.Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 =tkinter.Label(text="Miles")
label_2.grid(column=2, row=0)

label_3 =tkinter.Label(text="km")
label_3.grid(column=2, row=1)

label_4 =tkinter.Label(text="0")
label_4.grid(column=1, row=1)


def button_action():
    miles_value = entry.get()
    km_value=(float(miles_value) * 1.6)
    label_4.config(text=km_value)

button=tkinter.Button(text="Calculate", command=button_action)
button.grid(column=1, row=3)


entry = tkinter.Entry(width=10)
# print(entry.get())
entry.grid(column=1, row=0)



window.mainloop()
