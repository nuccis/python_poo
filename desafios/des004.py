#Sistema de Gerenciamento de Contatos: Crie um programa que permita ao usuário adicionar, visualizar, atualizar e excluir contatos. Cada contato deve ter um nome, um número de telefone e um endereço de e-mail.
#Classes
class Contato:
    def __init__(self, nome:str, numero:str, email:str) -> None:
        self.nome = nome
        self.numero = numero
        self.email = email
      
    def __repr__(self) -> str:
        return(f'{type(self).__name__} ('
               f'nome = {self.nome}, '
               f'numero = {self.numero}, '
               f'email = {self.email})')        


class Agenda:
    def __init__(self) -> None:
        self.contatos = []
    
    def adicionar(self, contato:object) -> None:
        self.contatos.append(contato)

    def visualizar(self) -> None:
        print('-'*60)
        print(f'{'SUA LISTA DE CONTATOS':^60}')
        print('-'*60)
        if not self.contatos:
            print(f'{'VAZIA':^60}')
        else:
            for i, n in enumerate(self.contatos):
                print(f'{i+1}º {n.nome}: {n.numero} - {n.email} ')

    def atualizar(self, nome:str, numero:str, email:str) -> None:
        self.visualizar()
        ind = int(input('Digite o índice do contato desejado: '))
        if 0 < ind <= len(self.contatos):
            self.contatos[ind - 1].nome = nome
            self.contatos[ind - 1].numero = numero
            self.contatos[ind - 1].email = email
        else:
            print('Opção inválida')

    def excluir(self) -> None:
        ind = int(input('Digite o índice do contato que desja excluir: '))
        if 0 < ind <= len(self.contatos):
            self.contatos.pop(ind - 1)
        else:
            print('Opção inválida')


#Funções
def ler_contato() -> tuple[str, str, str]:
    nome = str(input('Nome do contato: ')).strip()
    numero = str(input('Número do contato: ')).strip()
    email = str(input('Email do contato: ')).strip()
    return nome, numero, email


#Programa principal
agenda_telefonica = Agenda()
for n in range(0, 2):
    nome, numero, email = ler_contato()
    agenda_telefonica.adicionar(Contato(nome,numero,email))

nome = 'a loka'
numero = '123'
email = '3456'
agenda_telefonica.excluir()
agenda_telefonica.visualizar()
