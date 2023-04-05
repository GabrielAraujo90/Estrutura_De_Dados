#Atividade 05

lista_de_numeros = []  



for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_de_numeros.append(numero)  

soma = 0  


for numero in lista_de_numeros:
    soma += numero

print(f"A soma dos números digitados é: {soma}")
