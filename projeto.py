import random
import time
import msvcrt
from perguntas import perguntas

perguntas_sorteadas = random.sample(perguntas, 10)

def resposta_com_tempo(segundos):
    print(f"\nVocê tem {segundos} segundos para responder.")

    inicio = time.time()
    resposta = ""

    while time.time() - inicio < segundos:
        if msvcrt.kbhit():
            tecla = msvcrt.getwch()

            if tecla == "\r":  # Enter
                print()
                return resposta

            resposta += tecla
            print(tecla, end="", flush=True)

    print("\n⏰ Tempo esgotado!")
    return None

pontos = 0

print("Sejam bem-vindos ao Arraiá do cumpadi python! ")
print("Vamos testar o seu conhecimento junino, sô! ")

for perguntas in perguntas_sorteadas:
    print("\n" + perguntas["pergunta"])
    
    for i, alternativa in enumerate(perguntas["alternativas"], start=1):
        print(f"{i} - {alternativa}")

    resposta = resposta_com_tempo(10)

    if resposta is None:
        print("❌ Você perdeu essa pergunta!")
        continue

    resposta = int(resposta)

    if resposta == perguntas["resposta"]:
        print("✅ Acertou! ")
        pontos  += 10
    else:
        print("❌ Errou!")

print("\nFim do jogo!")
print(f"Sua pontuação foi: {pontos}")

if pontos >= 90:
    print("🏆 Mestre Junino!")

elif pontos >= 70:
    print("🌽 Arretado!")

elif pontos >= 50:
    print("🎉 Dançarino!")

else:
    print("🤠 Continue treinando!")


    

