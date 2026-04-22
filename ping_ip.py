import subprocess  
import platform
import time

#Subprocess ele tem uam funcao de abrir o cmd ou terminal e rodar um comando nele sem que o user veja
#Já o Platform ele tem uma funcao para identificar em ql sistema eu estou

ip = input("Com qual IP vamos trabalhar agora ?")
time.sleep(2)


#Função para pingar uma máquina 
def ping_ip (ip):
    sistema = platform.system()  #Declarei a variavel sistemas e disse a pra busca pelo platforma.system em qual sistema op eu estou 
    if sistema == "Windows":
        parametro = "-n"
    else: 
        parametro = "-c"   
    comando = ["ping", parametro, "4", ip]   #Declarei essa variavel para poder passar os termos que vao ser jogados no cmd .
    resultado = subprocess.run(comando, capture_output=True) #Variavel vai jopgar no cmd via subprocess os tem na var comando e vai capturar oq sair de la pelo capture_output
    if resultado.returncode == 0:
            print("Print Máquina online")
            
    else:
            print("Máquina não respondeu")



while True: 
    print("\n ===== Menu =====")
    print("1 - Ping IP")
    print("2 - SSH")
    
    opcao = input("Escolha uma opção")
    
    if opcao == "1":
        ping_ip(ip)