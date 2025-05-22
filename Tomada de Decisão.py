
def tomada_de_decisao(criterios):
    """
    Função para auxiliar na tomada de decisão com base em critérios e pesos.
    
    :param criterios: Lista de tuplas no formato (critério, peso, valor).
                      Exemplo: [("Custo", 0.4, 7), ("Qualidade", 0.6, 9)]
    :return: Pontuação final calculada.
    """
    pontuacao_final = 0
    for criterio, peso, valor in criterios:
        pontuacao_final += peso * valor
    return pontuacao_final

if __name__ == "__main__":
    criterios = [
        ("Custo", 0.4, 7),  
        ("Qualidade", 0.6, 9)  
    ]
    resultado = tomada_de_decisao(criterios)
    print(f"A pontuação final para a decisão é: {resultado}")
