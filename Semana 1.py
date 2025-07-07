# Semana 1

# Exercício 1 
# Executar um código que retorne a soma dos múltiplos de 3 e 5 até o número n
# Ex: com n=10, os múltiplos são [3,5,6,9] e a soma é 23
print("Escolha um número:")
n = int(input())
multiplos = list()
for i in range (1,n):
    if i%3==0 or i%5==0:
        multiplos.append(i)

print("A soma dos múltiplos é", sum(multiplos))

# Exercício 2
# Criar um programa que leia uma lista de números e retorne a média dos números pares