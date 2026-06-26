import random
from perguntas import perguntas

perguntas_sorteadas = random.sample(perguntas, 10)

pontos = 0

for perguntas in perguntas_sorteadas:
    print("\n" + pergunta["pergunta"])
    

print("Sejam bem-vindos ao Arraiá do cumpadi python! ")

print("Vamos testar o seu conhecimento junino, sô! ")

