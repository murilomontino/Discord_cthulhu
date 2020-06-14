import discord
import pymongo
from discord.ext import commands

import DiscordAppBot
from ficha_rpg.Cthulhu_Sheet import Cthulhu_sheet

class Database(commands.Cog):

    def __init__(self, client: DiscordAppBot):
        self._client = client

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def myself(self, message):
        id = str(message.author.id)
        player = self._client.database.find_one({'id': id})
        await message.send(embed=Cthulhu_sheet.embed_player(player))





def setup(client):
    client.add_cog(Database(client))
