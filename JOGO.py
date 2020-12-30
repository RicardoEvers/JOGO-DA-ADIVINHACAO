from random import randint
print('#' * 22)
print('JOGO DA ADIVINHAÇÃO')
print('#' * 22)
print('ESCOLHA A DIFICULDADE:')
print('#' * 22)
dif = int(input('(1)FÁCIL (2)MÉDIO (3)DIFÍCIL (4) IMPOSSÍVEL\n'))
chance = 0
num = randint(1, 101)
print('#' * 37)
print('A RESPOSTA É UM NÚMERO ENTRE 1 E 100')
print('#' * 37)
if dif == 1:
    chance = 10
elif dif == 2:
    chance = 8
elif dif == 3:
    chance = 6
elif dif == 4:
    chance = 1

for n in range(1, chance + 1):
    tentativa = int(input(f'TENTATIVA {n}/{chance}: '))
    maior = num > tentativa
    menor = num < tentativa

    if tentativa == num:
        print('#' * 20)
        print('VOCÊ VENCEU O JOGO')
        print('#' * 20)
        break
    elif maior:
        if n == chance:
            break
        print('TENTE UM NÚMERO MAIOR')

    elif menor:
        if n == chance:
            break
        print('TENTE UM NÚMERO MENOR')
if tentativa != num:
    print('#' * 20)
    print('VOCÊ PERDEU O JOGO')
    print('#' * 20)
    print(f'O NÚMERO ERA {num}')
    print('#' * 20)
print('###FIM###')
