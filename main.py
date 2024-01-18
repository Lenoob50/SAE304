import argparse
import gui
def launch(args):
    if(args!=None):
        gui()
    else:
        pass
def arguments():
    parser = argparse.ArgumentParser(description="SAE 304 - Découvrir le pentesting")
    parser.add_argument('--no-gui','-n',type=str,required=False,help="Lancement en mode graphique ou non")
    args = parser.parse_args()
    launch(args.no_gui)

arguments()



