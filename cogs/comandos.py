import discord
import json
from discord.ext import commands
import os


class Comandos(commands.Cog):

    def __init__(self, client: discord.Client):
        self._client = client
    
    @commands.command()
    async def new_nameComando(self, message, comando=None, *, nome=None):
        print(comando)
        print(nome)
        try:
            self._client.novo_nome_comando(comando=comando, nome=nome)
            await message.channel.send('Teste bem sucedido!')
            
        except:
            await message.channel.send('Comando inválido!')
        finally:
            return

 
def setup(client):
    client.add_cog(Comandos(client))
