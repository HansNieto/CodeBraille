#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import*
import time
import pyperclip


    

def senales():
    
    
    def tra(*args):
        if txt.get() == "a":
            return entrada.set("0")       
        elif txt.get()=="b":
            return entrada.set("1")
        elif txt.get()=="c":
            return entrada.set("2")
        elif txt.get()=="d":
            return entrada.set("3")
        elif txt.get()=="e":
            return entrada.set("4")
        elif txt.get()=="f":
            return entrada.set("5")
        elif txt.get()=="g":
            return entrada.set("6")
        elif txt.get()=="h":
            return entrada.set("7")
        elif txt.get()=="i":
            return entrada.set("8")
        elif txt.get()=="j":
            return entrada.set("9")
        elif txt.get()=="k":
            return entrada.set("10")
        elif txt.get()=="l":
            return entrada.set("11")
        elif txt.get()=="m":
            return entrada.set("12")
        elif txt.get()=="n":
            return entrada.set("13")
        elif txt.get()=="ñ":
            return entrada.set("14")
        elif txt.get()=="o":
            return entrada.set("15")
        elif txt.get()=="p":
            return entrada.set("16")
        elif txt.get()=="q":
            return entrada.set("17")
        elif txt.get()=="r":
            return entrada.set("18")
        elif txt.get()=="s":
            return entrada.set("19")
        elif txt.get()=="t":
            return entrada.set("20")
        elif txt.get()=="u":
            return entrada.set("21")
        elif txt.get()=="v":
            return entrada.set("22")
        elif txt.get()=="w":
            return entrada.set("23")
        elif txt.get()=="x":
            return entrada.set("24")
        elif txt.get()=="y":
            return entrada.set("25")
        elif txt.get()=="z":
            return entrada.set("26")
    def change_image(*args):
  
        if entrada.get() == "0":
            label.config(image=photos[int(entrada.get())]) 
        elif entrada.get()=="1":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="2":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="3":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="4":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="5":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="6":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="7":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="8":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="9":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="10":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="11":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="12":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="13":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="14":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="15":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="16":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="17":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="18":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="19":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="20":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="21":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="22":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="23":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="24":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="25":
            label.config(image=photos[int(entrada.get())])
        elif entrada.get()=="26":
            label.config(image=photos[int(entrada.get())])
        
        
        
        
    
        
            
        
    ven.destroy()
    venS=Tk()
    imagenf=PhotoImage(file="senas.png")
    labelFondo=Label(venS,image=imagenf)
    labelFondo.place(x=0,y=0,relwidth=1,relheight=1)
    venS.title("Traductor")
    venS.geometry("700x600+350+120")
    venS.resizable(0,0)
    venS.iconbitmap("icono.ico")
    labelTitulo=Label(venS, text="SEÑALES",fg="#711610", bg="white", font="arial 25 italic bold").place(x=270,y=5)
    lblpalabra=Label(text="digite la letra que quiere traducir: ", font="arial 14 italic bold ").place(x=20,y=70)
    entrada=StringVar()
    txt=Entry(venS, font="arial 14")
    txt.place(x=350,y=70)
    btn=Button(venS, text="traducir", command=tra).place(x=580,y=70)
    entrada.trace("w", change_image)
    photos =[PhotoImage(file='letra a.png'), PhotoImage(file='letra b.png'), PhotoImage(file='letra c.png'),
             PhotoImage(file='letra d.png'), PhotoImage(file='letra e.png'), PhotoImage(file='letra f.png'),
             PhotoImage(file='letra g.png'), PhotoImage(file='letra h.png'), PhotoImage(file='letra i.png'),
             PhotoImage(file='letra j.png'), PhotoImage(file='letra k.png'), PhotoImage(file='letra l.png'),
             PhotoImage(file='letra m.png'), PhotoImage(file='letra n.png'), PhotoImage(file='letra ne.png'), 
             PhotoImage(file='letra o.png'), PhotoImage(file='letra p.png'), PhotoImage(file='letra q.png'),
             PhotoImage(file='letra r.png'), PhotoImage(file='letra s.png'), PhotoImage(file='letra t.png'),
             PhotoImage(file='letra u.png'), PhotoImage(file='letra v.png'), PhotoImage(file='letra w.png'),
             PhotoImage(file='letra x.png'), PhotoImage(file='letra y.png'), PhotoImage(file='letra z.png')]
    label = Label(venS,image=photos[0],bg="#1e1e1e")
    label.place(x=200,y=200)
    retro=PhotoImage(file='retro.png')
    retro=retro.zoom(40)
    retro=retro.subsample(350)

    venS.mainloop()
 
