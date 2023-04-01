from tkinter import *

def calculate():
  result = float(miles_entry.get()) * 1.609
  result_label.config(text=f"{result}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

window.mainloop()