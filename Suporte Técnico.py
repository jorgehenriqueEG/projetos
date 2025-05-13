from datetime import datetime, timedelta

class SuporteTecnico:
    def __init__(self):
        self.agenda = []

    def adicionar_suporte(self, descricao, duracao_estimada_minutos):
        horario_inicio = datetime.now()
        horario_fim = horario_inicio + timedelta(minutes=duracao_estimada_minutos)
        suporte = {
            "descricao": descricao,
            "horario_inicio": horario_inicio.strftime("%Y-%m-%d %H:%M:%S"),
            "horario_fim": horario_fim.strftime("%Y-%m-%d %H:%M:%S"),
            "duracao_estimada": f"{duracao_estimada_minutos} minutos"
        }
        self.agenda.append(suporte)
        print(f"Suporte adicionado: {descricao}")

    def listar_agenda(self):
        if not self.agenda:
            print("A agenda está vazia.")
        else:
            print("Agenda de Suporte Técnico:")
            for idx, suporte in enumerate(self.agenda, start=1):
                print(f"{idx}. {suporte['descricao']}")
                print(f"   Início: {suporte['horario_inicio']}")
                print(f"   Fim: {suporte['horario_fim']}")
                print(f"   Duração Estimada: {suporte['duracao_estimada']}")
                print("-" * 30)

# Exemplo de uso
if __name__ == "__main__":
    suporte_tecnico = SuporteTecnico()
    suporte_tecnico.adicionar_suporte("Configuração de impressora", 30)
    suporte_tecnico.adicionar_suporte("Atualização de software", 45)
    suporte_tecnico.listar_agenda()