def braille():
    def tra():
        trad=txt.get()
        palabra=trad
        palabra=palabra.lower()
        list(palabra)
        mostrar=[]
        for i in palabra:
    
            if i == ' ':
                espacio = ' '
                mostrar.append(espacio)

            if i == "a":
                a = '⠁'
                mostrar.append(a)
      
            if i == "b":
                b = '⠃'
                mostrar.append(b)

            if i == "c" : 
                c = '⠉'
                mostrar.append(c)

            if i == "d": 
                d = '⠙'
                mostrar.append(d)

            if i == "e": 
                e = '⠑'
                mostrar.append(e)
      
            if i == "f": 
                f = '⠋'
                mostrar.append(f)
    
            if i == "g": 
                g = '⠛'
                mostrar.append(g)

            if i == "h": 
                h = '⠓'
                mostrar.append(h)

            if i == "i": 
                i = '⠊'
                mostrar.append(i)

            if i == "j": 
                j = '⠚'
                mostrar.append(j)

            if i == "k": 
                k = '⠅'
                mostrar.append(k)

            if i == "l": 
                l = '⠇'
                mostrar.append(l)

            if i == "m":
                m = '⠍'
                mostrar.append(m)

            if i == "n": 
                n = '⠝'
                mostrar.append(n)
      
            if i == "ñ":
                ñ = '⠻'
                mostrar.append(ñ)

            if i == "o": 
                o = '⠕'
                mostrar.append(o)

            if i == "p": 
                p = '⠏'
                mostrar.append(p)

            if i == "q":
                q = '⠟'
                mostrar.append(q)

            if i == "r": 
                r = '⠗'
                mostrar.append(r)
        
            if i == "s": 
                s = '⠎'
                mostrar.append(s)

            if i == "t":
                t = '⠞'
                mostrar.append(t)

            if i == "u":
                u = '⠥'
                mostrar.append(u)

            if i == "v":
                v = '⠧'
                mostrar.append(v)

            if i == "w":
                w = '⠺'
                mostrar.append(w)

            if i == "x":
                x = '⠭'
                mostrar.append(x)

            if i == "y":
                y = '⠽'
                mostrar.append(y)

            if i == "z":
                z = '⠵'
                mostrar.append(z)

            if i == ".":
                punto = '⠲'
                mostrar.append(punto)
      
            if i == ",":
                coma = '⠂'
                mostrar.append(coma)
        cadena = " ".join(mostrar)
        return entrada.set(cadena)
    
    ven.destroy()
    venB=Tk()
    imagenf=PhotoImage(file="braille.png")
    labelFondo=Label(venB,image=imagenf)
    labelFondo.place(x=0,y=0,relwidth=1.0,relheight=1.0)
    venB.title("Traductor") 
    venB.geometry("700x600+350+120")
    venB.resizable(0,0)
    venB.iconbitmap("icono.ico")
    labelTitulo=Label(venB, text="BRAILLE",fg="white", bg="#9C9C9C", font="arial 25 italic bold").place(x=270,y=5)
    lblpalabra=Label(venB,text="digite lo que quiere traducir: ",fg="white", bg="#9C9C9C", font="arial 14 italic bold ").place(x=40,y=70)
    entrada=StringVar()
    txt = Entry(venB, font="arial 14", width=50)
    txt.place(x=40,y=120)
    btn=Button(venB, text="traducir", command=tra).place(x=540,y=70)
    lblRes=Label(venB,textvariable=entrada, font="arial 14", wraplength=600, justify=LEFT)
    lblRes.place(x=40, y=170)
    def copiar():
        resultado = entrada.get()
        pyperclip.copy(resultado)
    btn_copiar = Button(venB, text="Copiar", command=copiar)
    btn_copiar.place(x=550,y=520)
    venB.mainloop()

    
ven=Tk()
imagenf=PhotoImage(file="fondo.png")
labelFondo=Label(ven,image=imagenf)
labelFondo.place(x=0,y=0,relwidth=1.0,relheight=1.0)
ven.title("Traductor")
ven.geometry("700x600+350+120")
ven.resizable(0,0)
ven.iconbitmap("icono.ico")
imaBtn1 = Button(ven, text="señales",fg="white", font="arial 20 italic bold", bg="#711610", command=senales).place(x=170,y=460)
imaBtn2 = Button(ven, text="braille",fg="white", font="arial 20 italic bold", bg="#711610", command=braille).place(x=430,y=460)
ven.mainloop()


# In[ ]:





# In[ ]:




