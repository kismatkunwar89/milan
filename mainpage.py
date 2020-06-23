from tkinter import*
from PIL import  ImageTk, Image
import os

window=Tk()
window.geometry("604x550")

window.title("THe Ultimate Walkers Mart")
window.maxsize(704, 650)
window.minsize(704, 650)

def myfunc():
    window.destroy()
    Call1= os.system("python3 /Users/kismat/Desktop/PROJECT/1.py")
    print(Call1)
    
def create_image(filename): 
    img=Image.open(filename)
    img = img.resize((650, 600), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(img)
    return photo
    
image1=create_image("1.png")
lbl1=Label(window,image=image1)
lbl1.place(x=30,y=0)

def cimage(filename): 
    img=Image.open(filename)
    img = img.resize((75, 25), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(img)
    return photo
    
image2=cimage("2.png")
btn1=Button(window,image=image2,command=myfunc)
btn1.place(x=520,y=420)

f1 = Frame(window, bg="#203A43", borderwidth=6, relief=SUNKEN)
f1.place(x=260,y=400)

lb2=Label(f1,text="BILL ENQUIRY",font=("Comic sans MS",24,"bold"),background="#414345",foreground="#ffffff")
lb2.pack()

lb3=Label(window,text="Location;\n Kapan,Budhanilkantha-11\nKathmandu,Nepal",width=100, font=("Times",24),anchor=SW,background="#414345",foreground="#cac531")
lb3.pack(side=BOTTOM)

window.mainloop()































