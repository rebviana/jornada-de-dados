# #### Números de Ponto Flutuante (`float`)
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

def potencia():
    try:
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))

        resultado = base ** expoente

        print(f"O resultado de {base} elevado a {expoente} é: {resultado}")
    
    except ValueError:
        print("Por favor, digite números válidos para a base e o expoente.")

if __name__ == "__main__":
    potencia()
