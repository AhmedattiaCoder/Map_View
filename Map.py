from tkinter import *
from tkintermapview import TkinterMapView

def x():
    exit()

def search():
    place1=e1.get()
    Map2.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
    Map2.set_address(place1,marker=True)

app=Tk()
app.geometry('800x500+300+100')
app.resizable(False,False)
app.title("Map")
app.iconbitmap("map.ico")
app.config(bg='#009ba9')
Map2=TkinterMapView(app,width=799,height=400)
Map2.pack()
f1=Frame(bg='#12ecff',width=799,height=80)
f1.place(x=0,y=420)
e1=Entry(f1,bg='#0a00a9',fg='white',font=('',20,''),width=20)
e1.place(x=290,y=20)
l1=Label(f1,text='اسم المكان',font=('',20,''),bg='#12ecff')
l1.place(x=620,y=20)
b1=Button(f1,text='بحث',bg='#06ff15',activebackground='#00d50d',font=('',20,''),borderwidth=0,width=10,height=0,cursor='hand2',command=search)
b1.place(x=100,y=20)
b2=Button(f1,text='خروج',bg='#fef015',activebackground='#d0c402',font=('',20,''),height=0,width=5,borderwidth=0,cursor='hand2',command=x)
b2.place(x=10,y=20)
app.mainloop()