from ipaddress import *
from random import *
###################Random IP address generator###################################
def ip_generate(type=None):
    "Generate random ip address"
    global mask
    if type == 'A':
        addr=str(randint(1,126))+".0.0.0"
        mask = 8
        addr_net = IPv4Network(addr + "/" + str(mask), strict=False)
        return str(addr_net.network_address) + "/" + str(mask)

    elif type == 'B':
        addr = str(randint(128, 191)) +"."+ str(randrange(1, 256)) + ".0.0"
        mask = 16
        addr_net = IPv4Network(addr + "/" + str(mask), strict=False)
        return str(addr_net.network_address) + "/" + str(mask)

    elif type == 'C':
        addr = str(randint(192, 223)) +"."+ str(randrange(0, 256)) +"."+ str(randrange(0, 256)) +".0"
        mask = 24
        addr_net = IPv4Network(addr + "/" + str(mask), strict=False)
        return str(addr_net.network_address) + "/" + str(mask)

    elif type == None:
        a = getrandbits(32)
        addr = str(IPv4Address(a))
        mask = randint(1, 32)
        addr_net = IPv4Network(addr + "/" + str(mask), strict=False)
        return str(addr_net.network_address) + "/" + str(mask)



####################Random subnet mask generator###################################
def subnet_mask():
    "Generate randome subnet mask"
    k=mask
    x=int(k/8)
    y=k%8
    l=[]
    #L'ajout des octets 255 du partie net-id
    for i in range(x):
        l.append("255")
    #L'octet de la separation du masque
    if y != 0:
        a=0
        for i in range(y):
            a+=2**(7-i)
        l.append(str(a))
    #L'ajout des octets 0 du partie host-id
    while len(l) < 4:
        l.append("0")
    addr=".".join(l)
    return addr
