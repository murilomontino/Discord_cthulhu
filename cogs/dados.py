import discord
import pymongo

from d20 import roll
from cogs import painel, identidade
from ficha_rpg.TypeSheet import TypeSheet
from discord.ext import commands

class Dados(commands.Cog):

    def __init__(self, client: discord.AutoShardedClient):
        # Cliente Discord
        self._client = client
        self.database = self._client.database
        self.ficha = TypeSheet()

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command(name='r')
    async def rolagem_principal(self, message:discord.message, atributo=None, *, lixo=None):

        nome, _id, tipo = identidade(message, self.database)
        await message.channel.send('teste bem sucedido')

        if atributo== None:
            await message.channel.send(embed=painel(self.ficha.rolagem_principal(cls=tipo), author=nome))




def setup(client):
    client.add_cog(Dados(client))
