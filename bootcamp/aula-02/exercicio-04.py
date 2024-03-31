# #### Inteiros (`int`)
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

def divisao_inteira():
    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

        resultado = numero1 // numero2
        print(f"A divisão inteira de {numero1} por {numero2} é: {resultado}")
    
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    divisao_inteira()
