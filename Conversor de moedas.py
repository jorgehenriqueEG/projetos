# Conversor de Moedas

def converter_moeda(valor, taxa_cambio):
    """
    Converte um valor de uma moeda para outra com base na taxa de câmbio.
    
    :param valor: Valor na moeda de origem.
    :param taxa_cambio: Taxa de câmbio para a moeda de destino.
    :return: Valor convertido na moeda de destino.
    """
    return valor * taxa_cambio

def main():
    print("Bem-vindo ao Conversor de Moedas!")
    
    try:
        valor = float(input("Digite o valor na moeda de origem: "))
        taxa_cambio = float(input("Digite a taxa de câmbio (exemplo: 5.25 para BRL/USD): "))
        
        valor_convertido = converter_moeda(valor, taxa_cambio)
        print(f"Valor convertido: {valor_convertido:.2f}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()