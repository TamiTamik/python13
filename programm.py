# burtgeliin programm
    # hereglegchiin burtgel(Registriin Dugaar, Owog, Ner, Utas)
    # nomni burtgel(ner, zohiogch, on, turul, angilal)

# create, read, update, delete - CRUD

from tkinter import *

window = Tk()
window.title('burtgeliin programm')
window.geometry('350x200')
window.resizable(0,0)

reg = StringVar()
owog = StringVar()
ner = StringVar()
utas = StringVar()

Label(window, text = 'Registr:').grid(row = 0, column = 0)
Entry(window, bd=1, textvariable = reg).grid(row = 0, column = 1)

Label(window, text = 'Owog:').grid(row = 1, column = 0)
Entry(window, bd=1, textvariable = owog).grid(row = 1, column = 1)

Label(window, text = 'Ner:').grid(row = 2, column = 0)
Entry(window, bd=1, textvariable = ner).grid(row = 2, column = 1)

Label(window, text = 'Utas:').grid(row = 3, column = 0)
Entry(window, bd=1, textvariable = utas).grid(row = 3, column = 1)

def user_save():
    print(reg.get(), owog.get(), ner.get(), utas.get())

Button(window, text = 'hadgalah', command=user_save).grid(row=4,column=0)

window.mainloop()