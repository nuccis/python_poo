#Sistema de Gerenciamento de Tarefas: Crie um aplicativo para gerenciar tarefas a fazer. Cada tarefa deve ter uma descrição, uma data de vencimento e um status (pendente, em andamento, concluída).
from datetime import datetime
from time import sleep

#Classes
class Tarefa:
    statusPossiveis = ['Pendente', 'Em Andamento', 'Concluído']

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


#Programa principal
tarefa01 = Tarefa('limparcasa','2024-03-02')
print(tarefa01.criacao)
print(tarefa01.vencimento)
print(tarefa01.status)