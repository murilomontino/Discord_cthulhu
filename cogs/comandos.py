import discord
from discord.ext import commands

import DiscordAppBot

class Comandos(commands.Cog):

    def __init__(self, client):
        self._client : DiscordAppBot = client

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def play(self, mensage, *, game=None):
        if game == None:
            await mensage.send("!play + game")
            await mensage.send("Exemplo: !play coc")
        if game == "coc":
            #cthulhu_sheet.load_sheets
            await mensage.send("Hello World!")


    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def createCoC(self, message):
        await message.send("Criando Ficha de Cthlhu 7e")

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def id(self, message):
        _id = message.author.id
        await message.send(_id)

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def reg(self, message, *, nome_personagem=None):
        if nome_personagem == "None":
            await message.send("!reg + id_personagem")

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def list_personagens(self, message):
        embed = discord.Embed()
        embed.add_field(name="valor_um")
        await self.message.send(embed=embed)




def setup(client):
    client.add_cog(Comandos(client))
