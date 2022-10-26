# Técnica: Cifra de César

import os
from turtle import delay

# Deixando a tela pronta
os.system('cls') or None

# Caracteres que serão utilizados
biblioteca = [ 'í','#', '*', 'Á', '(', 'a', 'É', 'o', 'p','5', '6', '7', '8', 'q', 'r', 's', 't', 'u', 'v', 'w', '°', '_', 'x', 'y', 'z', 'A', 'b', '||', 'c', 'd', 'e', 'f', '.', '!', 'Ê', '|||||', 'Î', 'Ô', 'ú', 'â', 'ê', 'î', 'ô', 'û', 'à', '@', '$', ')', '[', ']', '{', '}', '%', ':', '<', '>', '+', '=','g', 'h', 'i', 'j','||||||', 'Ó', 'Ú', 'k', 'l', 'm', 'n', 'B', 'C', 'D', '|||', 'Û', 'á', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'º', '-', 'P','Q', 'R', 'S', 'T', 'ã', 'õ', '&', 'Ã', 'Õ', 'U', ';', 'V','W','X', 'Y', 'Z', '0', '1', '2', '?', 'Í', 'Â', '3', '4', 'ó', '9', ' ', ',', 'é']

def criptografando():
    # Recebendo info
    mensagem = input('Digite a mensagem que deseja criptografar: ')

    # Desmontando mensagem
    parteMensagem = []
    parteMensagem.extend(mensagem)

    # Contando os itens da biblioteca
    numeroItensBiblioteca = len(biblioteca)

    # Criando chave de criptografar
    chave = 59
    mensagemCriptografada = ""

    # Criptografando
    for caractere in mensagem:
    
        indice = biblioteca.index(caractere)
        code = biblioteca[(indice + chave)%numeroItensBiblioteca]
        mensagemCriptografada += code

    # Mensagem Criptografada
    return print(mensagemCriptografada)

def descriptografando():
    # Recebendo info
    mensagemCriptografada = input('Digite a mensagem que deseja descriptografar: ')

    # Desmontando mensagem criptografar
    parteMensagemCriptografada = []
    parteMensagemCriptografada.extend(mensagemCriptografada)

    # Contando os itens da biblioteca
    numeroItensBiblioteca = len(biblioteca)

    # Criando chave de descriptografar
    chave = 59
    mensagem = ""

    # Descriptografando
    for caractere in mensagemCriptografada:
    
        indice = biblioteca.index(caractere)
        code = biblioteca[(indice - chave)%numeroItensBiblioteca]
        mensagem += code

    # Mensagem Descriptografada
    return print(mensagem)

def fixo():
    print('-=-'*20)
    print('                BEM VINDO AO CRIPTOGRAFEITOR')
    print('-=-'*20)

def movimento():
    escolha = input('\nVocê deseja:\n\n [1] criptografar\n [2] descriptografar\n\n -> ')

    if escolha == '1':
        os.system('cls') or None
        criptografando()
    elif escolha == '2':
        os.system('cls') or None
        descriptografando()
    else:
        print('\nNão consiguimos entender o que você quer :(\n')

def finalizar():
    fim = input('\nDeseja finalizar [S/N]? ').upper()

    while fim == "N":
        os.system('cls') or None
        fixo()
        movimento()
        fim = input('Deseja finalizar [S/N]? ').upper()

# Funcionando

fixo()
movimento()
finalizar()

# Fim do Programa