#!/usr/bin/python3
import DHCP.dhcp
import STP.stp

print("Numéro 1 -> Attaque DHCP Starvation\nNuméro 2 -> Attaque STP\n\nNuméro 3 -> Informations supplémentaires")

id = int(input("Saisir le numéro correspondant à l'attaque :\n"))

if id==1:
    print("Vous lancez l'attaque DHCP Starvation !")
    '''DHCP.dhcp_no_gui("eno1")'''
if id==2:
    print("Vous lancez l'attaque STP !")
    '''STP.stp()'''
if id==3:
    print("Voici les informations")
else:
    print("Cette action est impossible")