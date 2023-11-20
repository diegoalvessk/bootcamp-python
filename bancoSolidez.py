class Account:

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("Seu novo saldo é: " , self.saldo)
            return print("Saque efetuado com sucesso.")
        else: 
            print("Seu novo saldo é: " , self.saldo)
            return print("Saque cancelado por falta de saldo.")
        
    def deposito(self, valor):
        self.saldo = self.saldo + valor
        print("Seu novo saldo é: " , self.saldo)
        return print("Deposito realizado com sucesso")


cont = 0

while cont != 2:

    if(cont == 0):
        print("Vamos criar sua conta!")

        nome = input("Informe seu nome para prosseguirmos")

        saldo = float(input("Informe o saldo da sua conta."))

        conta = Account(nome, saldo)

        cont = cont + 1

    condicao = int(input("O que deseja fazer agora? 1 - Saque. 2 - Deposito. 3 - Sair"))

    if(condicao == 3):
        exit()
    elif(condicao == 1):
        valor = float(input("Informe o valor do saque"))
        conta.saque(valor)
    elif(condicao ==  2):
        valor = float(input("Informe o valor do deposito"))
        conta.deposito(valor)

