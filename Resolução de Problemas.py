# Resolução de Problemas

def resolver_problema(problema):
    """
    Função genérica para resolver problemas.
    Substitua esta lógica com a solução específica para o problema.
    """
    try:
        # Lógica para resolver o problema
        print(f"Resolvendo o problema: {problema}")
        solucao = "Solução encontrada"
        return solucao
    except Exception as e:
        print(f"Erro ao resolver o problema: {e}")
        return None

if __name__ == "__main__":
    problema = input("Descreva o problema: ")
    resultado = resolver_problema(problema)
    if resultado:
        print(f"Resultado: {resultado}")
    else:
        print("Não foi possível resolver o problema.")