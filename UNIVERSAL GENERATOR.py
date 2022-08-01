import os,platform, json
try:import requests
except ImportError:os.system('pip3 install requests')
try:import colorama
except ImportError:os.system('pip3 install colorama')
import string
import random
import time
#from dhooks import Webhook, Embed
try:from dhooks import Webhook, Embed
except ImportError:os.system('pip3 install dhooks')	
from colorama import Fore
logo = """ _   _  _   _  ___ __     __ _____  ____   ____      _     _        ____  _____  _   _  _____  ____      _     _____   ___   ____  
| | | || \ | ||_ _|\ \   / /| ____||  _ \ / ___|    / \   | |      / ___|| ____|| \ | || ____||  _ \    / \   |_   _| / _ \ |  _ \ 
| | | ||  \| | | |  \ \ / / |  _|  | |_) |\___ \   / _ \  | |     | |  _ |  _|  |  \| ||  _|  | |_) |  / _ \    | |  | | | || |_) |
| |_| || |\  | | |   \ V /  | |___ |  _ <  ___) | / ___ \ | |___  | |_| || |___ | |\  || |___ |  _ <  / ___ \   | |  | |_| ||  _ < 
 \___/ |_| \_||___|   \_/   |_____||_| \_\|____/ /_/   \_\|_____|  \____||_____||_| \_||_____||_| \_\/_/   \_\  |_|   \___/ |_| \_\\"""
print(logo)

check_file = os.path.exists(f"settings.json")
if check_file == False:
	stngs = """
{
	"auto_save_webhook": false,
	"last_webhook": null,
	"default_type_saving": "json"
}"""
	with open("settings.json", "w+") as file:file.write(stngs)

check_file = os.path.exists(f"saved.json")
if check_file == False:
	saved = """
{
    "valid_nitro": [],
    "valid_invites": [],
    "valid_github": [],
    "valid_replit": []
}"""
	with open("saved.json", "w+") as file:file.write(saved)
def error():
	print(Fore.RED + "Неверное значение")
	s = ""
	if platform.system() == "Windows":os.system('pause')
	else:input("Нажмите <Enter> для продолжения")
	os.system('cls||clear')
	print(Fore.RESET + logo)

with open("settings.json") as config:cfg = json.load(config)
colorama.init()
if cfg['default_type_saving'] == "webhook":
	while True:
		webh = input('Введите URL Discord вебхука для вывода валидных кодов, если хотите загрузить последний сохраненный вебхук, введите last: ')
		if webh == "last":webh = str(cfg['last_webhook'])
		valid = ['https://ptb.discord.com/api/webhooks', 'https://discord.com/api/webhooks', 'https://canary.discord.com/api/webhooks']
		try:
			response = requests.get(webh)
			if response.status_code == 200:
				hook = Webhook(webh)
				if cfg['auto_save_webhook']:
					cfg['last_webhook'] = webh
					with open("settings.json", 'w') as save: json.dump(cfg, save, indent=4)
				break
			else:
				print(Fore.RED + "Неверный URL вебхука")
				if platform.system() == "Windows":os.system('pause')
				else:input("Нажмите <Enter> для продолжения")
				print(Fore.RESET)
				os.system('cls||clear')
				print(Fore.RESET + logo)
		except:
				print(Fore.RED + "Неверный URL вебхука")
				if platform.system() == "Windows":os.system('pause')
				else:input("Нажмите <Enter> для продолжения")
				print(Fore.RESET)
				os.system('cls||clear')
				print(Fore.RESET + logo)
elif cfg['default_type_saving'] == "json":pass
else:
	print(Fore.RED + "Неверно заданный параметр!")
	if platform.system() == "Windows":os.system('pause')
	else:input("Нажмите <Enter> для продолжения")
	raise SystemExit
