def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    choice = input("Escolha uma opção (1/2): ")

    if choice == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()