from Binary_tree import *         #le code de l'arbre
with open("100_ip_bin.txt",'r') as f:
    arbre_bin=Creatarbre()
    while 1:
        txt=f.readline()
        if txt == "":
            break
        elif txt[0] == "d":
            l = txt.split()
            arbre_bin.insert_default(l[1], l[0], l[2])
        else:
            l=txt.split()
            arbre_bin.insert(l[1],l[0],l[2])
