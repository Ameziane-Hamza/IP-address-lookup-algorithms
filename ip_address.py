from MyFunctions import *
import random
d=0
with open("ip_address.txt",'w') as f:
    print("Type"+17*" "+"destination"+9*" "+"netmask"+13*" "+"interface",file=f)
    while d<500:
        ip = ip_generate('A')
        mask = subnet_mask()
        s = "A" + 20 * " " + ip + (20 - len(ip)) * " " + mask + (20 - len(mask)) * " " + random.choice(["S1", "S2", "S3", "S4"])
        print(s, file=f)
        if d < 300:
            ip = ip_generate('B')
            mask = subnet_mask()
            s = "B" + 20 * " " + ip + (20 - len(ip)) * " " + mask + (20 - len(mask)) * " " + random.choice(["S1", "S2", "S3", "S4"])
            print(s, file=f)
        if d < 200:
            ip = ip_generate('C')
            mask = subnet_mask()
            s = "C" + 20 * " " + ip + (20 - len(ip)) * " " + mask + (20 - len(mask)) * " " + random.choice(["S1", "S2", "S3", "S4"])
            print(s, file=f)
        d+=1

    s = "default" + 14 * " " + "0.0.0.0/0"+ 11 * " " + "0.0.0.0" + 13 * " " + random.choice(["S1", "S2", "S3"])
    print(s, file=f)