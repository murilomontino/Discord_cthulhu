import discord
from discord.ext import commands

import DiscordAppBot

class Dados(commands.Cog):

    def __init__(self, client: DiscordAppBot):
        self._client = client

    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.command()
    async def dado(self, message:discord.User):
        rollem: discord.User = self._client.get_user(240732567744151553)
        await message.send(content=f'{rollem.mention} d20', tts=False, embed=None, file=None, files=None, delete_after=None,
                           nonce=None, allowed_mentions=discord.AllowedMentions())

def setup(client):
    client.add_cog(Dados(client))
