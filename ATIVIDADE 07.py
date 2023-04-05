#Atividade 07

import numpy as np


matriz = np.array([[3, 4, 1], [3, 1, 2]])

soma_numeros = 0  


for linha in matriz:
    for elemento in linha:
        soma_numeros += elemento

print(f"A soma de todos os números da matriz é: {soma_numeros}")
