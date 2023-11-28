import pandas as pd


# Lista de perguntas

questoes = [
    ["Qual é o personagem que o jeff mais feda?",  "Seraphine", "Jana", "Ekko", "Todas as alternativas anteriores", 4],
    ["Como você descreveria o desempenho do Renan de Samira?", "Mediano", "Horrível", "Da pro gasto se ele não ficar respondendo o insta", "Horrível só que pela análise IMPECÁVEL do RB", 4],
    ["Se você é um nasus top e está contra um mordekaiser, qual tipo de resistência deve fazer?", "Armor", "Fé", "Resistência mágica", "Só god KNOWS", 1],
    ["Quando você está com dificuldades em dar dano qual é a melhor alternativa?", "O seu time não ajuda", "Só consequi dar 10k de dano", "Não tem time", "Tem player afk", 3],
    ["Boi e Kustela jogando duo no lolzin, a 100km/h, quem desiste antes?", "Kustela", "A riot", "O outro time(brincadeira, sabemos que é free pdl)", "Lucas", 2],
]

# criar dataframe do pandas
df = pd.DataFrame(questoes, columns=["Perguntas", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

# salvar no arquivo excel
df.to_excel("questoes.xlsx", index=False)

print("Perguntas inseridas com sucesso")