while True:
	os.system("cls||clear")
	print(logo)
	print(Fore.BLUE + "1)Discord приглашения\n2)Discord Nitro\n3)Гитхаб аккаунты\n4)Repl.it аккаунты")
	try:types = int(input('Выберите пункт: '))
	except:error();continue
	if types == 1:
		s = "Генерация завершена"
		try:inps = int(input("Введите количество генераций: "))
		except:error();continue
		for i in range(int(inps)):
			prigl = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
			url = f"https://discord.com/api/invite/{prigl}?with_application=false"
			response = requests.get(url)
			if response.status_code == 200:
				print(Fore.GREEN + f"{url} Валид")
				if cfg['default_type_saving'] == "webhook":hook.send(embed=Embed(title="Валидное приглашение", description=url, color=0x30d5c8))
				else:
					with open('saved.json', 'r') as file:autosave = json.load(file)
					autosave['valid_invites'].append(url)
					with open('saved.json', 'w') as file:json.dump(autosave,file, indent=4)
				time.sleep(0.5)
				os.system('cls||clear')
				print(Fore.RESET + logo)
			else:
				print(Fore.RED + f"discord.gg/{prigl} Невалид")
				time.sleep(0.5)
				os.system('cls||clear')
				print(Fore.RESET + logo)
	elif types == 2:
		s = "Генерация завершена"
		try:inps = int(input("Введите количество генераций: "))
		except:error();continue
		for i in range(int(inps)):
			nitro = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
			url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
			response = requests.get(url)
			if response.status_code == 200:
				print(Fore.GREEN + f"discord.gift/{nitro} Валид")
				if cfg['default_type_saving'] == "webhook":hook.send(embed=Embed(title="Валидное нитро", description=f"discord.gift/{nitro}", color=0x30d5c8))
				else:
					with open('saved.json', 'r') as file:autosave = json.load(file)
					autosave['valid_nitro'].append(f"https://discord.gift/{nitro}")
					with open('saved.json', 'w') as file:json.dump(autosave,file, indent=4)
				time.sleep(0.5)
			else:
				print(Fore.RED + f"discord.gift/{nitro} Невалид")
				time.sleep(0.5)
			os.system('cls||clear')
			print(Fore.RESET + logo)
	elif types == 3:
		s = "Генерация завершена"
		lens = (input("Укажите длину строки\nЕсли не указано будет взято число от 3 до 8\nЕсли введете rnd то будет подбираться рандмное количество каждый раз"))
		try:lengen = int(input("Укажите количество генераций"))
		except:error();continue
		lenstr = 0
		lim = 0
		if lens == "":
			lenstr = random.randint(3, 8)
			lim += 1
		elif lens != "rnd":
			try:lenstr = int(lens)
			except:error()
			lim += 1
		elif lens == "rnd":lim += 1
		if lim == 0:error();continue
		if lens != "rnd":
			try:
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(int(lenstr)))
					getcode = requests.get('http://github.com/' + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://github.com/{name} Невалид")
						time.sleep(0.5)
						os.system('cls||clear')
						print(Fore.RESET + logo)
					else:
						print(Fore.GREEN + f"https://github.com/{name} Валид")
						os.system('cls||clear')
						print(Fore.RESET + logo)
						if cfg['default_type_saving'] == "webhook":hook.send(embed=Embed(title="Валидный гитхаб", description=f"https://github.com/{name} ", color=0x30d5c8))
						else:
							with open('saved.json', 'r') as file:autosave = json.load(file)
							autosave['valid_github'].append(f"https://github.com/{name}")
							with open('saved.json', 'w') as file:json.dump(autosave,file, indent=4)
			except:error()
			time.sleep(0.5)	
		else:
			for i in range(int(lengen)):
				os.system("cls||clear")
				print(Fore.RESET + logo)
				letters = string.ascii_lowercase
				name = ''.join(random.choice(letters) for i in range(random.randint(3, 8)))
				getcode = requests.get('http://github.com/' + str(name))
				if getcode.status_code in [404, '404']:print(Fore.RED + f"https://github.com/{name} Невалид")
				else:
					print(Fore.GREEN + f"https://github.com/{name} Валид")
					if cfg['default_type_saving'] == "webhook":hook.send(embed=Embed(title="Валидный гитхаб", description=f"https://github.com/{name} ", color=0x30d5c8))
					else:
						with open('saved.json', 'r') as file:autosave = json.load(file)
						autosave['valid_github'].append(f"https://github.com/{name}")
						with open('saved.json', 'w') as file:json.dump(autosave,file, indent=4)
				time.sleep(0.5)
	elif types == 4:
		s = "Генерация завершена"
		lens = (input("Укажите длину строки\nЕсли не указано будет взято число от 3 до 8\nЕсли введете rnd то будет подбираться рандмное количество каждый раз"))
		try:lengen = int(input("Укажите количество генераций"))
		except:error();continue
		lenstr = 0
		lim = 0
		if lens == "":
			lenstr = random.randint(3, 8)
			lim += 1
		elif lens != "rnd":
			try:lenstr = int(lens)
			except:error()
			lim += 1
		elif lens == "rnd":lim += 1
		if lim == 0:error();continue
		if lens != "rnd":
			try:
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(int(lenstr)))
					getcode = requests.get('http://replit.com/@' + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://replit.com/@{name} Невалид")
						time.sleep(0.5)
						os.system('cls||clear')
						print(Fore.RESET + logo)
					else:
						print(Fore.GREEN + f"https://replit.com/@{name} Валид")
						os.system('cls||clear')
						print(Fore.RESET + logo)
						if cfg['default_type_saving'] == "webhook":hook.send(embed=Embed(title="Валидный реплит", description=f"https://replit.com/@{name} ", color=0x30d5c8))
						else:
							with open('saved.json', 'r') as file:autosave = json.load(file)
							autosave['valid_replit'].append(f"https://replit.com/@{name}")
							with open('saved.json', 'w') as file:json.dump(autosave,file, indent=4)
			except:error()
			time.sleep(0.5)	
		else:
			for i in range(int(lengen)):
				os.system("cls||clear")
				print(Fore.RESET + logo)
				letters = string.ascii_lowercase
				name = ''.join(random.choice(letters) for i in range(random.randint(3, 8)))
				getcode = requests.get('http://github.com/' + str(name))
				if getcode.status_code in [404, '404']:print(Fore.RED + f"https://github.com/{name} Невалид")
				else:
					print(Fore.GREEN + f"https://github.com/{name} Валид")
					if cfg['default_type_saving'] == "webhook":hook.send(embed=Embed(title="Валидный гитхаб", description=f"https://github.com/{name} ", color=0x30d5c8))
					else:
						with open('saved.json', 'r') as file:autosave = json.load(file)
						autosave['valid_github'].append(f"https://github.com/{name}")
						with open('saved.json', 'w') as file:json.dump(autosave,file, indent=4)
				time.sleep(0.5)
	else:error();continue
	if s == "":
		pass
	else:
		os.system('cls||clear')
		print(Fore.RESET + logo)
		print(Fore.RESET + "Генерация завершена")
		if platform.system() == "Windows":os.system('pause')
		else:input("Нажмите <Enter> для продолжения")
		os.system("cls||clear")
	#os.system('cls||clear')