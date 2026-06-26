import random
from perguntas import perguntas

perguntas_sorteadas = random.sample(perguntas, 10)

pontos = 0

for perguntas in perguntas_sorteadas:
    print("\n" + perguntas["pergunta"])
    

print("Sejam bem-vindos ao Arraiá do cumpadi python! ")

print("Vamos testar o seu conhecimento junino, sô! ")

for i, alternativa in enumerate(perguntas["alternativas"], start=1):
    print(f"{i} - {alternativa}")

resposta = int(input("digite sua resposta: "))

if resposta == perguntas["resposta"]:
    print("acertou")
    pontos  += 10
else:
    print("errou")

print("\nFim do jogo!")
print(f"Sua pontuação foi: {pontos}")

if pontos >= 90:
    print("Mestre Junino!")

elif pontos >= 70:
    print("Arretado!")

elif pontos >= 50:
    print("Dançarino!")

else:
    print("Continue treinando!")


    

