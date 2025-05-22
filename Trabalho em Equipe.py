def dividir_tarefas(tarefas, membros):
    """
    Divide as tarefas igualmente entre os membros da equipe.
    
    :param tarefas: Lista de tarefas a serem realizadas.
    :param membros: Lista de membros da equipe.
    :return: Dicionário com membros como chaves e suas tarefas como valores.
    """
    distribuicao = {membro: [] for membro in membros}
    for i, tarefa in enumerate(tarefas):
        membro = membros[i % len(membros)]
        distribuicao[membro].append(tarefa)
    return distribuicao

def exibir_distribuicao(distribuicao):
    """
    Exibe a distribuição de tarefas de forma organizada.
    
    :param distribuicao: Dicionário com a distribuição de tarefas.
    """
    print("Distribuição de Tarefas:")
    for membro, tarefas in distribuicao.items():
        print(f"{membro}: {', '.join(tarefas)}")

if __name__ == "__main__":
    tarefas = ["Planejar", "Desenvolver", "Testar", "Documentar", "Revisar"]
    membros = ["Alice", "Bob", "Carlos"]
    
    distribuicao = dividir_tarefas(tarefas, membros)
    exibir_distribuicao(distribuicao)
