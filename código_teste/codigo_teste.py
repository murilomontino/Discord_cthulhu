import pymongo
import json
import os
import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or
from abc import abstractmethod
from d20 import roll




class DiscordAppBot(AutoShardedBot):
    
    def __init__(self):
        super().__init__(command_prefix='!', case_insensitive=True)

    async def on_guild_join(self, guild):
        print(guild.id)
        return

    async def process_commands(self, message):
          
        if message.author.bot:
            return
               
        ctx = await self.get_context(message)
        await self.invoke(ctx)        

    async def on_ready(self):
        print('CTHULHU ONLINE - OLÁ MUNDO')
        print('-----PR------')
        await self.change_presence(activity=discord.Streaming(name='!help', url='www.google.com.br'))
    
    async def on_message(self, message):
       await self.process_commands(message)
       

MODULOs = ['cog_teste']
TOKEN = "NzE1NjgyMDcxOTQyNTI5MTM0.XuW_-w.UGFoK5PZ38PADlRy3qyrNGJk_1Q"
CLIENT = DiscordAppBot()

for modulo in MODULOs:
    CLIENT.load_extension(modulo)

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


def main():
   CLIENT.run(TOKEN)

if __name__ == '__main__':
    main()
