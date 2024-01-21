


import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():

    #Windows
    if name == 'nt':
        _ = system('cls')

    #Mac ou Linux
    else:
        _ = system('clear')


def game():

    limpa_tela()

    print("\nBem- Vindo(a) ao jogo da Forca!") 
    print("Adivinhe a palavra abaixo:\n")

    #Lista de palavras para o jogo
    palavras = ['banana', 'aacate', 'uva', 'morango', 'laranja']

    #Escolha de forma aleatoria a palavra para o jogo
    palavra = random.choice(palavras)

    #List Comprehension 
    letras_advinhadas = ['_' for letra in palavra]

    #Numero Chances de jogada
    chances = 6

    # Lista para guardar as letras erradas pelo jogador
    letras_erradas = []

    #Criar um loop 
    while chances > 0:

        #Imprimir as informações atualizadas do jogo
        
        print(" ".join(letras_advinhadas))
        print("\nChances Restantes:", chances)
        print("Letras Erradas:", " ".join(letras_erradas))

        #Tentantivas
        tentativa = input("\nDigita uma letra: ").lower()

        #Condição
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_advinhadas[index] = letra
                index += 1 

        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #Condição
        if  "_" not in letras_advinhadas:
            print("\nVocÊ venceu, a palavra era:", palavra)
            break

    if "_" in letras_advinhadas:
        print("\nVocÊ perdeu, a palavra era:", palavra)      

#Bloco main
if __name__ == "__main__":
    game()
