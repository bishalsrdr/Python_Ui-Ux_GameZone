from tkinter import *
import tkinter


window = tkinter.Tk()

def snake():
    #window.destroy()
    import snake

#def main():
    #window.destroy()
    #import main


def Game1():
  myLabel = Label(window,text="""Snake is a video game genre where the player manoeuvres a growing line that becomes a primary obstacle to itself. 
  The concept originated in the 1976 two-player arcade game Blockade from Gremlin Industries, and the ease of implementation has led to hundreds of versions for many platforms.""",font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack()
  myLabel.place(x=65,y=615)


def Game2():
  myLabel = Label(window,text="""Flappy Bird is a mobile game developed by Vietnamese video game artist and programmer Dong Nguyen, under his game development company .Gears. The game is a side-scroller 
  where the player controls a bird, attempting to fly between columns of green pipes without hitting them.""",font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=75,y=615)


window.title("Main Menu")


lbl = Label(window, text=" * * * LIST OF GAMES * * * " , bg="BLUE", fg="White",font= ('Cambria 19 bold'))
lbl.pack()

canvas1 = Canvas(width=150, height=150 , bg ='white' )
canvas1.pack()
canvas1.place(x=190, y=70)
photo1 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\G22.png')
canvas1.create_image(0,0, image=photo1, anchor=NW)

LL1 = Label(window, text=" HUNGRY SNAKE  ",font="Calibri 15 bold",fg="black",bg="white")
LL1.pack()
LL1.place(x=192,y=42)

btn1 = Button(window, text="P L A Y" , command=snake)
btn1.pack(padx=20, pady=20)
btn1.place(x=125, y=233)
btn1.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')

btn11 = Button(window, text="A B O U T" , command=Game1)
btn11.pack(padx=20, pady=20)
btn11.place(x=270, y=233)
btn11.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')

canvas2 = Canvas(width=150, height=150 , bg ='white' )
canvas2.pack()
canvas2.place(x=693, y=70)
photo2 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\G23.png')
canvas2.create_image(0,0, image=photo2, anchor=NW)

LL2 = Label(window, text=" FLAPPY BIRD  ",font="Calibri 15 bold",fg="black",bg="white")
LL2.pack()
LL2.place(x=705,y=42)

btn2 = Button(window, text="P L A Y" )
btn2.pack(padx=20, pady=20)
btn2.place(x=635, y=233)
btn2.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')

btn22 = Button(window, text="A B O U T" , command=Game2)
btn22.pack(padx=20, pady=20)
btn22.place(x=780, y=233)
btn22.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')

canvas3 = Canvas(width=150, height=150 , bg ='white' )
canvas3.pack()
canvas3.place(x=1190, y=70)
photo3 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\G24.png')
canvas3.create_image(0,0, image=photo3, anchor=NW)

LL3 = Label(window, text=" ADD LATER  ",font="Calibri 15 bold",fg="black",bg="white")
LL3.pack()
LL3.place(x=1210,y=42)

btn3 = Button(window, text="P L A Y")
btn3.pack(padx=20, pady=20)
btn3.place(x=1130, y=233)
btn3.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')

btn33 = Button(window, text="A B O U T")
btn33.pack(padx=20, pady=20)
btn33.place(x=1275, y=233)
btn33.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')



#EXIT
btn99 = Button(window,height=2 , width =12,text="E X I T", font = 'Aerial 12 bold' ,bg = 'aquamarine2',fg = 'black',command=lambda:window.destroy(), border = '10')
btn99.pack()
btn99.place(x=675, y=725)


canvas4 = Canvas(width=150, height=150 , bg ='white' )
canvas4.pack()
canvas4.place(x=190, y=319)
photo4 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\G24.png')
canvas4.create_image(0,0, image=photo4, anchor=NW)

LL4 = Label(window, text=" ADD LATER  ",font="Calibri 15 bold",fg="black",bg="white")
LL4.pack()
LL4.place(x=208,y=290)

btn4 = Button(window, text="P L A Y" )
btn4.pack(padx=20, pady=20)
btn4.place(x=125, y=483)
btn4.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE', fg = 'white')

btn44 = Button(window, text="A B O U T")
btn44.pack(padx=20, pady=20)
btn44.place(x=275, y=483)
btn44.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')


canvas5 = Canvas(width=150, height=150 , bg ='white' )
canvas5.pack()
canvas5.place(x=693, y=319)
photo5 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\G24.png')
canvas5.create_image(0,0, image=photo5, anchor=NW)

LL5 = Label(window, text=" ADD LATER  ",font="Calibri 15 bold",fg="black",bg="white")
LL5.pack()
LL5.place(x=710,y=290)

btn5 = Button(window, text="P L A Y" )
btn5.pack(padx=20, pady=20)
btn5.place(x=635, y=483)
btn5.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE', fg = 'white')

btn55 = Button(window, text="A B O U T")
btn55.pack(padx=20, pady=20)
btn55.place(x=780, y=483)
btn55.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')


canvas6 = Canvas(width=150, height=150 , bg ='white' )
canvas6.pack()
canvas6.place(x=1190, y=319)
photo6 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\G24.png')
canvas6.create_image(0,0, image=photo6, anchor=NW)

LL6 = Label(window, text=" ADD LATER  ",font="Calibri 15 bold",fg="black",bg="white")
LL6.pack()
LL6.place(x=1208,y=290)

btn6 = Button(window, text="P L A Y" )
btn6.pack(padx=20, pady=20)
btn6.place(x=1130, y=483)
btn6.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE', fg = 'white')

btn66 = Button(window, text="A B O U T")
btn66.pack(padx=20, pady=20)
btn66.place(x=1275, y=483)
btn66.configure(height=2 , width =12, font = 'Aerial 12 bold italic' , bg = 'BLUE' , fg = 'white')

#Developed By

lbl = Label(window, text="Developed By",font="Calibri 13 bold italic",bg="light yellow",fg="black")
lbl.pack()
lbl.place(x=693,y=799)
lbl = Label(window, text=" DEBARATHI SARDAR | BITTU DEY | SUJIT MAITY ",font="Calibri 13 bold",bg="black",fg="white")
lbl.pack()
lbl.place(x=569,y=830)


window.configure(bg='light yellow')

#window.resizable(False , False)

window.attributes('-fullscreen' , True)

#window.geometry("635x610")

window.mainloop()