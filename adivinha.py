import random

def pulaLinha():
    print("\n")

def mostra(frase):
    print(frase)
    pulaLinha()

numeroPensado = random.randint(1, 30)
tentativas = 1

while tentativas <= 3:
    chute = int(input("Digite seu chute: "))

    if chute == numeroPensado:
        mostra(f"Você ACERTOU, o número pensado era {numeroPensado}")
        break  # quebra o looping do while4
    
    else:
        mostra("Você ERROU!")

    tentativas += 1

mostra("FIM")