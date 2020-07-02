import discord
import pymongo
import json

from cogs.helping import helping as _help, brief as _brief, description as _description


from cogs import identidade # retorna nome do personagem, id_discord e sistema
from cogs import painel  # cria um painel para texto de maneira padrão

from ficha_rpg.TypeSheet import TypeSheet

from discord.ext import commands


class Database(commands.Cog):

    def __init__(self, client):

        # Cliente Discord
        self._client: discord.Client = client

        # Ponteiros de funções uteis, para facilitar o uso e diminuir a poluição do código
        self.ficha = TypeSheet()  # Classe que definirá qual tipo de ficha

        # Ponteiros de funçoes do banco de dados
        self.database = self._client.database  # banco de dados das fichas dos jogadores
        self.comando = self._client.comandos.find_one  # banco de dados de comandos para acessar atributos das fichas

        # Ponteiros de busca e atualização de atributos do banco de dados
        self.update = self.database.update_one  # atualiza atributo da ficha
        self.busca = self.database.find_one  # busca atributo da ficha

    ###########################################################################################
    # FUNCAO CRIA UM PAINEL COM VALORES CHAVES DA FICHA DEPENDENDO DE QUAL SISTEMA ESTEJA SENDO
    # USADO
    # EXEMPO:
    # NOME: Jogador
    # HP
    # MP
    # FORÇA DESTREZA CARISMA

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command(help=_help('myself'), description=_description('myself'), brief=_brief('myself'))
    async def myself(self, message):

        nome, _id, sistema = identidade(message, self.database)
        player = self.busca(_id)

        try:
            await message.send(embed=self.ficha.painel_do_jogador(cls=sistema, player=player))
        except:
            pass
        finally:
            return

    ###########################################################################################
    # FUNCAO PARA CAPTURAR UM ATRIBUTO

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command(help=_help('my'), description=_description('my'), brief=_brief('my'))
                    
    async def my(self, message, atributo: str = None, *, lixo=None):

        if atributo == None:
            await message.send(embed=painel("!my nome_do_atributo"))
            return

        nome_personagem, _id, tipo = identidade(message, self.database)

        try:
            comando = self.comando({}, {f'cthulhu_7e.{atributo}': 1, '_id': 0})['cthulhu_7e']
            endereco = '.'.join(comando[atributo])
            player = self.busca( _id, {'_id': 0, endereco: 1, })

            for rua in comando[atributo]:
                player = player[rua]

            texto_formatado = f"{atributo.upper()}  -->   {player}"
            await message.send(embed=painel(texto_formatado, nome_personagem, image=""))

        except:
            await message.send(embed=painel("Ficha não encontrada!"))

        finally:
            return

    ###########################################################################################
    # FUNCAO PARA ADICIONAR VALORES A UM ATRIBUTO E CONTROLÁ-LO
    # COMO HP, MP

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def add(self, message):
        game = discord.Game("Cthulhu 7e API")
        await self._client.change_presence(status=discord.Status.idle, activity=game)

    ###########################################################################################
    # FUNCAO PARA ATUALIZAR ATRIBUTOS DA FICHA NO BANCO DE DADOS update_atributo
    # ESTA FUNCAO SERA CHAMADA POR 3 OUTRAS
    # att
    # update
    # upd
    
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command(help=_help('update_atributo'), description=_description('update_atributo'), brief=_brief('update_atributo'))
    async def update_atributo(self, message: discord.message, atributo=None, valor=None):
        _id = str(message.author.id)

        if (atributo == None) or (valor == None):
            await message.send(embed=painel("Comando Inválido"))
            return

        comando_ficha = self.comando({"sistema": "cthulhu_7e"})['cthulhu_7e']

        try:
            comando: list = comando_ficha[atributo]
            comando = '.'.join(comando)

            try:
                valor = int(valor)
            except:
                pass
            finally:
                update = {'$set': {comando: valor}}

            self.update({'id_discord': _id, 'favorito': True}, update=update)
            await message.send(embed=painel("Valores att com sucesso!", "CTHULHU"))

        except KeyError:
            await message.send(embed=painel("Atributo Inválido"))
        finally:
            return


    ###########################################################################################


def setup(client):
    client.add_cog(Database(client))
