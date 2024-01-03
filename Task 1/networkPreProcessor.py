import subprocess
import pyshark

interface = "ens33"
ip_Blocked = "8.8.8.8"
 
def blocked(ip_address):
        try:
                rule = f"iptables -A INPUT -i {interface} -s {ip_address} -p icmp -j DROP"
                subprocess.run(rule,shell = True,check = True)
                print(f"Blocked icmp from {ip_address}")
                
        except subprocess.CalledProcessError as e:
                print(f"Error blocking icmp traffic:{e}")

def catchAndBlockICMP():
        cap=pyshark.LiveCapture(interface=interface,display_filter = "icmp and ip.src == " + ip_Blocked)
        print(f"listening to icmp traffic from {ip_Blocked}")
        
        for i in cap.sniff_continuously():
                print("ICMP traffic detected, blocking..")
                blocked(ip_Blocked)
 
if __name__ == "__main__":
        catchAndBlockICMP()
