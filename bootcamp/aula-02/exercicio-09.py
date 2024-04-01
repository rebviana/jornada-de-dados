# #### Números de Ponto Flutuante (`float`)
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

def celsius_para_fahrenheit():
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32

        print(f"A temperatura {celsius}°C em Fahrenheit é: {fahrenheit}°F.")
    except ValueError:
        print("Por favor, digite uma temperatura válida.")
    
if __name__ == "__main__":
    celsius_para_fahrenheit()
