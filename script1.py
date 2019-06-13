from tkinter import *

# Easier to import all elements at once since multiple references will be made

window = Tk()


def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    # Convert value to type float
    t1.insert(END, miles)


b1 = Button(window, text="Convert", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=10)
t1.grid(row=0, column=2)

window.mainloop()
# To end the window loop
