import platform
import os
while True:
	try:
		import requests
		break
	except ImportError: 
		print('Отсутствует библиотека requests\nВведите pip install requests и повторите попытку')
		if platform.system() == "Windows":
			os.system('pause')
			os.system('cls')
		else:
			input("Нажмите <Enter> для продолжения")
			os.system('clear')
while True:
	try:
		import colorama
		break
	except ImportError: 
		print('Отсутствует библиотека colorama\nВведите pip install colorama и повторите попытку')
		if platform.system() == "Windows":
			os.system('pause')
			os.system('cls')
		else:
			input("Нажмите <Enter> для продолжения")
			os.system('clear')
import string
import random
import time
while True:
	try:
		from dhooks import Webhook, Embed
		break
	except ImportError: 
		print('Отсутствует библиотека dhooks\nВведите pip install dhooks и повторите попытку')
		if platform.system() == "Windows":
			os.system('pause')
			os.system('cls')
		else:
			input("Нажмите <Enter> для продолжения")
			os.system('clear')
			
from colorama import Fore

if platform.system() == "Windows":
	colorama.init()
	print('Универсальный генератор v1.0 FOR WINDOWS')
	while True:
		webh = input('Введите URL Discord вебхука для вывода валидных кодов: ')
		if not "https://discord.com/api/webhooks" in webh:
			print(Fore.RED + "Недопустимый URL вебхука")
			os.system('pause')
			print(Fore.RESET)
			os.system('cls')
		else:
			response = requests.get(webh)
			if response.status_code == 200:
				hook = Webhook(webh)
				break
			else:
				print(Fore.RED + "Неверный URL вебхука")
				os.system('pause')
				print(Fore.RESET)
				os.system('cls')
		print('Универсальный генератор v1.0')
	while True:
		print(Fore.BLUE + "1)Discord приглашения\n2)Discord Nitro\n3)Гитхаб аккаунты\n4)Repl.it аккаунты")
		types = input('Выберите пункт: ')
		if types == "1":
			s = "Генерация завершена"
			inps = input("Введите количество генераций: ")
			for i in range(int(inps)):
				prigl = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
				url = f"https://discord.com/api/invite/{prigl}?with_application=false"
				response = requests.get(url)
				if response.status_code == 200:
					print(Fore.GREEN + f"{url} Валид")
					hook.send(embed=Embed(title="Валидное приглашение", description=url, color=0x30d5c8))
					time.sleep(0.5)
				else:
					print(Fore.RED + f"discord.gg/{prigl} Невалид")
					time.sleep(0.5)
					os.system('cls')
		elif types == "2":
			s = "Генерация завершена"
			inps = input("Введите количество генераций: ")
			for i in range(int(inps)):
				nitro = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
				url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
				response = requests.get(url)
				if response.status_code == 200:
					print(Fore.GREEN + f"discord.gift/{nitro} Валид")
					hook.send(embed=Embed(title="Валидное нитро", description=f"discord.gift/{nitro}", color=0x30d5c8))
					time.sleep(0.5)
				else:
					print(Fore.RED + f"discord.gift/{nitro} Невалид")
					time.sleep(0.5)
					os.system('cls')	
		elif types == "3":
			s = "Генерация завершена"
			lens = input("Укажите длину строки\nЕсли не указано будет взято число от 3 до 8\nЕсли введете rnd то будет подбираться рандмное количество каждый раз")
			lengen = input("Укажите количество генераций")
			lenstr = 0
			if lens == "":
				lenstr = random.randint(3, 8)
			elif lens != "rnd":
				lenstr = lens
			if lens != "rnd":
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(int(lenstr)))
					getcode = requests.get('http://github.com/' + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://github.com/{name} Невалид")
						time.sleep(0.5)
						os.system('cls')
					else:
						print(Fore.GREEN + f"https://github.com/{name} Валид")
						os.system('cls')
						hook.send(embed=Embed(title="Валидный гитхаб", description=f"https://github.com/{name} ", color=0x30d5c8))
						time.sleep(0.5)	
			else:
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(random.randint(3, 8)))
					getcode = requests.get('http://github.com/' + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://github.com/{name} Невалид")
						time.sleep(0.5)
						os.system('cls')
					else:
						print(Fore.GREEN + f"https://github.com/{name} Валид")
						os.system('cls')
						hook.send(embed=Embed(title="Валидный гитхаб", description=f"https://github.com/{name} ", color=0x30d5c8))
						time.sleep(0.5)
		elif types == "4":
			s = "Генерация завершена"
			lens = input("Укажите длину строки\nЕсли не указано будет взято число от 3 до 8\nЕсли введете rnd то будет подбираться рандмное количество каждый раз")
			lengen = input("Укажите количество генераций")
			lenstr = 0
			if lens == "":
				lenstr = random.randint(3, 8)
			elif lens != "rnd":
				lenstr = lens
			if lens != "rnd":
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(int(lenstr)))
					getcode = requests.get('http://replit.com/' + "@" + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://replit.com/@{name} Невалид")
						time.sleep(0.5)
						os.system('cls')
					else:
						print(Fore.GREEN + f"https://replit.com/@{name} Валид")
						os.system('cls')
						hook.send(embed=Embed(title="Валидный replit", description=f"https://replit.com/@{name} ", color=0x30d5c8))
						time.sleep(0.5)	
			else:
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(random.randint(3, 8)))
					getcode = requests.get('http://replit.com/@' + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://replit.com/@{name} Невалид")
						time.sleep(0.5)
						os.system('cls')
					else:
						print(Fore.GREEN + f"https://replit.com/@{name} Валид")
						os.system('cls')
						hook.send(embed=Embed(title="Валидный replit", description=f"https://replit.com/@{name} ", color=0x30d5c8))
						time.sleep(0.5)
		else:
			print(Fore.RED + "Неверное значение")
			s = ""
			os.system('pause')
		if s == "":
			print(Fore.RESET + s)
			os.system('cls')
		else:
			print(Fore.RESET + "Генерация завершена")
			os.system('pause')
		os.system('cls')
else:
	colorama.init()
	print('Универсальный генератор v1.0 FOR LINUX')
	while True:
		webh = input('Введите URL Discord вебхука для вывода валидных кодов: ')
		if not "https://discord.com/api/webhooks" in webh:
			print(Fore.RED + "Недопустимый URL вебхука")
			input("Нажмите <Enter> для продолжения")
			print(Fore.RESET)
			os.system('clear')
		else:
			response = requests.get(webh)
			if response.status_code == 200:
				hook = Webhook(webh)
				break
			else:
				print(Fore.RED + "Неверный URL вебхука")
				input("Нажмите <Enter> для продолжения")
				print(Fore.RESET)
				os.system('clear')	
		print('Универсальный генератор v1.0')
	while True:
		print(Fore.BLUE + "1)Discord приглашения\n2)Discord Nitro\n3)Гитхаб аккаунты\n4)Repl.it аккаунты")
		types = input('Выберите пункт: ')
		if types == "1":
			inps = input("Введите количество генераций: ")
			for i in range(int(inps)):
				prigl = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
				url = f"https://discord.com/api/invite/{prigl}?with_application=false"
				response = requests.get(url)
				if response.status_code == 200:
					print(Fore.GREEN + f"{url} Валид")
					hook.send(embed=Embed(title="Валидное приглашение", description=url, color=0x30d5c8))
					time.sleep(0.5)
				else:
					print(Fore.RED + f"discord.gg/{prigl} Невалид")
					time.sleep(0.5)
					os.system('clear')	
		elif types == "2":
			inps = input("Введите количество генераций: ")
			for i in range(int(inps)):
				nitro = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
				url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
				response = requests.get(url)
				if response.status_code == 200:
					print(Fore.GREEN + f"discord.gift/{nitro} Валид")
					hook.send(embed=Embed(title="Валидное нитро", description=f"discord.gift/{nitro}", color=0x30d5c8))
					time.sleep(0.5)
				else:
					print(Fore.RED + f"discord.gift/{nitro} Невалид")
					time.sleep(0.5)
					os.system('clear')	
		elif types == "3":
			lens = input("Укажите длину строки\nЕсли не указано будет взято число от 3 до 8\nЕсли введете rnd то будет подбираться рандмное количество каждый раз")
			lengen = input("Укажите количество генераций")
			lenstr = 0
			if lens == "":
				lenstr = random.randint(3, 8)
			elif lens != "rnd":
				lenstr = lens
			if lens != "rnd":
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(int(lenstr)))
					getcode = requests.get('http://github.com/' + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://github.com/{name} Невалид")
						time.sleep(0.5)
						os.system('clear')	
					else:
						print(Fore.GREEN + f"https://github.com/{name} Валид")
						os.system('clear')	
						hook.send(embed=Embed(title="Валидный гитхаб", description=f"https://github.com/{name} ", color=0x30d5c8))
						time.sleep(0.5)	
			else:
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(random.randint(3, 8)))
					getcode = requests.get('http://github.com/' + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://github.com/{name} Невалид")
						time.sleep(0.5)
						os.system('clear')	
					else:
						print(Fore.GREEN + f"https://github.com/{name} Валид")
						os.system('clear')	
						hook.send(embed=Embed(title="Валидный гитхаб", description=f"https://github.com/{name} ", color=0x30d5c8))
						time.sleep(0.5)
		elif types == "4":
			lens = input("Укажите длину строки\nЕсли не указано будет взято число от 3 до 8\nЕсли введете rnd то будет подбираться рандмное количество каждый раз")
			lengen = input("Укажите количество генераций")
			lenstr = 0
			if lens == "":
				lenstr = random.randint(3, 8)
			elif lens != "rnd":
				lenstr = lens
			if lens != "rnd":
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(int(lenstr)))
					getcode = requests.get('http://replit.com/' + "@" + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://replit.com/@{name} Невалид")
						time.sleep(0.5)
						os.system('clear')	
					else:
						print(Fore.GREEN + f"https://replit.com/@{name} Валид")
						os.system('clear')	
						hook.send(embed=Embed(title="Валидный replit", description=f"https://replit.com/@{name} ", color=0x30d5c8))
						time.sleep(0.5)	
			else:
				for i in range(int(lengen)):
					letters = string.ascii_lowercase
					name = ''.join(random.choice(letters) for i in range(random.randint(3, 8)))
					getcode = requests.get('http://replit.com/@' + str(name))
					if getcode.status_code in [404, '404']:
						print(Fore.RED + f"https://replit.com/@{name} Невалид")
						time.sleep(0.5)
						os.system('clear')	
					else:
						print(Fore.GREEN + f"https://replit.com/@{name} Валид")
						os.system('clear')	
						hook.send(embed=Embed(title="Валидный replit", description=f"https://replit.com/@{name} ", color=0x30d5c8))
						time.sleep(0.5)
		else:
			print(Fore.RED + "Неверное значение")
			s = ""
			input("Нажмите <Enter> для продолжения")
		if s == "":
			print(Fore.RESET + s)
			os.system('clear')
		else:
			print(Fore.RESET + "Генерация завершена")
			input("Нажмите <Enter> для продолжения")
		os.system('clear')	