import socket
from geoip import geolite2
# !==========================================================================
print(" *" * 26 , "START" , " *" * 26)
print("=> [1] Ip Website\n=> [2] protocol type\n=> [3] Server Name\n=> [4] ip public anythings\n=> [5] show my ip & hostname")
choose =input('=> Select Number: ')
print(" $" * 25 , "WELCOM..." , " $" * 25)

# todo========================================================================
def gethip():
    print('''\033[32m
          ███▄ ▄███▓▓██   ██▓    ██▓ ██▓███         ██░ ██  ▒█████    ██████ ▄▄▄█████▓ ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████ 
▓██▒▀█▀ ██▒ ▒██  ██▒   ▓██▒▓██░  ██▒      ▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒ ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▓██    ▓██░  ▒██ ██░   ▒██▒▓██░ ██▓▒      ▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███   
▒██    ▒██   ░ ▐██▓░   ░██░▒██▄█▓▒ ▒      ░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
▒██▒   ░██▒  ░ ██▒▓░   ░██░▒██▒ ░  ░      ░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
░ ▒░   ░  ░   ██▒▒▒    ░▓  ▒▓▒░ ░  ░       ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
░  ░      ░ ▓██ ░▒░     ▒ ░░▒ ░            ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░      ░    ▒ ▒ ░░      ▒ ░░░              ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░         ░   ░ ░   ░   ▒   ░      ░      ░   
       ░    ░ ░         ░                  ░  ░  ░    ░ ░        ░                    ░       ░  ░       ░      ░  ░
            ░ ░                                                                                                     
\033[34m Developed by Abdollah El-Fiqi \033[39m         
''')
    hostname = socket.gethostname()
    IpAddr = socket.gethostbyname(hostname)
    print(f"=>\033[35m your host name is:\033[39m \033[37m('{hostname}')\033[39m")
    print(f"=>\033[35m your Ip Addriss is:\033[39m (\033[37m{IpAddr})\033[39m")




if choose == '1':
    print('''\033[32m
          /      |                /  |  _  /  |          /  |                /  |  /  |              
$$$$$$/   ______        $$ | / \ $$ |  ______  $$ |____    _______ $$/  _$$ |_     ______  
  $$ |   /      \       $$ |/$  \$$ | /      \ $$      \  /       |/  |/ $$   |   /      \ 
  $$ |  /$$$$$$  |      $$ /$$$  $$ |/$$$$$$  |$$$$$$$  |/$$$$$$$/ $$ |$$$$$$/   /$$$$$$  |
  $$ |  $$ |  $$ |      $$ $$/$$ $$ |$$    $$ |$$ |  $$ |$$      \ $$ |  $$ | __ $$    $$ |
 _$$ |_ $$ |__$$ |      $$$$/  $$$$ |$$$$$$$$/ $$ |__$$ | $$$$$$  |$$ |  $$ |/  |$$$$$$$$/ 
/ $$   |$$    $$/       $$$/    $$$ |$$       |$$    $$/ /     $$/ $$ |  $$  $$/ $$       |
$$$$$$/ $$$$$$$/        $$/      $$/  $$$$$$$/ $$$$$$$/  $$$$$$$/  $$/    $$$$/   $$$$$$$/ 
        $$ |                                                                               
        $$ |                                                                               
        $$/                                                                                
\033[39mDeveloped by Abdollah El-Fiqi
''')
    Ipwebsite = socket.gethostbyname(input("\033[33m=> Website Company is: ")).strip()
    print(f"\033[33m=> your Ip is:\033[39m (\033[37m\"{Ipwebsite}\")\033[39m")
    print(" =" * 23 , "Thanks Very much" , " =" * 23)






elif choose == '2' :
    print('''\033[32m          _                  _   _                    
                 | |                | | | |                   
  _ __  _ __ ___ | |_ ___   ___ ___ | | | |_ _   _ _ __   ___ 
 | '_ \| '__/ _ \| __/ _ \ / __/ _ \| | | __| | | | '_ \ / _ \
 | |_) | | | (_) | || (_) | (_| (_) | | | |_| |_| | |_) |  __/
 | .__/|_|  \___/ \__\___/ \___\___/|_|  \__|\__, | .__/ \___|
 | |                                          __/ | |         
 |_|                                         |___/|_|         
\033[32mDeveloped by Abdollah El-Fiqi\033[39m    
''')
    print("=> [5] https\n=> [6] http\n=> [7] ftp\n=> [8] ftp-data\n=> [9] TCP\n=> [10] telnet\n=> [11] smtp\n=> [12] daytime")
    port = socket.getservbyname(input("=> Enter Your Protocol is: "))
    print(f"=> your port is: (\"{port}\")")
    print(" =" * 23 , "Thanks Very much" , " =" * 23)






elif choose == '3' :
    print('''\033[32m
           _____   ___  ____  __ __    ___  ____       ____    ____  ___ ___    ___ 
 / ___/  /  _]|    \|  |  |  /  _]|    \     |    \  /    ||   |   |  /  _]
(   \_  /  [_ |  D  )  |  | /  [_ |  D  )    |  _  ||  o  || _   _ | /  [_ 
 \__  ||    _]|    /|  |  ||    _]|    /     |  |  ||     ||  \_/  ||    _]
 /  \ ||   [_ |    \|  :  ||   [_ |    \     |  |  ||  _  ||   |   ||   [_ 
 \    ||     ||  .  \\   / |     ||  .  \    |  |  ||  |  ||   |   ||     |
  \___||_____||__|\_| \_/  |_____||__|\_|    |__|__||__|__||___|___||_____|
\033[39m
Developed by Abdollah El-Fiqi
''')
    x = int(input("=> Enter Your Protocol Number: ")).strip()
    service = socket.getservbyport(x)
    print(f"=> The Required Protocol is: (\"{service}\")")
    print(" =" * 23 , "Thanks Very much" , " =" * 23)








elif choose == '4' :
    print(''' \033[32m
           _                  _    _ _                    _   _    _              
 (_)_ __   _ __ _  _| |__| (_)__   __ _ _ _ _  _| |_| |_ (_)_ _  __ _ ___
 | | '_ \ | '_ \ || | '_ \ | / _| / _` | ' \ || |  _| ' \| | ' \/ _` (_-<
 |_| .__/ | .__/\_,_|_.__/_|_\__| \__,_|_||_\_, |\__|_||_|_|_||_\__, /__/
   |_|    |_|                               |__/                |___/    
\033[39m
Developed by Abdollah El-Fiqi          
''')
    ip_info = input(f"Enter your ip: ").strip()
    info = geolite2.lookup(ip_info)
    print(f"=> [1] your ip Enter is: {info.ip}")
    print(f"=> [2] your country Enter from ip is: {info.country}")
    print(f"=> [3] your continent Enter from ip is: {info.continent}")
    print(f"=> [4] your timezone Enter from ip is: {info.timezone}")
    print(f"=> [5] your location Enter from ip is: {info.location}")
    print(" =" * 23 , "Thanks Very much" , " =" * 23)


    





elif choose == '5':
    gethip()
else:
    print('=> Write the Correct Number\n\nI\'m Waiting...')
# !============================================================================