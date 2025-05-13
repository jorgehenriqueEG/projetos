import time

def cronometro():
    try:
        tempo = int(input("Digite o tempo em segundos: "))
        for t in range(tempo, 0, -1):
            print(f"Tempo restante: {t} segundos", end="\r")
            time.sleep(1)
        print("\nTempo esgotado!")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    cronometro()