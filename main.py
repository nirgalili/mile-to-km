from tkinter import *

# window

window = Tk()
text1 = "Mile to Km Converter"
window.title(text1)
window.config(padx=20, pady=20)

# label

my_label1 = Label(text="Miles")
my_label1.grid(column=3, row=1)

my_label2 = Label(text="Km")
my_label2.grid(column=3, row=2)

my_label3 = Label(text="is equal to")
my_label3.grid(column=1, row=2)

calculated = 0
my_label4 = Label(text=calculated)
my_label4.grid(column=2, row=2)

# button

def button_clicked():
    mile = float(input.get())
    Km = mile*1.60934
    my_label4.config(text=round(Km, 2))


button = Button(text="Calculate")
button["command"] = button_clicked
button.grid(column=2, row=3)

#Entry

input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=2, row=1)

window.mainloop()