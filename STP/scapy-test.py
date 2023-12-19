#!/usr/bin/python3
from scapy.all import *
def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst= 'ff:ff:ff:ff:ff:ff')
    finalpacket = broadcast/arp_request
    answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)

get_target_mac("192.168.17.53")