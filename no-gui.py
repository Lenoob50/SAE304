#!/usr/bin/python3
import DHCP.dhcp
import STP.STP_opé

print("1->attaque_dhcp\n2->attaque_stp\n")

id = input("Saisir le numéro correspondant à l'attaque")

if id==1:
    DHCP.dhcp()