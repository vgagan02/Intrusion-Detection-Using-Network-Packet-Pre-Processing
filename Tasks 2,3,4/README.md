TASK 2: to pull ip addresses from an online threat database to a pandas or polars dataframe and subsequently use the firewall to block icmp requests from the threat ips

TASK 3: to explore various firewalls in linux and see if it's possible to convert the previous implementation(task 1) of the firewall to being statelesss

TASK 4: to preferably use scapy instead of pyshark as scapy offers more reliable support and documentation

The filesPull.py script pulls the threat ips provided by the github repository stamparm/ipsum and stores it in a polars series and returns the series.

The sniff.py script imports the filesPull module and creates a polars series. It uses the sniff method from the scapy library and uses a callback function to check whether the sniffed packets are present in the polars series and block it if they are.

Similar to task 1, the subprocess module is used to interact with the command shell and block the required ips using the iptables firewall, only difference being that it is implemented in a stateless manner by dropping the contraint to check whether the packets are new, related or established.
