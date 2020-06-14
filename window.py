from tkinter import * # * - vse komponenti(Button, Label...)

from PIL import Image, ImageTk

window = Tk()
window.title('Minecraft 2.2.8')
width = 1200
height = 720
window.geometry('{}x{}'.format(width, height))
window.resizable(100,100) #(0,0) - ne izmenyaetsya

Lb1 = Listbox(window)
Lb1.insert(1, "vot eto")
Lb1.insert(2, "pa")
Lb1.insert(3, "pa")
Lb1.insert(4, "pa")
Lb1.insert(5, "vo")
Lb1.insert(6, "rot")

Lb1.pack()

mb = Menubutton(window, text="pay respect", relief=RAISED)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label="HAH",
                        variable=mayoVar)
mb.menu.add_checkbutton(label="HEH",
                        variable=ketchVar)

mb.pack()

def click():
    print('loading...')

button1 = Button(window, text = 'skachat tanki online besplatno(net)', 
command = click, 
activebackground = "red", 
activeforeground = "red").pack()

Checkbutton(window, text = 'postavi galku',
    variable = 'postavil',
    onvalue = 1,
    offvalue = 0,
    height = 5, width = 20, command = click).pack()

name = StringVar() #Stringvar - class

def ok():
    print('ladno', name.get())
    name.set('')

Label(window, text = 'familiya imya otchestvo: ').pack(side = LEFT)
Entry(window, bd=1, textvariable = name).pack(side=RIGHT)
Button(window, text = 'prohodi ne stesnjaysya', command = ok).pack(side = RIGHT)

window.mainloop()
