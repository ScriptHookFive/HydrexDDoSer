import requests
import os
import socket
import ipaddress

hydrex = "\033[38;5;196m"
red = "\033[38;5;196m"
clear = "\033[0m"
lila = "\033[38;5;165m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
 Created by {lila}Hydrex{clear}     |{hydrex} Copyright {clear}| 
          {hydrex}
               __________  ____  __   ____
              /_  __/ __ \/ __ \/ /  / __/
               / / / /_/ / /_/ / /___\ \  
              /_/  \____/\____/____/___/  
                                  {clear}
                         By Hydrex
           {hydrex}╔═══════════════════════════════════╗{clear}
           {hydrex}║{clear}  {hydrex}-{clear} geoip   {hydrex}|{clear} geolocation ip       {hydrex}║{clear}         
           {hydrex}║{clear}  {hydrex}-{clear} dns     {hydrex}|{clear} DNS lockup           {hydrex}║{clear}
           {hydrex}║{clear}  {hydrex}-{clear} subnet  {hydrex}|{clear} Reverse DNS lockup   {hydrex}║{clear}
           {hydrex}╚═══════════════════════════════════╝{clear}

""")              
    
def tools():
    while True:
        banner()
        select = input(f"""
╔═══[{hydrex}type{clear}@{hydrex}Hydrex{clear}]
╚══{hydrex}>{clear} """)
                                        
        if select.startswith("geoip"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{hydrex}:{clear} {hydrex}geoip{clear} <{hydrex}ip{clear}>")
                input()
                continue

            ip = parts[1]

            def geoip():
                r = requests.get(f"http://ip-api.com/json/{ip}")
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"""
            {hydrex}╔══════════════════════════════════{clear}
            {hydrex}║{clear} IP{hydrex}:{clear} {hydrex}[{clear}{r.json().get("query")}{hydrex}]{clear}              
            {hydrex}║{clear} Country{hydrex}:{clear} {hydrex}[{clear}{r.json().get("country")}{hydrex}]{clear}        
            {hydrex}║{clear} Region{hydrex}:{clear} {hydrex}[{clear}{r.json().get("regionName")}{hydrex}]{clear}       
            {hydrex}║{clear} City{hydrex}:{clear} {hydrex}[{clear}{r.json().get("city")}{hydrex}]{clear}               
            {hydrex}║{clear} ISP{hydrex}:{clear} {hydrex}[{clear}{r.json().get("isp")}{hydrex}]{clear}        
            {hydrex}║{clear} Latitude{hydrex}:{clear} {hydrex}[{clear}{r.json().get("lat")}{hydrex}]{clear}               
            {hydrex}║{clear} Longitude{hydrex}:{clear} {hydrex}[{clear}{r.json().get("lon")}{hydrex}]{clear}        
            {hydrex}║{clear} ZIP{hydrex}:{clear} {hydrex}[{clear}{r.json().get("zip")}{hydrex}]{clear}                     
            {hydrex}╚══════════════════════════════════{clear}
                      """)
                input()

            geoip()

        elif select.startswith("dns"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{hydrex}:{clear} {hydrex}dns{clear} <{hydrex}domain{clear}>")
                input()
                continue

            host = parts[1]

            def dnslockup():
                try:
                    dns = socket.gethostbyname(host)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
            {hydrex}╔══════════════════════════════════{clear}
            {hydrex}║{clear} HOST{hydrex}:{clear} {hydrex}[{clear}{host}{hydrex}]{clear}              
            {hydrex}║{clear} DNS{hydrex}:{clear} {hydrex}[{clear}{dns}{hydrex}]{clear}          
            {hydrex}╚══════════════════════════════════{clear}
                    """)
                except socket.gaierror:
                    pass
                input()

            dnslockup()


        elif select.startswith("subnet"):
            parts = select.split()
            if len(parts) != 2:
                print(f"usage{hydrex}:{clear} {hydrex}subnet{clear} <{hydrex}ip{clear}>")
                input()
                continue

            ip = parts[1]

            def subnet():
                try:
                    n = ipaddress.ip_network(ip + "/24", strict=False)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"""
                {hydrex}╔════════════════════════════════════════════════╗{clear}
                {hydrex}║{clear} IP       {hydrex}:{clear} [{ip}]
                {hydrex}║{clear} SUBNET   {hydrex}:{clear} [{n}]
                {hydrex}║{clear} NET ADDR {hydrex}:{clear} [{n.network_address}]
                {hydrex}║{clear} BROADCAST{hydrex}:{clear} [{n.broadcast_address}]
                {hydrex}║{clear} NETMASK  {hydrex}:{clear} [{n.netmask}]
                {hydrex}║{clear} HOSTS    {hydrex}:{clear} [{n.num_addresses}] addresses
                {hydrex}╚════════════════════════════════════════════════╝{clear}
                    """)
                except Exception:
                    pass

                input()

            subnet()

if __name__ == "__main__":
    tools()


