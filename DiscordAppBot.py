import random
import json
import discord
import pymongo

from cogs import roll

from discord.ext.commands import AutoShardedBot, when_mentioned_or

class DiscordAppBot(AutoShardedBot):

    def __init__(self):
        super().__init__(command_prefix='!', case_insensitive=True)
        self.muted = set()
        self.all_commands 
        self._database = pymongo.MongoClient('mongodb+srv://murilomontiono:'
                                             'kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/'
                                             'rpg?retryWrites=true&w=majority')['RPG']['sheets']
    
        self._comandos = pymongo.MongoClient('mongodb+srv://murilomontiono:'
                                             'kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/'
                                             'rpg?retryWrites=true&w=majority')['RPG']['comandos']

    def all_comandos(self):
        return self.all_commands

    @property
    def database(self):
        return self._database

    @property
    def comandos(self):
        return self._comandos

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

    def new_comandos(self):
        novos_comandos = dict()
        with open(".\\database_json\\command.json", 'r') as json_file:
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








TOKEN = "NzE1NjgyMDcxOTQyNTI5MTM0.XuW_-w.UGFoK5PZ38PADlRy3qyrNGJk_1Q"
MODULOS = ['cogs.comandos', 'cogs.database', 'cogs.dados', 'cogs.efeitos_sonoros']
CLIENT = DiscordAppBot()



@CLIENT.event
async def on_message(message):

    if message.author.id in CLIENT.muted:
        return

    if message.content.startswith('#'): #efeitos_sonoros serão chamados
        message.content = f"{CLIENT.command_prefix}# " + message.content
        await CLIENT.process_commands(message)
        return
    
    try:
        rolagem = roll(message.content, message.author)
        await message.channel.send(embed=rolagem)
    except:
        await CLIENT.process_commands(message)
    finally:
        return

for modulo in MODULOS:
    CLIENT.load_extension(modulo)


def main():
    CLIENT.run(TOKEN)


if __name__ == '__main__':
    main()
