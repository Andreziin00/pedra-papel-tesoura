class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.flag = ""

    #a=pedra  b=papel  c==tesoura
    def pedra(self):
        if self.flag=="":print('jogou pedra')
        self.flag="a"
    def papel(self):
        if self.flag=="":print('jogou papel')
        self.flag="b"
    def tesoura(self):
        if self.flag=="":print('jogou tesoura')
        self.flag="c"
        