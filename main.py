from classes import Jogador

def resultado(p1, p2):
        if p1.flag=="" or p2.flag=="":
            print("nao fez nenhuma escolha!")
        if p1.flag=="a" and p2.flag=="b" or p1.flag=="b" and p2.flag=="c" and p1.flag=="c" and p2.flag=="a":
            print(f'{p2.nome} ganhou!')
            return
        elif p1.flag == p2.flag:
            print('empate')
            return
        else:
            print(f'{p1.flag} ganhou!')
            return

def iniciarJogo(p1,p2):
    print('digite "a" para pedra')
    print('digite "b" para papel')
    print('digite "c" para tesoura\n')

    p1.flag = input(f'digite a jogada de {p1.nome}: ')
    p2.flag = input(f'digite a jogada de {p2.nome}: ')

    if p1.flag=='a':
        p1.pedra()
    if p1.flag=='b':
        p1.papel()
    if p1.flag=='c':
        p1.tesoura()

    
    if p2.flag=='a':
        p2.pedra()
    if p2.flag=='b':
        p2.papel()
    if p2.flag=='c':
        p2.tesoura()


p1_name = input('digite o nome do jogador 1: ')
p2_name = input('digite o nome do jogador 2: ')

p1 = Jogador(p1_name)
p2 = Jogador(p2_name)

iniciarJogo(p1, p2)
resultado(p1, p2)

