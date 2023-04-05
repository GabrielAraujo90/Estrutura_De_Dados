#Atividade 04

carros = []

while True:
    print("Opções disponíveis:")
    print("1 - Adicionar veículo")
    print("2 - Consultar veículos")
    print("3 - Apagar veículo")
    print("4 - Finalizar")

   
    escolha = input("Escolha uma opção: ")

    
    if escolha == "1":
        
        modelo = input("Informe o modelo do veículo: ")
        marca = input("Informe a marca do veículo: ")
        ano = input("Informe o ano do veículo: ")
        carros.append({"modelo": modelo, "marca": marca, "ano": ano})
        print("Veículo adicionado com sucesso.")
    elif escolha == "2":
        
        if not carros:
            print("Não há veículos cadastrados.")
        else:
            for i, carro in enumerate(carros):
                print(f"{i+1} - {carro['modelo']} {carro['marca']} ({carro['ano']})")
    elif escolha == "3":
      
        if not carros:
            print("Não há veículos cadastrados.")
        else:
            indice = int(input("Informe o número do veículo que deseja apagar: "))
            if indice < 1 or indice > len(carros):
                print("Número inválido.")
            else:
                carros.pop(indice-1)
                print("Veículo removido com sucesso.")
    elif escolha == "4":
       
        print("Programa finalizado.")
        break
    else:
       
        print("Opção inválida. Escolha uma opção válida.")
