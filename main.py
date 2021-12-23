# Mile to KM converter
from tkinter import *


def calculate():
    miles = float(user_input.get())
    km = miles * 1.609
    result_label["text"] = f"{km}"


screen = Tk()
screen.title("Miles to Km")
screen.config(padx=20, pady=20)

user_input = Entry(width=10)
mile_label = Label(text="Miles")
is_equal_to_label = Label(text="Is equal to")
result_label = Label(text="0")
km_label = Label(text="Km")
calculate_button = Button(text="Calculate", command=calculate)

user_input.grid(column=1, row=0)
mile_label.grid(column=2, row=0)
is_equal_to_label.grid(column=0, row=1)
result_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)

# All code before exit
screen.mainloop()
