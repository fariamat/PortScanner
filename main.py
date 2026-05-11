import socket

def verifica_host():
    host = input("Digite o host que deseja verificar: ")
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        host = 1 #1 para host invalido, host que nao existe
        return host
def verifica_porta():
    try:
        porta = int(input("Digite o porta que deseja verificar: "))
        return porta
    except ValueError:
        porta = 1 # status 1 para porta que contem caracteres invalidos como letras
        return porta

port = verifica_porta()
host = verifica_host()

if port == 1:
    print("Porta contem letras ou caracteres especias")
elif host == 1:
    print("host invalido, nao existe")
else:
    try:
        s = socket.socket()
        s.settimeout(1)
        resultado = s.connect_ex((host, port))
        if resultado == 0:
            print(f"a porta {port} esta aberta")
        else:
            print(f"a porta {port} esta fechada")
        s.close()
    except OverflowError:
        print("porta nao nao existe")