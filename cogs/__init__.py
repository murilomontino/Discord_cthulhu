from discord import Embed
from template import COMANDO
from d20 import roll as r

FICHAS_IN_GAME = {

}

CONFIG = {
    
}

COMANDOs = COMANDO

def painel(description, author='CTHULHU', image="https://cdn.imgbin.com/7/11/13/"
                                                   "imgbin-cthulhu-lovecraftian-horror-computer-icons-rpg-maker-mv-others"
                                                   "-e3H7mww7JVhF6Bhu2UPgNvhzp.jpg"):
        embed = Embed()
        embed.set_author(name=author, icon_url=image)
        embed.description = description

        return embed

def identidade(message, database):

    def id():
        identidade = {'id_discord': str(message.author.id),
                      'favorito': True
                      }
        return identidade

    _id = id()
    nome_personagem = 'fichamento.nome_personagem'

    try:
        valores = database.find_one(_id, {'_id': 0, nome_personagem: 1, 'sistema': 1})
    except:
        return 'Erro'

    nome = valores['fichamento']['nome_personagem']
    sistema = valores['sistema']

    return (nome, _id, sistema)

def roll(message, author='CTHULHU'):
    rolagem = str(r(message))
    rolagem = painel(description=rolagem, author=author)
    return rolagem