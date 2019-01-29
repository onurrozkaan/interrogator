from assets.styling.colors import  *
import sys

banner = yellow + """ 
  _       _                                  _             
 (_)     | |                                | |            
  _ _ __ | |_ ___ _ __ _ __ ___   __ _  __ _| |_ ___  _ __ 
 | | '_ \| __/ _ \ '__| '__/ _ \ / _` |/ _` | __/ _ \| '__|
 | | | | | ||  __/ |  | | | (_) | (_| | (_| | || (_) | |   
 |_|_| |_|\__\___|_|  |_|  \___/ \__, |\__,_|\__\___/|_|   
                                  __/ |                    
                                 |___/                     
 """
contact = green + """                                                                   
      ███████████████████████████████████████████████████╗
      ██╔══════════════════════════════════════════════██║
      ██║                                              ██║
      ██║       Website: http://onurozkan.work         ██║
      ██║       E-Mail: Contact@onurozkan.work         ██║
      ██║     Github: http://github.com/onurrozkaan    ██║
      ██║                                              ██║
      ██║                                              ██║
      ╚█████████████████████████████████████████████████╔╝ 
       ╚════════════════════════════════════════════════╝

"""

def banner_printer():
    sys.stdout.write(banner)
    sys.stdout.write(contact)