with open("ip_address.txt",'r') as f:
    f.readline()
    with open("ip_address_bin.txt",'w') as f2:
        while 1 :
            s=f.readline()
            if s == "":
                break
            else:
                l = s.split()
                m= l[1].split("/")
                mask=int(m[1])
                ###### convert ip address to binary
                net=m[0].split(".")
                net_bin = ""
                for a in net:
                    x = bin(int(a))
                    x = x[2:]
                    for i in range(8 - len(x)):
                        x = "0" + x
                    net_bin += x
                net_bin=net_bin[:mask]+"*"
                ######## write route P
                f2.write(l[0])
                f2.write((10-len(l[0]))*" ")
                ######## write ip address of th destination
                f2.write(net_bin)

                f2.write((35-len(net_bin))*" ")
                ######### write the interface
                f2.write(l[3])
                ########## retour à la ligne
                f2.write("\n")
