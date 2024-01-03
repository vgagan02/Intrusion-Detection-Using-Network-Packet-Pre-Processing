import polars as pl
import requests
import ipaddress
url="https://github.com/stamparm/ipsum/raw/master/levels"
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
def createDataFrame(url):
        ans=[]
        for i in range(1,9):
                urlnew=url+"/"+str(i)+".txt"
                response=requests.get(urlnew)
                data=response.text.split('\n')
                for i in data:
                        ip=i.strip()
                        if is_valid_ip(ip):
                                ans.append(ip)
        ans.append("14.139.181.236")
        df=pl.Series("malicious_ips",ans)
        return df
        
