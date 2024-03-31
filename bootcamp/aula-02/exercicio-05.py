# #### Inteiros (`int`)
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

def quadrado():
    try:
        numero = float(input("Digite um número: "))

        resultado = numero ** 2

        print(f"O quadrado de {numero} é: {resultado}")

    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    quadrado()
