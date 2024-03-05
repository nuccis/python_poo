#Sistema de Gerenciamento de Tarefas: Crie um aplicativo para gerenciar tarefas a fazer. Cada tarefa deve ter uma descrição, uma data de vencimento e um status (pendente, em andamento, concluída).
from datetime import datetime
from time import sleep

#Classes
class Tarefa:
    statusPossiveis = ['Pendente', 'Em Andamento', 'Concluída']

    def __init__(self, descricao:str, vencimento:datetime, status:str=statusPossiveis[0]) -> None:
        self.descricao = descricao
        self.criacao = datetime.today().date().isoformat()
        self.vencimento = vencimento
        self.status = status
    
    @property
    def vencimento(self):
        return self._vencimento
    
    @vencimento.setter
    def vencimento(self, value):
        self._vencimento = datetime.fromisoformat(value).date()


#classes
class Agenda:
    def __init__(self, atividades:list=[]) -> None:
        self.atividades = atividades
    
    def mostrarTarefas(self):
        print('-^'*30)
        print(f'{'TODAS AS SUAS TAREFAS':^60}')
        print('-^'*30)
        for i, atv in enumerate(self.atividades):
            print(f'[{i+1}] {atv.descricao}: {atv.criacao} -> {atv.vencimento} - {atv.status}')
        
    def alterarStatus(self):
        pass

    def excluirTarefa(self):
        pass

    def adicionarTarefa(self):
        pass


#Funções
def leInteiro(msg) -> int:
    while True:
        try:
            opc = int(input(msg))
            if opc not in range(1, 6):
                raise ValueError
            break
        except ValueError:
            print('\033[0;31mErro! Digite uma opção válida.\033[m')
    return opc


#Programa principal
tarefa01 = Tarefa('limparcasa','2024-03-06')
tarefa02 = Tarefa('Ir ao mercado','2024-04-12')
tarefa03 = Tarefa('Caminhar', '2024-05-01', 'Em Andamento')
tarefa04 = Tarefa('Comprar blusa', '2024-02-01', 'Concluída')
lista_de_tarefas = [tarefa01, tarefa02, tarefa03, tarefa04]
minha_agenda = Agenda(lista_de_tarefas)

while True:
    print('-*'*30)
    print(f'{'GERENCIAMENTO DE TAREFAS':^60}')
    print('-*'*30)
    print('[1] Mostrar todas as tarefas\n'
            '[2] Alterar status\n'
            '[3] Excluir tarefa\n'
            '[4] Adicionar tarefa\n'
            '[5] Sair do menu')
    
    r = leInteiro('Escolha uma opção: ')
    if r == 1:
        minha_agenda.mostrarTarefas()
    elif r == 2:
        pass
    elif r == 3:
        pass
    elif r == 4:
        pass
    else:
        print('Ok! Até logo')
        break
