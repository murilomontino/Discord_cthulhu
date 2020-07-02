import discord
import pymongo
import json

from discord.ext import commands

class Efeito_Sonoro(commands.Cog):

    def __init__(self, client):
        self._client = client
        with open('.\\database_json\\efeito_sonoro.json', 'r') as json_file:
            self.link_efeito_sonoro = json.load(json_file)
    
    @commands.command()
    async def play(self):
        pass
    
    @commands.command(name="#")
    async def sustenido(self, message):
        await message.channel.send('play')
        

    

def setup(client):
    client.add_cog(Efeito_Sonoro(client))
