
from tkinter import *
import os
#from from_txt_to_multi_tree import *
#from from_txt_to_tree import *


#interface 1
fen1 = Tk()

fen1.title("projet de lookup ")
fen1.geometry("600x300")
fen1.config(background='#092452')

fen1.minsize(600, 300)
fen1.maxsize(610, 310)
frame = Frame(fen1, bg='#092452', bd=1, relief=SUNKEN)
ensa=PhotoImage(file="ensa.png")
logo=Label(fen1,image=ensa)
logo.place(x=500,y=20)


def nouvfen():
    os.system("python 100_ip_bin.py")         #Pour Linux os.system("python3 file.py")
    os.system("python ip_address_bin.py")
    os.system("python from_txt_to_multi_tree.py")
    os.system("python from_txt_to_tree.py")
    os.system("python from_txt_to_tree_class.py")
    os.system("python from_txt_to_tree_class.py")

    #on supp linterface 1 et on creee linterface 2
    get_i=i.get()
    fen1.destroy()
    fen2 = Tk()
    fen2.title("projet de lookup ")
    fen2.geometry("600x300")
    fen2.config(background='#092452')
    fen2.minsize(600, 300)
    fen2.maxsize(610, 310)
    ensa = PhotoImage(file="ensa.png")
    logo = Label(fen2, image=ensa)
    logo.place(x=500, y=20)
    def quit():
        fen2.destroy()
    global l1
    global l4
    global l2
    l1= Label()
    l4= Label()
    l2= Label()
    def chercher():
        global l1
        global l4
        global l2
        if l1 != None:
            l1.destroy()
            l4.destroy()
            l2.destroy()
        ###############################################
        l7 = Label(fen2, text="Route", bg='#092452', fg="#FFFFFF")
        l7.place(x=20, y=200)
        l8 = Label(fen2, text="Destination", bg='#092452', fg="#FFFFFF")
        l8.place(x=80, y=200)
        l9 = Label(fen2, text="Interface", bg='#092452', fg="#FFFFFF")
        l9.place(x=190, y=200)
        ###############################################
        addr = txt7.get()
        ####### Split address and mask
        m = addr.split("/")
        mask = int(m[1])
        ######### Split the address to bytes
        net = m[0].split(".")
        net_bin = ""
        ########## Convert each byte to binary and append it
        for a in net:
            x = bin(int(a))
            x = x[2:]
            for i in range(8 - len(x)):
                x = "0" + x
            net_bin += x
        net_bin = net_bin[:mask] + "*"

        
        if j.get() == 1:
            ############ MultiBit Tree
            ########## Depends on the type chosen file
            if get_i == 1:
                import from_txt_to_multi_tree as multi_tree
            if get_i == 2:
                import from_txt_to_multi_tree_class as multi_tree

            k = multi_tree.arbre_multi.find(net_bin)

            if type(k) == type(tuple()):
                k=k[0]

            if k["route"] != "default":
                if get_i == 1:
                    l1 = Label(fen2, text=k["route"][:3], bg='#092452', fg="#FFFFFF")
                if get_i == 2:
                    l1 = Label(fen2, text=k["route"][0], bg='#092452', fg="#FFFFFF")
                l4 = Label(fen2, text=addr, bg='#092452', fg="#FFFFFF")
            else:
                l1 = Label(fen2, text=k["route"], bg='#092452', fg="#FFFFFF")
                l4 = Label(fen2, text=k["destination"], bg='#092452', fg="#FFFFFF")
            l1.place(x=20, y=220)
            l4.place(x=80, y=220)
            l2 = Label(fen2, text=k["interface"], bg='#092452', fg="#FFFFFF")
            l2.place(x=190, y=220)

        elif j.get() == 2:
            ########## Binary Tree
            ########## Depends on the type chosen file
            if get_i == 1:
                import from_txt_to_tree as bin_tree
            if get_i == 2:
                import from_txt_to_tree_class as bin_tree

            k = bin_tree.arbre_bin.lookup(net_bin)
            l1 = Label(fen2, text=k["route"], bg='#092452', fg="#FFFFFF")
            l1.place(x=20, y=220)
            if k["route"] != "default":
                l4 = Label(fen2, text=addr, bg='#092452', fg="#FFFFFF")
            else:
                l4 = Label(fen2, text=k["destination"], bg='#092452', fg="#FFFFFF")
            l4.place(x=80, y=220)
            l2 = Label(fen2, text=k["interface"], bg='#092452', fg="#FFFFFF")
            l2.place(x=190, y=220)


    def dessiner():
        if j.get() == 1:
            if get_i ==1:
                os.system("python Multi_Bit_Trie_Graph.py")  #Pour Linux os.system("python3 file.py")
            if get_i==2:
                os.system("python Multi_Bit_Trie_Graph_Class.py")
        elif j.get() == 2:
            if get_i ==1:
                os.system("python Binary_Tree_Graph.py")
            if get_i ==2:
                os.system("python Binary_Tree_Graph_Class.py")



    txt4 = Label(fen2, text="ALGORITHME ", font=("courrier", 17), fg="#FFFFFF")
    txt4.config(background='#092452')
    txt4.place(x=180, y=10)
    entr4 = Entry(fen2)
    txt5 = Label(fen2, text="Choisissez", font=("courrier", 13), fg="#FFFFFF")
    txt5.config(background='#092452')
    txt5.place(x=60, y=90)
    entr5 = Entry(fen2)
    txt6 = Label(fen2, text="Enterz l'@ip", font=("courrier", 13), fg="#FFFFFF")
    txt6.config(background='#092452')
    txt6.place(x=60, y=130)
    entr6 = Entry(fen2)
    txt7 = Entry(fen2, text="Entrez l'@ip", font=("courrier", 13), fg="#FFFFFF")
    txt7.config(background='#092452')
    txt7.place(x=195, y=130)
    entr7 = Entry(fen2)

    j=IntVar()
    r3 =Radiobutton(fen2 ,text="MULTIBIT TRIE", value=1,variable=j)
    r4 =Radiobutton(fen2 , text="BINARY TRIE",value=2,variable=j)
    r3.place(x=195, y=90)
    r4.place(x=310, y=90)
    bou4 = Button(fen2, text='chercher',command=chercher)
    bou3 = Button(fen2, text="DESSINER L'ARBRE",command=dessiner)
    bou3.place(x=195, y=250)
    bou4.place(x=195, y=160)

    bou1 = Button(fen2, text='Quitter', command=quit)
    bou1.place(x=550, y=270)
    bou1.config(background='#A83417')
    fen2.mainloop()


