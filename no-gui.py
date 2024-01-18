#!/usr/bin/python3
import DHCP.dhcp
import STP.stp

print("  _____ _______ ___         _    _          _____ _  ________ _____ ")
print(" |  __ \__   __|__ \  ____ | |  | |   /\   / ____| |/ /  ____|  __ \ ")
print(" | |__) | | |     ) |/ __ \| |__| |  /  \ | |    | ' /| |__  | |__) |")
print(" |  _  /  | |    / // / _` |  __  | / /\ \| |    |  < |  __| |  _  / ")
print(" | | \ \  | |   / /| | (_| | |  | |/ ____ \ |____| . \| |____| | \ \ ")
print(" |_|  \_\ |_|  |____\ \__,_|_|  |_/_/    \_\_____|_|\_\______|_|  \_\ ")
print("                     \____/                                          ")

print("\nNuméro 1 -> Attaque DHCP Starvation\nNuméro 2 -> Attaque STP\nNuméro 3 -> Informations supplémentaires\n")

id = int(input("Saisir le numéro correspondant à l'attaque :\n\n"))

if id==1:
    print("\nVous lancez l'attaque DHCP Starvation !\n")
    '''DHCP.dhcp_no_gui("eno1")'''
elif id==2:
    print("\nVous lancez l'attaque STP !\n")
    '''STP.stp()'''
elif id==3:
    print("\nCode source et script réalisés dans le cadre de la SAE 304-Cyber\n"
          "Les étudiants en charge de ce projet sont DOREY Grégoire et CHARLES Clémence\n"
          "BUT 2A - IUT de Caen Normandie\n")
else:
    print("\nCette action est impossible")
