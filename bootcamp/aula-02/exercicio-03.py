# #### Inteiros (`int`)
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

def multiplicar_numeros():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        resultado = numero1 * numero2

        print(f"O resultado da multiplicação de {numero1} e {numero2} é: {resultado}")
    except ValueError:
        print("Por favor, digite números válidos.")

if __name__ == "__main__":
    multiplicar_numeros()
