class Jogo():
    jogos=[]
    def __init__(self,nome,categoria,plataforma):
        self.nome=nome
        self.categoria=categoria
        self.plataforma=plataforma
        Jogo.jogos.append(self)
    def __str__(self) -> str:
        return self.nome
    
class Usuarios():
    def __init__(self,nome,nickname,senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha