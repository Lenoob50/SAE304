#!/usr/bin/python3
import utils

def no_gui():
    '''Cette fonction lance les attaques de manière non graphique'''
    #Affichage du titre
    print("  _____ _______ ___         _    _          _____ _  ________ _____ ")
    print(" |  __ \__   __|__ \  ____ | |  | |   /\   / ____| |/ /  ____|  __ \ ")
    print(" | |__) | | |     ) |/ __ \| |__| |  /  \ | |    | ' /| |__  | |__) |")
    print(" |  _  /  | |    / // / _` |  __  | / /\ \| |    |  < |  __| |  _  / ")
    print(" | | \ \  | |   / /| | (_| | |  | |/ ____ \ |____| . \| |____| | \ \ ")
    print(" |_|  \_\ |_|  |____\ \__,_|_|  |_/_/    \_\_____|_|\_\______|_|  \_\ ")
    print("                     \____/                                          ")
    #Affichage des options
    print("\nNuméro 1 -> Attaque DHCP Starvation\nNuméro 2 -> Attaque STP\nNuméro 3 -> Informations supplémentaires\n")
    # Récuperation grace à un input du type d'attque que l'utilsateur veut lancer
    id = int(input("Saisir le numéro correspondant à l'attaque :\n\n"))
    #Lancement des attaques en fonction du numéro choisi
    if id == 1:
        print("\nVous lancez l'attaque DHCP Starvation !\n")
        utils.select_int("DHCP")

    elif id == 2:
        print("\nVous lancez l'attaque STP !\n")
        utils.select_int("STP")
    elif id == 3:
        print("\nCode source et script réalisés dans le cadre de la SAE 304-Cyber\n"
              "Les étudiants en charge de ce projet sont DOREY Grégoire et CHARLES Clémence\n"
              "BUT 2A - IUT de Caen Normandie\n")
    else:
        print("\nCette action est impossible, veuillez réitérer le script afin de donner un numéro entre 1 et 3 !\n")

