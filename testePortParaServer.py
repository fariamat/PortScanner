import socket

op = input('essa maquina é o servidor? (sim) ou (nao) ')
if op == "sim":
    ip = socket.gethostbyname(socket.gethostname()) #pega o ip da maquina
else:
    ip = input("qual o ip do servidor? ")

OP = input("DESEJA VARRER TODAS AS PORTAS? PODE LEVAR MAIS ATE 18HRS PARA CONCLUIR:")
if OP == "sim":
    # loop para definir todas as 65535 portas da rede
    portas_liberadas = []
    for porta_test in range(65535):  # numero totrais de portas
        s = socket.socket()
        s.settimeout(0.3)
        resultado = s.connect_ex((ip,porta_test))  # aqui eu passo o ip do servidor e a porta teste no for, a porta que vai estar passando pelo teste
        if resultado == 0:
            portas_liberadas = portas_liberadas.append(porta_test)
        s.close()

    print(portas_liberadas)
else:
    portas_teste =