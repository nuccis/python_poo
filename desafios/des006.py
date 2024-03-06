#Sistema de Gerenciamento de Tarefas: Crie um aplicativo para gerenciar tarefas a fazer. Cada tarefa deve ter uma descrição, uma data de vencimento e um status (pendente, em andamento, concluída).
from datetime import datetime, date
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
        if isinstance(value, date):
            self._vencimento = value         
        else:
            self._vencimento = datetime.fromisoformat(value).date()
            


#classes
class Agenda:
    def __init__(self, atividades:list=[]) -> None:
        self.atividades = atividades
    
    def mostrarTarefas(self):
        print('-^'*30)
        print(f'{'TODAS AS SUAS TAREFAS':^60}')
        print('-^'*30)
        if self.atividades:
            for i, atv in enumerate(self.atividades):
                print(f'[{i+1}] {atv.descricao}: {atv.criacao} -> {atv.vencimento} - {atv.status}')
        else:
            print(f'{'Vazio':^60}')
        
    def alterarStatus(self, opc, sts):
        print(f'Alterando o status da tarefa [{opc}] - {self.atividades[opc - 1].descricao}')
        self.atividades[opc - 1].status = Tarefa.statusPossiveis[sts - 1]

    def excluirTarefa(self, opc):
        print(f'Excluindo a tarefa [{opc}] - {self.atividades[opc - 1].descricao}')
        self.atividades.pop(opc - 1)
        
    def adicionarTarefa(self, descricao, vencimento, status):
        print(f'Adicionando a tarefa - {descricao}')
        self.atividades.append(Tarefa(descricao, vencimento, status))


#Funções
def leInteiro(msg:str, rng:int) -> int:
    while True:
        try:
            opc = int(input(msg))
            if opc not in range(1, rng):
                raise ValueError
            break
        except ValueError:
            print('\033[0;31mErro! Digite uma opção válida.\033[m')
    return opc

def leData(msg:str):
    while True:
        try:
            data = str(input(msg))
            data_iso = datetime.fromisoformat(data).date()
            break
        except ValueError:
            print('\033[0;31mErro! Digite o formato de data correto.\033[m')
    return data_iso
            

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
    
    r = leInteiro('Escolha uma opção: ', 6)
    if r == 1:
        minha_agenda.mostrarTarefas()
    elif r == 2:
        minha_agenda.mostrarTarefas()
        if minha_agenda.atividades:
            opc = leInteiro('Escolha uma atividade: ', 6)
            print(f'escolha entre os status:\n'
                  f'[1] - {Tarefa.statusPossiveis[0]}\n'
                  f'[2] - {Tarefa.statusPossiveis[1]}\n'
                  f'[3] - {Tarefa.statusPossiveis[2]}')
            sts = leInteiro('Escolha um status: ', 4)
            minha_agenda.alterarStatus(opc, sts)
    elif r == 3:
        minha_agenda.mostrarTarefas()
        if minha_agenda.atividades:
            opc = leInteiro('Escolha uma atividade: ', 6)
            minha_agenda.excluirTarefa(opc)
    elif r == 4:
        minha_agenda.mostrarTarefas()
        desc = str(input('Digite a descrição da tarefa: '))
        dataVenc = leData('Data de Vencimento (YYYY-MM-DD): ')
        print(f'escolha entre os status:\n'
                  f'[1] - {Tarefa.statusPossiveis[0]}\n'
                  f'[2] - {Tarefa.statusPossiveis[1]}\n'
                  f'[3] - {Tarefa.statusPossiveis[2]}')
        opc = leInteiro('Escolha um status: ', 4)
        sts = Tarefa.statusPossiveis[opc - 1]
        minha_agenda.adicionarTarefa(desc, dataVenc, sts)

    else:
        print('Ok! Até logo')
        break