def click_me():
    if i.get() == 1:
        os.system("python 100_ip.py")         #Pour Linux os.system("python3 file.py")
    elif i.get() == 2:
        os.system('python ip_address.py')
    txt6 = Label(fen1, text="✔")
    txt6.config(background='#A83417')
    txt6.place(x=350, y=145)
    entr6 = Entry(fen1)


def show_file():
    if i.get() == 1:
        os.system("100_ip.txt")         #Pour Linux os.system("gedit file.txt")
    elif i.get() == 2:
        os.system("ip_address.txt")


txt6 = Label(fen1, text="TYPE d'@ :", font=("courrier", 13), fg="#FFFFFF")
txt6.config(background='#092452')
txt6.place(x=60, y=90)
entr6 = Entry(fen1)
txt3 = Label(fen1, text="TABLE D'ADRESSE", font=("courrier", 17), fg="#FFFFFF")
txt3.config(background='#092452')
txt3.place(x=180, y=10)
entr3 = Entry(fen1)

entr1 = Entry(fen1)

i=IntVar()
r1=Radiobutton(fen1,text="CLASSLESS",value=1,variable=i)
r2=Radiobutton(fen1,text="CLASSFULL",value=2,variable=i)
r1.place(x=210, y=90)
r2.place(x=300, y=90)
bou3 = Button(fen1, text='GENERER LA TABLE ', command=click_me)
bou3.configure(bg='#BED1F1')

bou4 = Button(fen1, text='AFFICHER LA TABLE', command=show_file)
bou4.configure(bg='#BED1F1')
bou4.place(x=210, y=190)
bou3.place(x=210, y=140)



bou1 = Button(fen1, text='suivant', command=nouvfen)

bou1.place(x=550, y=270)
bou1.config(background='#A83417')

fen1.mainloop()
