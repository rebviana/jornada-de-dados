# #### Números de Ponto Flutuante (`float`)
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

def media():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        media = (numero1 + numero2) / 2

        print(f"A média dos números é: {media}")

    except ValueError:
        print("Por favor, digite números válidos.")

if __name__ == "__main__":
    media()
