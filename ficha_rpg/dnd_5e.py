import discord
from d20 import roll



class DnD_5e(object):

    @staticmethod
    def painel_do_jogador(player: dict):

        fichamento = player["fichamento"]
        primarias = player["caracteristicas"]["primarias"]
        secundarias = player["caracteristicas"]["secundarias"]

        embed = discord.Embed(title=fichamento["nome_personagem"])

        embed.set_author(name=fichamento["ocupacao"],
                         icon_url="https://cdn.imgbin.com/7/11/13/"
                                  "imgbin-cthulhu-lovecraftian-horror-computer-icons-"
                                  "rpg-maker-mv-others-e3H7mww7JVhF6Bhu2UPgNvhzp.jpg")
        embed.set_thumbnail(url=fichamento["url_image"])

        for atributo in primarias:
            embed.add_field(name=atributo, value=primarias[atributo], inline=True)

        embed.add_field(name="Sorte", value=secundarias["SORTE"], inline=False)
        embed.add_field(name="Sanidade", value=secundarias["SANIDADE"], inline=True)

        pontos_de_vida = f"{secundarias['PV']}({secundarias['PV_atual']})"
        embed.add_field(name="Vida", value=pontos_de_vida, inline=True)

        pontos_de_magia = f"{secundarias['PM']}({secundarias['PM_atual']})"
        embed.add_field(name="Magia", value=pontos_de_magia, inline=True)

        return embed

    @staticmethod
    def rolagem_principal(message=None):
        pass

