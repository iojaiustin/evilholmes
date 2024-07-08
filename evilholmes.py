import requests
import re
import argparse
import os
import sys
import cyberscout


parser = argparse.ArgumentParser(
                    prog='evilholmes.py',
                    description='''\033[94m Cyber Threat Intelligence tool. \033[00m
                      Search your credentials on both darkweb and clearweb to see your exposure to potential cyber attacks.
                      ''')

parser.add_argument('query',help='Enter your keyword here')
#parser.add_argument('-h','--help')

args = parser.parse_args()
query = args.query

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def printRed(text):
        print("\033[91m {}\033[00m" .format(text))

def printPurple(text):
        print("\033[95m {}\033[00m".format(text))

def print_logo():
        print('''
                             &@&*     (&@%                            
                            @@@@@@@@@@@@@@%                           
                           *@@@@@@@@@@@@@@@                           
                           @@@@@@@@@@@@@@@@(                          
                 ,%&&&%&@@,@@@@@@@@@@@@@@@@@*@@&%&&&#.                
                #@@@@@@@@%        ...        @@@@@@@@@.               
                 /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                
                     ./&@@@@@@@@@@@@@@@@@@@@@@@%*                     
                    &@@@@*/@@@@&&%%##%%&@@@@.&@@@@(                   
                 %@@@@@@@@ .@@@@@(   &@@@@& ,@@@@@@@@*                
                #@@@@@@@@@@                 @@@@@@@@@@.               
                  %@@@@@@@@@              (@@@@@@@@@/                 
                    .%@@@@@@@@,         (@@@@@@@@/,                   
               .@@@@@@@@%(&@@@@@@#. ,&@@@@@@%(@@@@@@@@%               
             /@@@@@@@@@@@@@@@@@@@@\@@@@@@@@@@@@@@@@@@@@@@.            
              @@@@@-No.1 CTI-@@@@@@@\@@@@@@@@@@@@@@@@@@@@%             
                 %@@@@@@@@@@@@@@@@@@@@\@@@@@@@@@@@@@@@@#                
                     ,&@@@@@@@@@@@@@@@@@\@@@@@@@@@@&.                    
                              .*(#%%%#(/.  
              
             [\033[91m {}\033[00m ]
                       [\033[92m Coded by Ioja Iustin \033[00m] 
                  [\033[94m https://github.com/iojaiustin \033[00m]
        '''.format('EvilHolmes - CyberThreat intelligence tool'))

def check(keyword):
        print("[\033[93mi\033[00m] Searching for '\033[95m"+keyword+"'\033[00m...")
        
        try:
                content = ""

                urls = cyberscout.perform_search_cred(keyword)
                if urls:

                        for url in urls:
                                if ".onion" in url:
                                        content+="[\033[91m!\033[00m]Critical: \n"
                                        content+="'\033[95m"+keyword+"\033[00m' was found in a DarkWeb page:\n"
                                content+=url
                                content+="\n"

                if re.fullmatch(email_regex, keyword):
                        email = keyword
                        results = cyberscout.search_breach(email.split("@")[0])
                        if len(results):
                                if "Warning" not in content:
                                        content += "[\033[91m+\033[00m] Warning: "
                                content+="Your email was found in database breach:\n"
                                for account in results:
                                        content += account+'\n'

                if content:
                        print(content)
                else:
                        print("[\033[93m+\033[00m] Congratz, you are all clear! For now...")
        except KeyError:
                print("[\033[93m+\033[00m] \033[93mCongratz, you are all clear! For now...\033[00m")

if __name__ == "__main__":
        print_logo()
        check(query)