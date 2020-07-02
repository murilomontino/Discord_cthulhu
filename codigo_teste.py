import pymongo
import json
import os
from abc import abstractmethod
from d20 import roll
from cogs.database import Database

#Template
class TypeSheet(object):

    @abstractmethod
    def rolagem_principal(self):
        pass

    @abstractmethod
    def painel(self):
        pass

    @abstractmethod
    def atack(self):
        pass

class Cthulhu_7e(TypeSheet):

    def roll_principal(self) :
        return roll('d100 [Cthulhu]')

class DnD_5e(TypeSheet):

    def roll_principal(self):
        return roll('d20 [D&D 5e]')

tipos_de_fichas = {
    'cthulhu_7e': Cthulhu_7e,
    'dnd_5e': DnD_5e
}

database  = pymongo.MongoClient('mongodb+srv://murilomontiono:'
                                     'kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/'
                                     'rpg?retryWrites=true&w=majority')['RPG']['sheets']



a = Database.get_commands(Database)
for c in a:
    print(c.help)


def main():
   
    jogador = dict(database.find_one({'id_discord': 'ficha_teste'}, {'_id':0}))
    nome = jogador['nome_discord']
    nome_personagem = jogador['fichamento']['nome_personagem']
    diretorio2 = "ProjectsPython\\DiscordApp\\Bot\\database_json\\" + nome + '.json'
    with open(diretorio2, 'a') as json_file:
        json.dump(jogador, json_file, indent=4)


if __name__ == '__main__':
    main()
