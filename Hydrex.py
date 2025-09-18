import os
import webbrowser
import subprocess
from methods.l4 import *
from methods.l7 import *
from Tools.main import *

hydrex = "\033[38;5;196m"
white = "\033[97m"
red = "\033[38;5;196m"
clear = "\033[0m"

def hydrexX():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    abs_path = os.path.abspath('Website/hydrexX.html')
    url = f'file:///{abs_path.replace("\\", "/")}'
    webbrowser.get(chrome_path).open(url)

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
 Created by {lila}Hydrex{clear}     |{hydrex} Copyright {clear}| 
          {hydrex}
         __ __        __           
        / // /_ _____/ /________ __
       / _  / // / _  / __/ -_) \ / 
      /_//_/\_, /\_,_/_/  \__/_\_\ 
           /___/                   {clear}

   +---------------------------------+
   | Type "{hydrex}help{clear}" to see all commands |
   +---------------------------------+
""")

def main():
    while True:
        banner()
        select = input(f"""
╔═══[{hydrex}type{clear}@{hydrex}Hydrex{clear}]
╚══{hydrex}>{clear} """)
        
        if select == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
 Created by {lila}Hydrex{clear}     |{hydrex} Copyright {clear}| 
          {hydrex}
                  __ __   __  
                 / // /__ / /__ 
                / _  / -_) / _ \\
               /_//_/\\__/_/ .__/
                         /_/    {clear}
              
                      By Hydrex
        {hydrex}╔═════════════════════════════════╗{clear}
        {hydrex}║{clear}  {hydrex}-{clear} l4     {hydrex}|{clear} Layer4 DDoS         {hydrex}║{clear}         
        {hydrex}║{clear}  {hydrex}-{clear} l7     {hydrex}|{clear} Layer7 DDoS         {hydrex}║{clear}
        {hydrex}║{clear}  {hydrex}-{clear} tools  {hydrex}|{clear} Tools Menu          {hydrex}║{clear}
        {hydrex}║{clear}  {hydrex}-{clear} hydrex {hydrex}|{clear} Hydrex Website      {hydrex}║{clear}
        {hydrex}╚═════════════════════════════════╝{clear}
                  """)
            input()


        elif select == "l4":
            layer4()

        
        elif select == "l7":
            layer7()

        elif select == "tools":
            tools()
            
        elif select == "hydrex":
            hydrexX()

            
    
             


if __name__ == "__main__":
    main()



