import random
import json
import discord
import pymongo
from config import config
from cogs import roll

from discord.ext.commands import AutoShardedBot, when_mentioned_or

class DiscordAppBot(AutoShardedBot):

    def __init__(self):
        super().__init__(command_prefix=config.prefix, case_insensitive=True)
        self.muted = set()
        self._database = pymongo.MongoClient(config.database)['RPG']['sheets']
        self._comandos = pymongo.MongoClient(config.database)['RPG']['comandos']

    def all_comandos(self):
        return self.all_commands

    @property
    def database(self):
        return self._database

    @property
    def comandos(self):
        return self._comandos

    async def on_guild_join(self,guild):
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
  
        self.name_function = [name for name in self.all_commands]
        self.new_comandos()
        await self.change_presence(activity=discord.Streaming(name='!help', url='www.google.com.br'))

    async def on_message(self, message):

        if message.author.id in self.muted:
            return

        if message.content.startswith('#'):  # efeitos_sonoros serão chamados
            message.content = f"{self.command_prefix}# " + message.content
            await self.process_commands(message)
            return

        try:
            rolagem = roll(message.content, message.author)
            await message.channel.send(embed=rolagem)
        except:
            await self.process_commands(message)
        finally:
            return
            
    def new_comandos(self):
        novos_comandos = dict()
        with open("./database_json/command.json", 'r') as json_file:
            novos_comandos = json.load(json_file)
        del (novos_comandos['comentario'])
        for nome in novos_comandos:
            if novos_comandos[nome] != []:
                for comando in novos_comandos[nome]:
                    self.all_commands[comando] = self.all_commands[nome]
            else:
                continue

    def novo_nome_comando(self, comando, nome):
        
        if self.all_comandos[comando]:
            self.all_comandos[nome] = self.all_comandos[comando]
        
        return


TOKEN = config.token
MODULOS = config.modulos
CLIENT = DiscordAppBot()





for modulo in MODULOS:
    CLIENT.load_extension(modulo)


def main():
    CLIENT.run(TOKEN)


if __name__ == '__main__':
    main()
