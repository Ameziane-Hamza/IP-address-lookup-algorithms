from Multi_Bit_Trie import *         #le code de l'arbre
with open("100_ip_bin.txt",'r') as f:
    arbre_multi=Arbre()
    while 1:
        txt=f.readline()
        if txt == "":
            break
        elif txt[0] == "d":
            l = txt.split()
            arbre_multi.insert_default(l[1], l[2], l[0])
        else:
            l=txt.split()
            arbre_multi.insert(l[1],l[2],l[0])

