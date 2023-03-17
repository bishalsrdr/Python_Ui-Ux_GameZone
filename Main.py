from tkinter import*
from PIL import Image,ImageTk


def nextPage():
    root.destroy()
    import Final3
    
root = Tk()

lbl1 = Label(root, text="PROJECT GROUP - 2",font="Cambria 19 bold",bg="light yellow" , fg = "blue")
lbl1.pack()

# Add Picture


canvas1 = Canvas(width=585, height=97,  bg ='light yellow'  )
canvas1.pack()
#canvas1.place(x=685, y=39)
photo1 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\bietADD.png')
canvas1.create_image(0,0, image=photo1, anchor=NW)



canvas2 = Canvas(width=1550, height=750 , bg ='black' )
canvas2.pack()
#canvas2.place(x=75, y=165)
photo2 = PhotoImage(file='C:\\Users\\Acer\\Desktop\\Python Project\\295.png')
canvas2.create_image(0,0, image=photo2, anchor=NW)

#lbl = Label(root, text="Welcome to Gaming Zone" , bg = "blue" ,font= ('Aerial 17 bold italic'))
#lbl.pack()

btn1 = Button(root, text="S T A R T", command=nextPage)
btn1.pack(padx=20, pady=20)
btn1.place(x=458, y=526)
btn1.configure(height=2 , width =12, font = 'Aerial 12 bold' , bg = 'cyan2' , fg = 'black' , border = '10' )

btn2 = Button(root, text="E X I T", command=lambda:root.destroy())
btn2.pack(padx=20, pady=20)
btn2.place(x=902,y=526)
btn2.configure(height=2 , width =12, font = 'Aerial 12 bold' , bg = 'cyan2' , fg = 'black' , border = '10' )

root.title("Home | Python Game Zone | Welcome")
root.attributes('-fullscreen' , True)
root.configure(bg="light yellow")
root.mainloop()