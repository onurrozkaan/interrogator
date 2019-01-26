from assets.styling.colors import  *
import sys

banner = yellow + """ 

       _               _       
      (_)             | |      
 _ __  _ _ __ ___   __| | __ _ 
| '_ \| | '_ ` _ \ / _` |/ _` |
| | | | | | | | | | (_| | (_| |
|_| |_|_|_| |_| |_|\__,_|\__,_|
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
splitter = red + """
• • • • • • • • • • • • • • • • • • • • • • • • • • • • • 

"""

def banner_printer():
    sys.stdout.write(banner)
    sys.stdout.write(contact)
    sys.stdout.write(splitter)