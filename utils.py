from scapy.all import *
import DHCP
import STP
def select_int(attaque):
    '''Cette fonction permet de choisir quel interface on va utiliser lors de l'attaque
    attaque ->str'''
    iface_list = get_if_list()#recuperation des interface du pc
    for i in range(len(iface_list)):
        print(str(i+1)+" - "+iface_list[i])#Affichage des interfaces
    choice = int(input("\nVeuillez choisir une interface réseau sur laquelle envoyé l'attaque\n \n")) #Recuperation de l'interface grace à un input
    print("\n")
    if(attaque=="DHCP"):
        DHCP.dhcp.dhcp_no_gui(str(iface_list[choice-1])) #Lancement de l'attaque DHCP avec l'interface choisi par l'utilisateur
    elif(attaque=="STP"):
        STP.stp.stp(str(iface_list[choice-1])) #Lancement de l'attaque STP avec l'interface choisi par l'utilisateur
