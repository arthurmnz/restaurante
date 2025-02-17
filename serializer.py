import json
from models import *
from os.path import dirname, abspath

BASE_DIR = dirname(abspath(__file__))
RESTAURANTES_DIR = BASE_DIR + "/restaurantes"
AVALIACOES_DIR = BASE_DIR + "/avaliacoes"
USUARIOS_DIR = BASE_DIR + "/usuarios"

class Serializer:
    def serialize_restaurante(self,obj):
        file_name = f'{RESTAURANTES_DIR}/{obj}.json'
        with open(file_name,'w') as file:
            json.dump(obj.__dict__,file,indent=2)

    def deserialize_restaurante(self,name):
            file_name = f'{RESTAURANTES_DIR}/{name}.json'
            with open(file_name,'r') as file:
                dct = json.load(file)
                values = [v for v in dct.values()]
                return Restaurante(*values)
            
    def serialize_avaliacao(self,obj):
        file_name = f'{AVALIACOES_DIR}/{obj}.json'
        with open(file_name,'w') as file:
            json.dump(obj.__dict__,file,indent=2)

    def deserialize_avaliacao(self,name):
            file_name = f'{AVALIACOES_DIR}/{name}.json'
            with open(file_name,'r') as file:
                dct = json.load(file)
                values = [v for v in dct.values()]
                return Avaliacao(*values)
            
    def serialize_usuario(self,obj):
        file_name = f'{USUARIOS_DIR}/{obj}.json'
        with open(file_name,'w') as file:
            json.dump(obj.__dict__,file,indent=2)

    def deserialize_usuario(self,name):
            file_name = f'{USUARIOS_DIR}/{name}.json'
            with open(file_name,'r') as file:
                dct = json.load(file)
                values = [v for v in dct.values()]
                return Usuario(*values)
                