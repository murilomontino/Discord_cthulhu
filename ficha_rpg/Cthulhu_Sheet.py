import discord

from .TypeSheet import TypeSheet

class Cthulhu_sheet(TypeSheet):

    _cthulhu_json_: str = 'cthulhu_7e_sheet.json'
    _cthulhu_sheet_ : str = 'cthulhu_sheet'

    def __init__(self, nome_jogador: str):
        super().__init__(tipo_ficha=self._cthulhu_json_, nome_jogador=nome_jogador, nome_ficha = self._cthulhu_sheet_ )
        self._caracteristicas_ = self._sheet_['caracteristicas']
        self._pericias_ = self._sheet_['pericias']

    def get_pericias(self, value: str):
        if value in self._pericias_:
            return self._pericias_[value]
        else:
            return 'Perícia inválida'

    def set_pericias(self, value: str, new_value: int):
        if value in self._pericias_:
            self._pericias_[value] = new_value
        else:
            return 'Perícia inválida'

    def get_caracteristica(self, value: str):
        if value in self._caracteristicas_:
            return self._caracteristicas_[value]
        else:
            return 'Característica inválida'

    def set_caracteristica(self, value: str, new_value: int):
        if value in self._caracteristicas_:
            self._caracteristicas_[value] = new_value
        else:
            return 'Característica inválida'

    @staticmethod
    def embed_player(player: dict):
        caracteristicas = player["caracteristicas"]
        embed = discord.Embed(title=player["nome_personagem"])

        embed.set_author(name=player["ocupacao"],
                         icon_url="https://cdn.imgbin.com/7/11/13/imgbin-cthulhu-lovecraftian-horror-computer-icons-rpg-maker-mv-others-e3H7mww7JVhF6Bhu2UPgNvhzp.jpg")
        embed.set_thumbnail(url=player["url_image"])
        embed.add_field(name="FOR:", value=caracteristicas["FOR"], inline=True)
        embed.add_field(name="DES", value=caracteristicas["DES"], inline=True)
        embed.add_field(name="CON", value=caracteristicas["CON"], inline=True)
        embed.add_field(name="APA", value=caracteristicas["APA"], inline=True)
        embed.add_field(name="TAM", value=caracteristicas["TAM"], inline=True)
        embed.add_field(name="EDU", value=caracteristicas["EDU"], inline=True)
        embed.add_field(name="INT", value=caracteristicas["INT"], inline=True)
        embed.add_field(name="POD", value=caracteristicas["POD"], inline=True)
        embed.add_field(name="Sorte", value=player["SORTE"], inline=False)
        embed.add_field(name="Sanidade", value=player["SANIDADE"], inline=True)
        embed.add_field(name="Vida", value=player["PTs DE VIDA"], inline=True)
        embed.add_field(name="Magia", value=player["PTs DE MAGIA"], inline=True)


        return embed

