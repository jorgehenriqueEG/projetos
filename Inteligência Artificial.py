def chatbot():
    print("Olá! Eu sou um chatbot simples. Como posso ajudar você hoje?")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "tchau", "adeus"]:
            print("Chatbot: Foi bom conversar com você. Até logo!")
            break
        else:
            print("Chatbot: Desculpe, ainda estou aprendendo. Pode repetir?")

if __name__ == "__main__":
    chatbot()
