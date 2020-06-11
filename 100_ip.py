from MyFunctions import *
import random
with open("100_ip.txt",'w') as f:
    print("route"+15*" "+"destination"+9*" "+"netmask"+13*" "+"interface",file=f)
    for i in range(1,101):
        route="P"+str(i)
        ip=ip_generate()
        mask=subnet_mask()
        s=route+(20-len(route))*" "+ip+(20-len(ip))*" "+mask+(20-len(mask))*" "+random.choice(["S1","S2","S3","S4"])
        print(s,file=f)
    s = "default" + 13 * " " + "0.0.0.0/0" + 11 * " " + "0.0.0.0" + 13 * " " + random.choice(["S1", "S2", "S3"])
    print(s, file=f)