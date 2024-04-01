# #### Números de Ponto Flutuante (`float`)
# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

def adicao_numeros():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        resultado = numero1 + numero2

        print(f"A adição de {numero1} e {numero2} é: {resultado}")
    
    except ValueError:
        print("Por favor, digite números flutuantes válidos.")

if __name__ == "__main__":
    adicao_numeros()

    