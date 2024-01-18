from tkinter import *
from tkinter import messagebox
from scapy.all import *
from DHCP.dhcp import dhcp


def nyi():
    msg = messagebox.showinfo("Erreur dans la matrice", "Pas ecnore implémenté\n Revenez plus tard ;)")



def dhcp_window():
    dhcp_win = Tk()
    dhcp_win.title("RT2@hacker - DHCP")
    dhcp_win.geometry("600x300")
    dhcp_win.resizable(False,False)
    label_dhcp = Label(dhcp_win,text="Attaque DHCP Starvation")
    label_dhcp.place(x=225,y=10)
    interfaces = get_if_list()
    inet_list = Listbox(dhcp_win,height=3)
    for i in range(len(interfaces)):
        inet_list.insert(i+1,str(interfaces[i]))
    inet_list.place(x=20,y=30)
    def selected_int():
        int_use = ""
        for i in inet_list.curselection():
            int_use=inet_list.get(i)
        return int_use
    def launch():
        dhcp(selected_int())
    button = Button(dhcp_win, text="Lancer l'attaque", width=15, command=launch)
    button.place(x=20, y=200)
    dhcp_win.mainloop()



dhcp_window()
def gui():
    main = Tk()
    main.title("RT2@hacker")
    main.geometry("800x500")
    main.resizable(False, False)
    bienvenue = Label(main, text="Bienvenue, quelle attaque voulez-vous utiliser ?")
    bienvenue.place(x=80, y=10)
    button = Button(main, text="DHCP", width=10)
    button.place(x=85, y=75)
    button = Button(main, text="STP", width=10)
    button.place(x=85, y=125)
    button = Button(main, text="NYI", width=10, command=nyi)
    button.place(x=225, y=75)
    button = Button(main, text="NYI", width=10, command=nyi)
    button.place(x=225, y=125)
    button = Button(main, text="INFOS", width=10)
    button.place(x=150, y=175)
    main.mainloop()



def stp_window():
    pass


