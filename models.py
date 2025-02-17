class Usuario:
    def __init__(self,username):
        self.username = username

    def __str__(self):
        return f"{self.username}"
    
class Restaurante:
    def __init__(self, name:str, avaliacoes = [], nota = None):
        self.name = name
        self.avaliacoes = avaliacoes
        self.nota_geral = nota

    def __str__(self):
        return f"{self.name}"

    def add_avaliacao(self,avaliacao):
        self.avaliacoes.append(avaliacao.__dict__)
        if self.nota_geral != None:
            soma = sum(avaliacao_parcial['nota'] for avaliacao_parcial in self.avaliacoes)
            self.nota_geral = soma / len(self.avaliacoes)
        else:
            self.nota_geral = avaliacao.nota

class Avaliacao:
    def __init__(self, nota, descricao, username, restaurante):
        self.autor = username
        self.restaurante = restaurante
        self.nota = nota
        self.descricao = descricao

    def __str__(self):
        return f"{self.autor}|{self.restaurante}"