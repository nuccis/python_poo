#Simulação de Banco: Implemente um programa que simule as operações básicas de um banco, como criar conta, depositar, sacar e verificar saldo.

#Classes
class ContaBancaria:
    def __init__(self, correntista:str) -> None:
        self.correntista:str = correntista
        self.saldo:float = 0
        self.conta:bool = False
    
    def criarConta(self) -> None:
        if self.conta:
            print('A conta já está aberta')
        else:
            self.conta = True
            print('A conta foi aberta com sucesso!')

    def depositar(self, din):
        if self.conta:
            self.saldo += din
        else:
            print('A conta se encontra fechada')

    def sacar(self, din):
        if not self.conta:
            print('A conta se encontra fechada')
        else:
            if self.saldo - din < 0:
                print('Você não possui saldo suficiente')
                print(f'Saldo atual de R${self.saldo:.2f}'.replace('.',','))
            else:
                self.saldo -= din
                print(f'Saque de R${din} '.replace('.',','),'realizado com sucesso!')
                print(f'Saldo atual de R${self.saldo:.2f}'.replace('.',','))

    def verificarSaldo(self):
        if self.conta:
            print(f'Saldo: R${self.saldo:.2f}'.replace('.',','))
        else:
            print('A conta se encontra fechada')

    def fecharConta(self):
        if not self.conta:
            print('A conta já se encontra fechada')
        elif self.saldo > 0:
            print(f'Não é possível fechar a conta.\n'
                  f'Ainda há um saldo de R${self.saldo:.2f}'.replace('.',','))
        else:
            self.conta = False
            print('A conta foi fechada com sucesso.')
                        
    def verificarConta(self):
        if self.conta:
            print('A sua conta encontra-se aberta\n'
                  f'Saldo: R${self.saldo:.2f}'.replace('.',','))
        else:
            print('Sua conta encontra-se fechada.')

#Funções
def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            return float(entrada)
        
#Programa principal
minha_conta = ContaBancaria('Leticia')

minha_conta.depositar(2)
minha_conta.sacar(2)