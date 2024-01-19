from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from scapy.all import *
from DHCP.dhcp import dhcp
from STP.stp import stp

def nyi():
    msg = messagebox.showinfo("Erreur dans la matrice", "Pas encore implémenté\n Revenez plus tard ;)")

def infos():
    msg = messagebox.showinfo("Informations", "\nCode source et script réalisés dans le cadre de la SAE 304-Cyber\n"
                                              "Les étudiants en charge de ce projet sont DOREY Grégoire et CHARLES Clémence\n"
                                              "BUT 2A - IUT de Caen Normandie\n",)

def dhcp_window():
    dhcp_win = Tk()
    dhcp_win.title("RT2@hacker - DHCP")
    dhcp_win.geometry("700x300")
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
    progressbar = ttk.Progressbar(dhcp_win,orient=HORIZONTAL,length=400)
    progressbar.place(x=150, y=150)
    def launch():
        dhcp(selected_int(),dhcp_win,progressbar)
    def update_ip():
        ip_display["text"]=get_if_addr(selected_int())
    button = Button(dhcp_win, text="Lancer l'attaque", width=15, command=launch)
    button.place(x=20, y=200)
    ip_display = Label(dhcp_win,text=get_if_addr(selected_int()),font=("Courier", 22))
    ip_display.place(x=250,y=50)
    refresh = Button(dhcp_win,text="Rafraichir l'ip",command=update_ip)
    refresh.place(x=550,y=50)
    dhcp_win.mainloop()

def stp_window():
    stp_win = Tk()
    stp_win.title

def gui():
    main = Tk()
    main.title("RT2@hacker")
    main.geometry("450x250")
    main.resizable(False, False)
    bienvenue = Label(main, text="Bienvenue, quelle attaque voulez-vous utiliser ?")
    bienvenue.place(x=80, y=10)
    button = Button(main, text="DHCP", width=10,command=dhcp_window)
    button.place(x=85, y=75)
    button = Button(main, text="STP", width=10)
    button.place(x=85, y=125)
    button = Button(main, text="NYI", width=10, command=nyi)
    button.place(x=225, y=75)
    button = Button(main, text="NYI", width=10, command=nyi)
    button.place(x=225, y=125)
    button = Button(main, text="INFOS", width=10, command=infos)
    button.place(x=150, y=175)
    main.mainloop()





