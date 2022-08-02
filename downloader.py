import requests, json, os,time, platform
try:import colorama
except ImportError:os.system("pip install colorama");import colorama
colorama.init()

logo = """ _   _  _   _  ___ __     __ _____  ____   ____      _     _        ____  _____  _   _  _____  ____      _     _____   ___   ____  
| | | || \ | ||_ _|\ \   / /| ____||  _ \ / ___|    / \   | |      / ___|| ____|| \ | || ____||  _ \    / \   |_   _| / _ \ |  _ \ 
| | | ||  \| | | |  \ \ / / |  _|  | |_) |\___ \   / _ \  | |     | |  _ |  _|  |  \| ||  _|  | |_) |  / _ \    | |  | | | || |_) |
| |_| || |\  | | |   \ V /  | |___ |  _ <  ___) | / ___ \ | |___  | |_| || |___ | |\  || |___ |  _ <  / ___ \   | |  | |_| ||  _ < 
 \___/ |_| \_||___|   \_/   |_____||_| \_\|____/ /_/   \_\|_____|  \____||_____||_| \_||_____||_| \_\/_/   \_\  |_|   \___/ |_| \_\\"""
logo2 = """
     _                          _                    _             
  __| |  ___  __      __ _ __  | |  ___    __ _   __| |  ___  _ __ 
 / _` | / _ \ \ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|
| (_| || (_) | \ V  V / | | | || || (_) || (_| || (_| ||  __/| |   
 \__,_| \___/   \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|   """
def printlogo():
    os.system("cls||clear")
    print(colorama.Fore.GREEN + logo)
    print(logo2 + colorama.Fore.BLUE)
def pause():
    if platform.system() == "Windows":os.system("pause")
    else:input("Нажмите <Enter> для продолжения")
printlogo()
with open('saved.json', 'r') as file:s = json.load(file)
while True:
    ch = input("Скачать с сгенерированных GitHub`ов\n1)Github\n2)Выход из приложения ")
    if ch == "1":
        for i in s['valid_github']:
            spisok = []
            n = i.replace("https://github.com/", "")
            r = requests.get(f"https://api.github.com/users/{n}/repos")
            jsn = json.loads(r.text)
            print(colorama.Fore.BLUE + f"Идет сбор информации о репозиториях {n}")
            time.sleep(0.5)
            printlogo()
            for i in range(len(jsn)):
                #try:
                    if str(type(jsn[i])) == "<class 'dict'>":
                        try:spisok.append(jsn[i]['name'])
                        except:pass
                        l=1
                #except:print(colorama.Fore.RED + "Не так быстро скачивайте, гитхаб это не разрешает");pause();printlogo();break;l=0
            #try:
             #   if l == 0:print(colorama.Fore.RED + "Не так быстро скачивайте, гитхаб это не разрешает");pause();printlogo();break
            #except:l=0
            print(colorama.Fore.GREEN + f"Начинаю скачивать репозитории {n}")
            time.sleep(0.5)
            printlogo()
            for i in spisok:
                check_file = os.path.exists(f"downloads\\{n}")
                if check_file == False:os.mkdir(f"downloads\\{n}")
                p = requests.get(f"https://github.com/{n}/{i}/archive/refs/heads/master.zip")
                out = open(f"downloads\\{n}\\{i}.zip", 'wb')
                out.write(p.content)
                out.close() 
                print(f"Репозитория [{i}] от {i} скачана успешно")
                time.sleep(0.5)
                printlogo()
            printlogo()
            print(colorama.Fore.GREEN + f"Репозитории {n} скачаны успешно")
    elif ch == "2":exit()
    else:print(colorama.Fore.RED + "Неверный пункт");pause()
    printlogo()