#Atividade 06

alunos = {}  


for i in range(3):
    nome = input(f"Informe o nome do  {i+1}º aluno: ")
    nota = float(input(f"Informe a nota do {i+1}º aluno: "))
    alunos[nome] = nota  

    soma_notas = 0  


for nome, nota in alunos.items():
    soma_notas += nota

    media_notas = soma_notas / len(alunos)  

    print(f"A média das notas é: {media_notas}")
