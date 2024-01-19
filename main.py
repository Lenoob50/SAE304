import argparse
import gui
import no_gui
def launch(args):
    if(args=="GUI"):
        gui.gui()
    elif(args=="CLI"):
        no_gui.no_gui()

def arguments():
    parser = argparse.ArgumentParser(description="SAE 304 - Découvrir le pentesting")
    parser.add_argument('--choice','-c',type=str,required=False,help="Lancement en mode graphique ou non")
    args = parser.parse_args()
    launch(args.choice)

arguments()



