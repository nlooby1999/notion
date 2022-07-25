from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo('you have accepted the terms of service',message='you accpted')

window = Tk()

button = Button(window, command=click,text="Click to accept the terms of service")
button.pack()
window.mainloop()