#Simulação de Banco: Implemente um programa que simule as operações básicas de um banco, como criar conta, depositar, sacar e verificar saldo.


from time import sleep

#Classes
class ContaBancaria:
    def __init__(self, correntista:str) -> None:
        self.correntista:str = correntista
        self.saldo:float = 0
        self.conta:bool = False
    
    def criarConta(self) -> None:
        if self.conta:
            print('\nA conta já está aberta')
        else:
            self.conta = True
            print('\nA conta foi aberta com sucesso!')

    def depositar(self, din):
        if self.conta:
            self.saldo += din
        else:
            print('\nA conta se encontra fechada')

    def sacar(self, din):
        if not self.conta:
            print('\nA conta se encontra fechada')
        else:
            if self.saldo - din < 0:
                print('\nVocê não possui saldo suficiente')
                print(f'\nSaldo atual de R${self.saldo:.2f}'.replace('.',','))
            else:
                self.saldo -= din
                print(f'\nSaque de R${din} '.replace('.',','),'realizado com sucesso!')
                print(f'\nSaldo atual de R${self.saldo:.2f}'.replace('.',','))

    def verificarSaldo(self):
        if self.conta:
            print(f'\nSaldo: R${self.saldo:.2f}'.replace('.',','))
        else:
            print('\nA conta se encontra fechada')

    def fecharConta(self):
        if not self.conta:
            print('\nA conta já se encontra fechada')
        elif self.saldo > 0:
            print(f'\nNão é possível fechar a conta.\n'
                  f'Ainda há um saldo de R${self.saldo:.2f}'.replace('.',','))
        else:
            self.conta = False
            print('\nA conta foi fechada com sucesso.')
                        
#Funções
def leiaDinheiro(msg) -> float:
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            return float(entrada)

def leInteiro(msg) -> int:
    while True:
        try:
            opc = int(input(msg))
            if opc not in range(1, 7):
                raise ValueError
            break
        except ValueError:
            print('\033[0;31mErro! Digite uma opção válida.\033[m')
    return opc

#Programa principal
print('-'*60)
print(f'{'BEM VINDA AO BANCO':^60}')
print('-'*60)

while True:
    opc = str(input('Olá! Deseja entrar no banco? [S/N] -> ')).strip().upper()
    if opc in 'SN':
        break
    print('\033[0;31mErro! Digite uma opção válida.\033[m')

if opc == 'S':
    minha_conta = ContaBancaria(str(input('Digite o seu nome: ')))
    while True:
        print('-'*60)
        print(f'{'MENU DO BANCO':^60}')
        print('-'*60)
        sleep(.5)
        print(f'1 - Criar conta')
        sleep(.5)
        print(f'2 - Depositar')
        sleep(.5)
        print(f'3 - Sacar')
        sleep(.5)
        print(f'4 - Verificar saldo')
        sleep(.5)
        print(f'5 - Fechar conta')
        sleep(.5)
        print(f'6 - Sair do menu')
        sleep(.5)
        r = leInteiro('Digite a opção desejada: ')
        if r == 1:
            minha_conta.criarConta()
        elif r == 2:
            quantia = leiaDinheiro('Digite a quantia a ser depositada: R$')
            minha_conta.depositar(quantia)
        elif r == 3:
            quantia = leiaDinheiro('Digite a quantia a ser sacada: R$')
            minha_conta.sacar(quantia)
        elif r == 4:
            minha_conta.verificarSaldo()
        elif r == 5:
            minha_conta.fecharConta()
        elif r == 6:
            print('Ok! Até logo')
            break
else:
    print('Ok! Até logo')


