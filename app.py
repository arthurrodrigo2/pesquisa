# Lista
cidades = ["Plano Piloto", "Samambaia", "Recanto das Emas", "Guará", "Santa Maria", "Águas Claras", "Planaltina", "Sobradinho", "Formosa", "Luziania", "Granja do Torto", "Caldas Novas", "Ceilandia", "Asa Sul", "Asa Norte", "Taguatinga", "Mestre D'armas", "Brasilinha", "Lago Sul", "Fercal", "Varjão", "Planaltina"]

# usuário informa um nome que deseja procurar
cidade = input("Informe o nome da cidade que deseja procurar: ")

# informa a quantidade de vezes que o termo foi achado
quantidade = cidades.count(cidade)

# Exibe o resultado na tela
if cidade in cidades:
    print(f"{cidade} foi encontrada na lista {quantidade} vezes.")
else:
    print(f"{cidade} não foi encontrada.")