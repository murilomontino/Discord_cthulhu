import json
from DiscordApp.Bot.ficha_rpg.TypeSheet import TypeSheet

class Sheet:

    def __init__(self):
        self._Sheets_: TypeSheet = []
        self.load_sheet()

    @property
    def sheets (self):
        return self._Sheets_

    @sheets.setter
    def sheets(self, new_sheet: TypeSheet):
        self._Sheets_.append(new_sheet)

    def load_sheet(self, type_sheet='Default'):
        with open('player_sheets.json', 'r') as json_file:
            self._Sheets_ = json.load(json_file)

    def list_sheet(self, type_sheet=None):
        contador = 1
        for sheet in self._Sheets_.values():
            if sheet['tipo_de_ficha'] == type_sheet:
                print(f"Id: {sheet['id']} ")
                print(sheet['nome_personagem'])
            contador += 1

    def save_sheet(self):
        pass




def main():
    teste = Sheet()
    teste.load_sheet()
    teste.list_sheet(type_sheet='cthulhu_7e')


if __name__ == "__main__":
    main()
