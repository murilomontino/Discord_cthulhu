import discord
from d20 import roll

class Cthulhu_7e(object):

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

        if message == None:
            dados = roll('d100')
            return str(dados)

        metade = pericia // 2
        um_quinto = pericia // 5

        dados = roll(f'd100 [{pericia_nome}]')

        ''' 
        1 - acerto critico
        2 até um_quinto - acerto extremo
        um_quinto até metade - acerto hard
        metade até pericia - acerto normal
        pericia+1 até 95 - erro
        96 até 100 - erro critico
       
        '''
        total = dados.total
        resultado : str = str()

        if total == 1:
            resultado = f"{str(dados)}  Acerto Critico"
        elif 1 < total <= um_quinto:
            resultado = f"{str(dados)}  Acerto Extremo"
        elif um_quinto < total <= metade:
            resultado = f"{str(dados)}  Acerto Difícil"
        elif metade < total <= pericia:
            resultado = f"{str(dados)}  Acerto Normal"
        elif pericia < total <= 95:
            resultado = f"{str(dados)}  Erro Comum"
        elif 95 < total:
            resultado = f"{str(dados)}  Erro Critico"

        return resultado

