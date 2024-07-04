    
class Usuarios():
    usuarios={}
    def __init__(self,nome,nickname,senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha
        Usuarios.usuarios[nickname]=self