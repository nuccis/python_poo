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

    def depositar(self):
        pass

    def sacar(self):
        pass

    def verificarSaldo(self):
        pass

    def fecharConta(self):
        pass
    
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
minha_conta.verificarConta()
minha_conta.criarConta()
minha_conta.verificarConta()