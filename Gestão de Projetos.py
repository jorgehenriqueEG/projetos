import pandas as pd

def mostrar_guia(tipo_projeto):
    if tipo_projeto == "Software":
        print("Guia para Projetos de Software:")
        print("1. Planejamento")
        print("2. Desenvolvimento")
        print("3. Testes")
        print("4. Implantação")
        tabela = pd.DataFrame({
            "Fase": ["Planejamento", "Desenvolvimento", "Testes", "Implantação"],
            "Duração Estimada (%)": [20, 50, 20, 10]
        })
        print("\nTabela de Fases:")
        print(tabela)
    elif tipo_projeto == "Construção":
        print("Guia para Projetos de Construção:")
        print("1. Design")
        print("2. Aprovação de Licenças")
        print("3. Construção")
        print("4. Finalização")
        tabela = pd.DataFrame({
            "Fase": ["Design", "Aprovação de Licenças", "Construção", "Finalização"],
            "Duração Estimada (%)": [15, 10, 60, 15]
        })
        print("\nTabela de Fases:")
        print(tabela)
    else:
        print("Tipo de projeto não reconhecido. Tente 'Software' ou 'Construção'.")

def calcular_porcentagem(total, porcentagem):
    return (total * porcentagem) / 100

def main():
    print("Bem-vindo ao Sistema de Gestão de Projetos!")
    tipo_projeto = input("Digite o tipo de projeto (Software/Construção): ")
    mostrar_guia(tipo_projeto)

    calcular = input("\nDeseja calcular porcentagens? (sim/não): ").strip().lower()
    if calcular == "sim":
        total = float(input("Digite o valor total: "))
        porcentagem = float(input("Digite a porcentagem: "))
        resultado = calcular_porcentagem(total, porcentagem)
        print(f"O valor correspondente a {porcentagem}% de {total} é {resultado:.2f}.")

if __name__ == "__main__":
    main()