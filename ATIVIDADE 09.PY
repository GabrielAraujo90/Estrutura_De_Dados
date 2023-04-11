#Atividade 09

def ler_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade


def calcular_litros_de_gasolina(tempo, velocidade):
    distancia = tempo * velocidade
    litros_gasolina = distancia / 12
    return litros_gasolina


tempo, velocidade = ler_valores()
litros_gasolina = calcular_litros_de_gasolina(tempo, velocidade)

print("Velocidade média:", velocidade, "km/h")
print("Tempo gasto na viagem:", tempo, "horas")
print("Distância percorrida:", tempo * velocidade, "km")
print("Quantidade de litros utilizada na viagem:", litros_gasolina, "litros")
