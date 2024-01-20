#!/usr/bin/python3
import argparse
import gui
import no_gui
def launch(args):
    '''Cette fonction permet de determiner quel argument à été lancé lors de l'appel du script'''
    if(args=="GUI"):
        gui.gui() #Lancement du programme en manière graphique en utilisant la fonction gui()
    elif(args=="CLI"):
        no_gui.no_gui() #Lancement du programme en manière non graphique en utilisant la fonction cli()
    else:
        raise AttributeError("Merci de préciser un argument valide -c {GUI/CLI} ") #Leve une exception si jamais aucun argument n'est passé

def arguments():
    '''Cette fonction crée les arguments lors de l'appel du script'''
    parser = argparse.ArgumentParser(description="SAE 304 - Découvrir le pentesting") #Creation des arguments en utilisant la classe ArgumentParser
    parser.add_argument('--choice','-c',type=str,required=False,help="Lancement en mode graphique ou non") #Ajout de l'argument -c
    args = parser.parse_args() # Parsage des arguments
    launch(args.choice) #Lancement de la fonction launch avec la valeur de l'argument -c

arguments()



