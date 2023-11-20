def imprimir_tabuleiro(tabuleiro):
    """
    Função para imprimir um tabuleiro de jogo da velha.

    Parâmetros:
    - tabuleiro: Uma lista de 9 elementos representando o tabuleiro do jogo da velha.
      Use 'X' para marcar o jogador 1 e 'O' para marcar o jogador 2.
    """
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

# Exemplo de uso:
tabuleiro_exemplo = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
contador = 0

def receber_jogada(contador):
    result = verificar_jogo()
    while result == "em andamento":
        result = verificar_jogo()
        if contador<9:
            if contador % 2 == 0:

                jogada_jogador1 = int(input("Jogador 1 informe sua jogada. Escolha de 0 a 8"  + " "))
                
                cont = 0

                while cont<2: 
                    if jogada_jogador1>8 or jogada_jogador1<0:
                        print("Informe um número valido")
                        jogada_jogador1 = int(input("Jogador 1 informe sua jogada. Escolha de 0 a 8 "  + " " ))
                    else:
                        cont = cont + 1

                    if tabuleiro_exemplo[jogada_jogador1] != '-':
                        print("Informe uma posição que esteja válida")
                        jogada_jogador1 = int(input("Jogador 1 informe sua jogada. Escolha de 0 a 8 "  + " " ))
                    else:

                        cont = cont + 1

                tabuleiro_exemplo[jogada_jogador1] = "X"
                contador =  contador + 1
            
            else:
                jogada_jogador2 = int(input("Jogador 2 informe sua jogada. Escolha de 0 a 8 "  + " " ))

                while cont<2: 
                    if jogada_jogador2>8 or jogada_jogador2<0:
                        print("Informe um número valido")
                        jogada_jogador2 = int(input("Jogador 2 informe sua jogada. Escolha de 0 a 8 "  + " " ))
                    else:
                        cont = cont + 1

                    if tabuleiro_exemplo[jogada_jogador2] != '-':
                        print("Informe uma posição que esteja válida")
                        jogada_jogador2 = int(input("Jogador 2 informe sua jogada. Escolha de 0 a 8 "  + " " ))
                    else:
                        cont = cont + 1

                tabuleiro_exemplo[jogada_jogador2] = "O"
                contador =  contador + 1
                
    else: 
        print("O jogo acabou")
        print("Mostrarei agora o ganhador do jogo, mostrando o tabuleiro. Jogador 1 1 = X e jogador 2 = O")
        imprimir_tabuleiro(tabuleiro_exemplo)
        exit()


def verificar_jogo():

    if tabuleiro_exemplo[0] != '-' and tabuleiro_exemplo[1] != '-' and tabuleiro_exemplo[2] != '-' and tabuleiro_exemplo[3] != '-' and tabuleiro_exemplo[4] != '-' and tabuleiro_exemplo[5] != '-' and tabuleiro_exemplo[6] != '-' and tabuleiro_exemplo[7] != '-' and tabuleiro_exemplo[8] != '-':
        status_jogo = "acabou"

    elif tabuleiro_exemplo[0] == '-' or tabuleiro_exemplo[1] == '-' or tabuleiro_exemplo[2] == '-' or tabuleiro_exemplo[3] == '-' or   tabuleiro_exemplo[4] == '-' or tabuleiro_exemplo[5] == '-' or   tabuleiro_exemplo[6] == '-' or tabuleiro_exemplo[7] == '-' or      tabuleiro_exemplo[8]: 
        status_jogo = "em andamento"


    return status_jogo
print("Esté é o tabuleiro.")
imprimir_tabuleiro(tabuleiro_exemplo)
receber_jogada(contador)

