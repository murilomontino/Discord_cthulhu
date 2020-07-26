import discord
import json
import pymongo
from discord.ext import commands, menus
import os

emoji = {
    "0": "0️⃣",
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣",
    "10": "🔟",

    "seguinte": "➡",
    "anterior": "⬅",

    "play": "▶",
    "pause": "⏸",
    "stop": "⏹",

    "confirmar": "🟢",
    "negar": "🔴",
    "editar": "🔵",

    "dinheiro": "💲",
}

emoji_number = {
    "0️⃣": 0,
    "1️⃣": 1,
    "2️⃣": 2,
    "3️⃣": 3 ,
    "4️⃣": 4,
    "5️⃣": 5,
    "6️⃣": 6,
    "7️⃣": 7,
    "8️⃣": 8,
    "9️⃣": 9,
    "🔟": 10
}


database = pymongo.MongoClient('mongodb+srv://murilomontiono:'
                                     'kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/'
                                     'rpg?retryWrites=true&w=majority')['RPG']['sheets']

def create_menu(author='CTHULHU', image="https://cdn.imgbin.com/7/11/13/"
           "imgbin-cthulhu-lovecraftian-horror-computer-icons-rpg-maker-mv-others"
           "-e3H7mww7JVhF6Bhu2UPgNvhzp.jpg"):

    painel : discord.Embed = discord.Embed()
    painel.set_author(name=author, icon_url=image)
    
    menu = dict()
    template = database.find_one({'template':'cthulhu_7e'}, {'_id':0, 'template':0})
    description = ""
    
    for indice, option in zip(emoji_number, template):
        description += f"{indice} {option} \n"
        menu[emoji_number[indice]] = option

    painel.description = description

    return (menu, painel)

def painel(description, author='CTHULHU', image="https://cdn.imgbin.com/7/11/13/"
           "imgbin-cthulhu-lovecraftian-horror-computer-icons-rpg-maker-mv-others"
           "-e3H7mww7JVhF6Bhu2UPgNvhzp.jpg"):
    embed : discord.Embed = discord.Embed()
    
    embed.set_author(name=author, icon_url=image)
    embed.description = description
    
    return embed

class MenuConfirmation(menus.Menu):
    @menus.button(emoji=emoji['confirmar'])
    async def confirmar(self, payload):
        await self.message.edit(content=f"That's not nice {self.ctx.author}...")
    
    @menus.button(emoji=emoji['negar'])
    async def negar(self, payload):
       self.clear_buttons()
       await self.message.clear_reactions()
       await self.update(payload)

class Comandos(commands.Cog):

    def __init__(self, client: discord.Client):
        self._client = client
    

    @commands.guild_only()
    @commands.command(name='create')
    async def create(self, message):
        channel = message.channel
        embed = painel('Nome do Personagem')
        resposta = discord.Embed()
        cthulhu_msg = await channel.send(embed=embed)
        cthulhu_resposta = await channel.send(embed=resposta)

        def check(m):
            return m.channel == channel
        embed.description = "Suceffuly"
        msg = await self._client.wait_for('message', check=check)
        resposta.description = msg.content
        await cthulhu_resposta.edit(embed=resposta)
        await msg.delete()
        await cthulhu_msg.edit(embed=embed)

    @commands.has_permissions()
    @commands.command()
    async def text(self, message):
        
        channel = message.channel
        guild = message.guild
        me = message.me
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }

        channel = await guild.create_text_channel('secret', overwrites=overwrites)

    @commands.command(name="teste")
    async def t(self, message):
        menu, embed = create_menu()
        print(menu)
        await message.channel.send(embed=embed)

    @commands.dm_only()
    @commands.command(name='tumb')
    async def tumb(self, message):
        channel = message.channel
        embed = painel('Send me that 👍 reaction, mate')
        await channel.send(embed=embed)

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await self._client.wait_for('reaction_add', timeout=60.0, check=check)
        except TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

def setup(client):
    client.add_cog(Comandos(client))
