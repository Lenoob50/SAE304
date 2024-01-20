#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from scapy.all import *
from DHCP.dhcp import dhcp
from STP.stp import stp

def nyi():
    '''Cette fonction affiche une boite de dialogue d'erreur'''
    #Affichage d'une boite de dialogue avec une erreur
    msg = messagebox.showinfo("Erreur dans la matrice", "Pas encore implémenté\n Revenez plus tard ;)")

def infos():
    '''Cette fonction affiche une boite de dialogue d'information '''
    #Affichage d'une boite de dialogue avec les informations du projet
    msg = messagebox.showinfo("Informations", "\nCode source et script réalisés dans le cadre de la SAE 304-Cyber\n"
                                              "Les étudiants en charge de ce projet sont DOREY Grégoire et CHARLES Clémence\n"
                                              "BUT 2A - IUT de Caen Normandie\n")

def dhcp_window():
    '''Cette fonction lance une fenetre pour l'utilisation de l'attaque DHCP Starvation'''
    #Utilisation du module Tkinter pour crée une fenetre et appel du constructeur de la classe TK
    dhcp_win = Tk()
    #Titre de la fentre
    dhcp_win.title("RT2@hacker - DHCP")
    #Taille de la fentre
    dhcp_win.geometry("700x300")
    #Blocage du redimensionement de la fenetre
    dhcp_win.resizable(False,False)
    #Ajout de texte dans la fenetre
    label_dhcp = Label(dhcp_win,text="Attaque DHCP Starvation")
    #Placement du texte
    label_dhcp.place(x=225,y=10)
    #Récuperation de toutes les interfaces du pc
    interfaces = get_if_list()
    #Creation d'une liste deroulante avec les interface
    inet_list = Listbox(dhcp_win,height=3)
    for i in range(len(interfaces)):
        inet_list.insert(i+1,str(interfaces[i]))#Ajout des interface dans la liste deroulantes
    inet_list.place(x=20,y=30)
    def selected_int():
        '''Cette fonction permet de savoir quelle interface est selectionée'''
        int_use = ""
        for i in inet_list.curselection():
            int_use=inet_list.get(i)
        return int_use
    #Creation d'une barre de progression
    progressbar = ttk.Progressbar(dhcp_win,orient=HORIZONTAL,length=400)
    #Placement de la barre de progression
    progressbar.place(x=150, y=150)
    def launch():
        '''Cette fonction nous permet de lancer l'attaque DHCP'''
        dhcp(selected_int(),dhcp_win,progressbar)
    def update_ip():
        '''Cette fonction nous permet de rafraichir l'ip'''
        ip_display["text"]=get_if_addr(selected_int())
    #Ajout d'un bouton qui actionne la fonction launch au clique
    button = Button(dhcp_win, text="Lancer l'attaque", width=15, command=launch)
    #Placement du boutton de lancement
    button.place(x=20, y=200)
    #Affichage de l'ip de la carte réseau
    ip_display = Label(dhcp_win,text=get_if_addr(selected_int()),font=("Courier", 22))
    #Placment du label
    ip_display.place(x=250,y=50)
    #Creation d'un bouton pour rafraichir l'ip
    refresh = Button(dhcp_win,text="Rafraichir l'IP",command=update_ip)
    #Placement de du boutton
    refresh.place(x=550,y=50)
    #Lancement de la fenetre
    dhcp_win.mainloop()

def stp_window():
    '''Cette fonction lance une fenetre pour l'utilisation de l'attaque STP'''
    # Utilisation du module Tkinter pour crée une fenetre et appel du constructeur de la classe TK
    stp_win = Tk()
    #Taille de la fenetre
    stp_win.geometry("400x300")
    #Titre de la fenetre
    stp_win.title("RT2@hacker - STP")
    #Blocage du redimensionement de la fenetre
    stp_win.resizable(False, False)
    #Ajout du texte dans la fenetre
    label_stp = Label(stp_win, text="Attaque STP")
    #Placement du texte dans la fenetre
    label_stp.place(x=20, y=10)
    #recuperation de la liste des interfaces
    interfaces = get_if_list()
    #Creation d'une liste deroulante
    inet_list = Listbox(stp_win, height=3)
    for i in range(len(interfaces)):
        inet_list.insert(i + 1, str(interfaces[i]))#Ajout des interface a la liste deroulante
    inet_list.place(x=20, y=30)
    def selected_int():
        '''Cette fonction permet de savoir quelle interface est selectionée'''
        int_use = ""
        for i in inet_list.curselection():
            int_use=inet_list.get(i)
        return int_use
    def launch():
        '''Cette fonction nous permet de lancer l'attaque STP'''
        stp(selected_int())
    def stop_attaque():
        '''Cette fonction permet de stopper l'attaque STP'''
        raise StopIteration("Arret de l'attaque STP")
    #Ajout d'un texte à la fenetre
    label_error = Label(stp_win, text="Il peut y avoir des problème lors de l'utilisaion du bouton\n Stopper l'attaque")
    #Placement du texte
    label_error.place(x=20,y=150)
    #Ajout d'un bouton qui actionne la fonction launch au clique
    button = Button(stp_win, text="Lancer l'attaque", width=15, command=launch)
    #Placement du boutton
    button.place(x=20, y=200)
    # Ajout d'un bouton qui actionne la fonction stop_attaque au clique
    stop = Button(stp_win,text="Stopper l'attaque",width=15, command=stop_attaque)
    #Placement du boutton
    stop.place(x=175, y=200)
    #Lancement de la fenetre
    stp_win.mainloop()


def gui():
    '''Cette fonction lance la fenetre princapale du programme'''
    # Utilisation du module Tkinter pour crée une fenetre et appel du constructeur de la classe TK
    main = Tk()
    #Titre de la fenetre
    main.title("RT2@hacker")
    #Taille de la fentre
    main.geometry("450x250")
    #Blocage du redimensionnement de la fenetre
    main.resizable(False, False)
    #Ajout du texte dans la fenetre
    bienvenue = Label(main, text="Bienvenue, quelle attaque voulez-vous utiliser ?")
    #Placement du texte
    bienvenue.place(x=80, y=10)
    #Ajout d'un boutton
    button = Button(main, text="DHCP", width=10,command=dhcp_window)
    #Placement du boutton
    button.place(x=85, y=75)
    # Ajout d'un boutton
    button = Button(main, text="STP", width=10,command=stp_window)
    # Placement du boutton
    button.place(x=85, y=125)
    # Ajout d'un boutton
    button = Button(main, text="NYI", width=10, command=nyi)
    # Placement du boutton
    button.place(x=225, y=75)
    # Ajout d'un boutton
    button = Button(main, text="NYI", width=10, command=nyi)
    # Placement du boutton
    button.place(x=225, y=125)
    # Ajout d'un boutton
    button = Button(main, text="INFOS", width=10, command=infos)
    # Placement du boutton
    button.place(x=150, y=175)
    #Lancement de la fenetre
    main.mainloop()
