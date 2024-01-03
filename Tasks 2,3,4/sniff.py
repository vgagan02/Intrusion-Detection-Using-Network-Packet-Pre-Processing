from scapy.all import *
from filesPull import *
import subprocess
url="https://github.com/stamparm/ipsum/raw/master/levels"
interface="ens33"
data=createDataFrame(url)
def pkt_callback(pkt):
    if IP in pkt:
        address=[pkt[IP].src,pkt[IP].dst]
        for i in address:
                if i in data:
                        try:
                            rule = f"iptables -A INPUT -i {interface} -s {i} -p icmp -m state --state NEW,RELATED,ESTABLISHED -j DROP"
                            subprocess.run(rule,shell = True,check = True)
                            print(f"Blocked icmp from {i}")
                                
                        except subprocess.CalledProcessError as e:
                                print(f"Error blocking icmp traffic:{e}")
         # debug statement

sniff(iface="ens33", prn=pkt_callback, filter="icmp", store=0)
