from cProfile import label
from tkinter import *
import tkinter
from turtle import left


window = tkinter.Tk()

def snake():
    window.destroy()
    import snake

#def main():
    #window.destroy()
    #import main


window.title("Main Menu")

lbl = Label(window, text="GAMES" , bg="BLUE", fg="White",font= ('Aerial 12 bold italic'))
lbl.pack()

canvas1 = Canvas(width=75, height=170 , bg ='white' )
canvas1.pack()
canvas1.place(x=29, y=50)
photo1 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\23.png')
canvas1.create_image(0,0, image=photo1, anchor=NW)

btn1 = Button(window, text="P L A Y" , command=snake)
btn1.pack(padx=20, pady=20)
btn1.place(x=4, y=230)
btn1.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE')

canvas2 = Canvas(width=75, height=170 , bg ='white' )
canvas2.pack()
canvas2.place(x=280, y=50)
photo2 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\23.png')
canvas2.create_image(0,0, image=photo2, anchor=NW)

btn2 = Button(window, text="P L A Y" )
btn2.pack(padx=20, pady=20)
btn2.place(x=250, y=230)
btn2.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' )

canvas3 = Canvas(width=75, height=170 , bg ='white' )
canvas3.pack()
canvas3.place(x=526, y=50)
photo3 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\23.png')
canvas3.create_image(0,0, image=photo3, anchor=NW)


btn3 = Button(window, text="P L A Y")
btn3.pack(padx=20, pady=20)
btn3.place(x=500, y=230)
btn3.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' )



#EXIT
btn99 = Button(window,height=2 , width =12,text="E X I T", font = 'Aerial 12 bold italic' ,bg = 'GREEN',fg = 'gold',command=lambda:window.destroy(), border = '10')
btn99.pack()
btn99.place(x=244, y=540)


canvas4 = Canvas(width=75, height=170 , bg ='white' )
canvas4.pack()
canvas4.place(x=29, y=290)
photo4 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\23.png')
canvas4.create_image(0,0, image=photo4, anchor=NW)

btn4 = Button(window, text="P L A Y" )
btn4.pack(padx=20, pady=20)
btn4.place(x=4, y=470)
btn4.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE')


canvas5 = Canvas(width=75, height=170 , bg ='white' )
canvas5.pack()
canvas5.place(x=280, y=290)
photo5 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\23.png')
canvas5.create_image(0,0, image=photo5, anchor=NW)

btn5 = Button(window, text="P L A Y" )
btn5.pack(padx=20, pady=20)
btn5.place(x=250, y=470)
btn5.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE')


canvas6 = Canvas(width=75, height=170 , bg ='white' )
canvas6.pack()
canvas6.place(x=526, y=290)
photo6 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\23.png')
canvas6.create_image(0,0, image=photo6, anchor=NW)

btn6 = Button(window, text="P L A Y" )
btn6.pack(padx=20, pady=20)
btn6.place(x=500, y=470)
btn6.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE')




window.configure(bg='red2')

window.resizable(False , False)

window.geometry("635x610")

window.mainloop()