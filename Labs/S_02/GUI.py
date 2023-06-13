from tkinter import *

window_1 = Tk()

window_1.title("Tkinter1")
window_1.geometry('600x600')

Label_1 = Label(window_1, text= "Kahwagy's")
Label_1.pack(side= TOP)

button_1 = Button(window_1, text= "North")
button_1.pack(side= TOP)

button_2 = Button(window_1, text= "South")
button_2.pack(side= BOTTOM)

button_3 = Button(window_1, text= "East")
button_3.pack(side= RIGHT)

button_4 = Button(window_1, text= "West")
button_4.pack(side= LEFT)

button_5 = Button(window_1, text= "Destroy",bd = '5' ,command = window_1.destroy)
button_5.pack(side= BOTTOM)

def PrintName():
    print("Muhammad Alkahwagy")

button_6 = Button(window_1, text= "Print Name",bd = '5' ,command =PrintName )
button_6.pack(side= TOP)


photo_1 = PhotoImage(file='mo.png')
photo_1 = photo_1.subsample(2,2)

button_7 = Button(window_1, text= "MO",image=photo_1)
button_7.pack(side= TOP)

window_1.mainloop()