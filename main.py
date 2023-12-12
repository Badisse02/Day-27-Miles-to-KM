from tkinter import *


window = Tk()
window.title("My first GUI program")
window.minsize(400, 200)
window.config(padx=20, pady=20)

# repair = Label(window, text="  ", font=("Arial", 24))
# repair.config(padx=20, pady=20)
# repair.grid(row=1, column=1)

enter = Entry(window, width=10)
enter.insert(END, string="0")
enter.grid(row=1, column=2)

is_equal = Label(window, text="is equal to ", font=("Arial", 20))
is_equal.grid(row=2, column=1)

miles = Label(window, text="Miles ", font=("Arial", 20))
miles.config(padx=20, pady=20)
miles.grid(row=1, column=3)

km = Label(window, text="Km", font=("Arial", 20))
km.config(padx=20, pady=20)
km.grid(row=2, column=3)

s = 0
result = Label(window, text=f"0", font=("Arial", 20))
result.grid(row=2, column=2)


def calculate():
    a = "{:.2f}".format(float(enter.get()) * 1.609344)
    result["text"] = f"{a}"
    result.grid(row=2, column=2)


button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=2)

window.mainloop()
