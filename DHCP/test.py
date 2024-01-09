from scapy.all import *
ip = get_if_addr("enxa0cec8f3e4df")
liste = ip.split(".")
liste.pop(3)
ip_str = ""
for i in range(len(liste)):
    if(i!=0):
        ip_str = (ip_str + "." + liste[i])
    else:
        ip_str = (ip_str+ liste[i])
for j in range(0,256):
    liste = ip.split(".")
    liste.pop(3)
    str_vide = ""
    new = ip_str+str_vide+ "."+str(j)
    print(new)