import discord
import json
from discord.ext import commands, menus
import os

class MyMenu(menus.Menu):
    async def send_initial_message(self, ctx, channel):
        return await channel.send(f'Hello {ctx.author}')

    @menus.button('\N{THUMBS UP SIGN}')
    async def on_thumbs_up(self, payload):
        await self.message.edit(content=f'Thanks {self.ctx.author}!')

    @menus.button('\N{THUMBS DOWN SIGN}')
    async def on_thumbs_down(self, payload):
        await self.message.edit(content=f"That's not nice {self.ctx.author}...")

    @menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
    async def on_stop(self, payload):
        self.stop()

class Comandos(commands.Cog):

    def __init__(self, client: discord.Client):
        self._client = client
    
    @commands.dm_only()
    @commands.command(name='menu')
    async def menu_example(self, ctx):
        m = MyMenu()
        await m.start(ctx)

    @commands.dm_only()
    @commands.command(name='create')
    async def create(self, message):
        channel = message.channel
        await channel.send('Nome_do_personagem!')
        
        def check(m):
            return m.channel == channel

        msg = await self._client.wait_for('message', check=check)

        await channel.send(f'Nome do Personagem =====> {msg.content}')

    @commands.dm_only()
    @commands.command(name='tumb')
    async def tumb(self, message):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

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
