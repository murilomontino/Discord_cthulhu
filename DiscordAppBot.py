import random

import discord
import pymongo
from discord.ext.commands import AutoShardedBot, when_mentioned_or

class DiscordAppBot(AutoShardedBot):

    TOKEN = "NzE1NjgyMDcxOTQyNTI5MTM0.XtHSCg.g0VB3MbRlrAJXwLw4k7iFdQHsQU"
    modulos = ['cogs.comandos', 'cogs.database', 'cogs.dados']

    def __init__(self):
        super().__init__(command_prefix='!', case_insensitive=True)
        for modulo in self.modulos:
            self.load_extension(modulo)
        self.database = pymongo.MongoClient('mongodb+srv://murilomontiono:kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/sheets?retryWrites=true&w=majority')['RPG']['sheets']
        self.run(self.TOKEN)

    async def on_ready(self):
        print('BOT ONLINE - OLÁ MUNDO')
        print(self.user.name)
        print(self.user.id)
        print('-----PR------')
        await self.change_presence(activity=discord.Streaming(name='!help', url='www.google.com.br'))




def main():
    client = DiscordAppBot()

if __name__ == '__main__':
    main()
