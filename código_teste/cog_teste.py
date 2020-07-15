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

# [{menu1}, {menu2}, {menu3}, {menu4}]
database = pymongo.MongoClient('mongodb+srv://murilomontiono:'
                                     'kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/'
                                     'rpg?retryWrites=true&w=majority')['RPG']['sheets']

def create_menu():
    template = database.find_one({'template':'cthulhu_7e'}, {'template':0})
    pass

def painel(description, author='CTHULHU', image="https://cdn.imgbin.com/7/11/13/"
           "imgbin-cthulhu-lovecraftian-horror-computer-icons-rpg-maker-mv-others"
           "-e3H7mww7JVhF6Bhu2UPgNvhzp.jpg"):
    embed : discord.Embed = discord.Embed()
    
    embed.set_author(name=author, icon_url=image)
    embed.description = description
    
    embed.add_field(name='Teste', value=5, inline=True)
    
    for indice, field in enumerate(embed._fields):
        print(indice)

    return embed


class MyMenu(menus.Menu):
    
    async def send_initial_message(self, ctx, channel):
        return await channel.send(f'Hello {ctx.author}')

    @menus.button(emoji=emoji['0'])
    async def on_digit_zero(self, payload):
        await self.message.edit(content=f'Thanks {self.ctx.author}!')

    @menus.button(emoji=emoji['1'])
    async def on_thumbs_down(self, payload):
        await self.message.edit(content=f"That's not nice {self.ctx.author}...")

    @menus.button(emoji=emoji['2'])
    async def on_two(self, payload):
        await self.message.edit(content=f"That's not nice {self.ctx.author}...")

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
    
    @commands.command(name='menu')
    async def menu_example(self, ctx):
        m = MyMenu()
        await m.start(ctx)
    
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
