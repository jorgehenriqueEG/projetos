# Adaptabilidade.py

def adaptabilidade(experiencia, aprendizado):
    """
    Calcula o nível de adaptabilidade com base na experiência e aprendizado.

    Args:
        experiencia (int): Nível de experiência (0 a 10).
        aprendizado (int): Nível de aprendizado (0 a 10).

    Returns:
        str: Mensagem indicando o nível de adaptabilidade.
    """
    if not (0 <= experiencia <= 10 and 0 <= aprendizado <= 10):
        return "Os valores devem estar entre 0 e 10."

    adaptabilidade = (experiencia + aprendizado) / 2

    if adaptabilidade >= 8:
        return "Alta adaptabilidade."
    elif adaptabilidade >= 5:
        return "Adaptabilidade moderada."
    else:
        return "Baixa adaptabilidade."


# Exemplo de uso
if __name__ == "__main__":
    experiencia = int(input("Informe o nível de experiência (0-10): "))
    aprendizado = int(input("Informe o nível de aprendizado (0-10): "))
    resultado = adaptabilidade(experiencia, aprendizado)
    print(resultado)