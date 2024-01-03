This code aims at blocking icmp protocols coming from a specific ip address specified by the user.

It uses the pyshark module(the python module of tshark) and its LiveCapture method to sniff live requests and responses going to and fro the user's interface.

It uses the inbuilt firewall of ubuntu, iptables to block the specified ip address if it is found and it is implemented using the in-built subprocess module, which helps in interacting with the command shell.
