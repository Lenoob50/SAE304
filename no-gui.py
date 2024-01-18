#!/usr/bin/python3
import DHCP.dhcp
import STP.stp

print("Numéro 1 -> Attaque DHCP Starvation\nNuméro 2 -> Attaque STP\nNuméro 3 -> Informations supplémentaires")
print("  _____ _______ ___         _    _          _____ _  ________ _____ ")
print(" |  __ \__   __|__ \  ____ | |  | |   /\   / ____| |/ /  ____|  __ \ ")
print(" | |__) | | |     ) |/ __ \| |__| |  /  \ | |    | ' /| |__  | |__) |")
print(" |  _  /  | |    / // / _` |  __  | / /\ \| |    |  < |  __| |  _  / ")
print(" | | \ \  | |   / /| | (_| | |  | |/ ____ \ |____| . \| |____| | \ \ ")
print(" |_|  \_\ |_|  |____\ \__,_|_|  |_/_/    \_\_____|_|\_\______|_|  \_\ ")
print("                     \____/                                          ")

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