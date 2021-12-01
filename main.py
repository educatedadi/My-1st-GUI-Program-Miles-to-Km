from tkinter import *


def button_clicked():
    global distance, text_input
    text = round((float(text_input.get()) * 1.609), 2)
    distance.config(text=text)


screen = Tk()
screen.title('Miles to Km')
screen.minsize(300, 150)

Space_label = Label(text=' ')
Space_label.grid(row=0, column=4, pady=5)

text_input = Entry(width=20)
text_input.grid(row=3, column=4)

label1 = Label(text='Miles')
label1.grid(row=3, column=5)

label2 = Label(text='is equal to', padx=20)
label2.grid(row=5, column=2)

distance = Label(text='0')
distance.grid(row=5, column=4, pady=10)

label3 = Label(text='Km')
label3.grid(row=5, column=5)

button1 = Button(text='Calculate', command=button_clicked)
button1.grid(row=6, column=4)


screen.mainloop()
