import discord
import pymongo
import json

from discord.ext import commands


class Create_Sheet(commands.Cog):

    def __init__(self, client):
        self._client = client

    @commands.command()
    @commands.dm_only()
    def create(self, message: discord.Message):
        pass


def setup(client):
    client.add_cog(Create_Sheet(client))
