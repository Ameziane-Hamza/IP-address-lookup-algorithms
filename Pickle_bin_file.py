import pickle
from MyFunctions import *
import random
f =open('pickle_bin_file.txt', 'wb')
for i in range(1,101):
    route = "P" + str(i)
    ip = ip_generate()
    mask = subnet_mask()
    s = route + (20 - len(route)) * " " + ip + (20 - len(ip)) * " " + mask + (20 - len(mask)) * " " + random.choice(["S1", "S2", "S3", "S4"])
    pickle.dump(s, f)
    pickle.dump("\n",f)
f.close()