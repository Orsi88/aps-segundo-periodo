
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

chave = 3
mensagem = 'abacaxi'

#tamanho da lista alfabeto

#n = len(alfabeto)
n = 128

cifrada = ""
for letra in mensagem:

    #ord()
    #chr()
    
    #achar no alfabeto a letra que esteja chave posições a frente

    #indice = alfabeto.index(letra)
    indice = ord(letra)

    #nova_letra = alfabeto[(indice + chave)%n]
    nova_letra = chr((indice + chave)%n)

    #substituir na mensagem a letra pela nova_letra
    cifrada += nova_letra

print(mensagem)
print(cifrada)
