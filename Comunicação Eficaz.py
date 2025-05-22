
def comunicar_eficazmente(mensagem, destinatario):
    """
    Envia uma mensagem de forma eficaz para o destinatário.
    
    Args:
        mensagem (str): A mensagem a ser enviada.
        destinatario (str): O nome do destinatário.
    """
    if not mensagem or not destinatario:
        print("Erro: Mensagem ou destinatário inválido.")
        return
    
    print(f"Enviando mensagem para {destinatario}...")
    print(f"Mensagem: {mensagem}")
    print("Mensagem enviada com sucesso!")

if __name__ == "__main__":
    mensagem = input("Digite a mensagem que deseja enviar: ")
    destinatario = input("Digite o nome do destinatário: ")
    comunicar_eficazmente(mensagem, destinatario)
