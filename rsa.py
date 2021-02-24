#IMPORTA O MÓDULO RANDOM QUE POSSIBILITA GERAR NÚMEROS ALEATÓRIOS
import random

#FUNÇÃO PARA CRIPTROGRAFAR
def criptografar(msg,n,e):
    i = 0
    tamanho = len(msg)
    msg_criptografada = []
    while(i < tamanho):
        letra = ord(msg[i])
        letra_criptografada = (letra**e)%n    #REGRA DA CRIPTOGRAFIA
        msg_criptografada.append(letra_criptografada)
        i += 1
    return msg_criptografada


#FUNÇÃO PARA DESCRIPTROGRAFAR
def descriptografar(msg,n,d):
    i = 0
    tamanho = len(msg)
    msg_descriptografada = []
    while i < tamanho:
        letra_descriptografada = (msg[i]**d)%n  #REGRA DE DESCRIPTOGRAFIA
        letra = chr(letra_descriptografada)
        msg_descriptografada.append(letra)
        i += 1
    return msg_descriptografada


#FUNÇÃO QUE GERA UM NÚMERO ALEATÓRIO DENTRO DE UM INTERVALO E VERIFICA SE ELE É PRIMO
def gerar_primo():
    while True:
        n=random.randrange(11,20)
        if(primo(n) == True):
            #print(n)
            return n

#FUNÇÃO QUE RECEBE UM VALOR E VERIFICA SE ELE É PRIMO OU NÃO
def primo(num):
    i = 0
    for x in range(1,num+1):
        if(num%x == 0):
            i+=1
    if(i == 2):
        return True
    else:
        return False

#VERIFICA SE O NUMERO É PRIMO E CALCULA SEU TOTIENTE
def totiente(num):
    if(primo(num) == True):
        return num-1 #CALCULA O TOTIENTE (NUM-1)

#GERA UM NÚMERO 'E' QUE NÃO PODE TER DIVISOR EM COMUM COM TOTIENTE DE N
def gerar_e(num): 
    def mdc(a,b):
        if (b==0):
            return a
        return mdc(b,a%b)

    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e
#RODA O LAÇO ATÉ QUE UM NÚMERO 'D' QUANDO MULTIPLICADO POR 'E' MOD(TOTIENTE DE N) = 1, SENDO ESTE O INVERSO DE 'E'
def calcular_d(totiente_n,e):
    d = 0
    while((d*e)%totiente_n != 1):
        d+=1
    return d


#RECEBE A LISTA COM UMA MENSAGEM E JUNTA OS CARACTERES
def juntar_msg(msg,tipo):
    if(tipo == "string"):
        mensagem = "".join(msg)
        return mensagem
    else:
        mensagem = "".join(map(str,msg))
        return mensagem


#DEFINE AS VARIAVEIS BÁSICAS PARA CRIPTOGRAFAR
p = gerar_primo()
q = gerar_primo()
n = p * q
toti_p = totiente(p)
toti_q = totiente(q)
toti_n = toti_p * toti_q
e = gerar_e(toti_n)
d = calcular_d(toti_n,e)

#DEFINE A CHAVE PÚBLICA E PRIVADA
chave_publica = (n,e)
chave_privada = (n,d)


#EXECUTA O PROGRAMA
frase = input("Digite a mensagem que deseja criptografar: ")

#CRIPTOGRAFA A MENSAGEM
msg_criptografada = criptografar(frase,n,e)
mensagem_criptografada = juntar_msg(msg_criptografada,"number")

#DESCRIPTOGRAFA A MENSAGEM
msg_descriptografada = descriptografar(msg_criptografada,n,d)
mensagem_descriptografada = juntar_msg(msg_descriptografada,"string")


#ESCREVE OS RESULTADOS
print(f"\nMensagem criptograda: {mensagem_criptografada}")
print(f"\nMensagem descriptografada: {mensagem_descriptografada}")
print(f"\nChave pública: {chave_publica}")
print(f"\nChave privada: {chave_privada}")
#print(f"\nPrimos escolhidos: P: {p} e Q: {q}")
#print(f"\n toti_n:{toti_n} , e:{e}")
