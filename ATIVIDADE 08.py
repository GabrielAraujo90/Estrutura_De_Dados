#atividade 08

def ler_temperatura():
    temperatura = float(input("Digite a temperatura em Celsius: "))
    return temperatura

def calcular_fahrenheit(celcius):
    fahrenheit = (9 * celcius + 160) / 5
    return fahrenheit


def mostrar_resultado(fahrenheit):
    print("A temperatura em Fahrenheit é:", fahrenheit)
   

temperatura_celsius = ler_temperatura()
temperatura_fahrenheit = calcular_fahrenheit(temperatura_celsius)
mostrar_resultado(temperatura_fahrenheit)
