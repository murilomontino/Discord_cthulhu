import json
from abc import abstractmethod


class TypeSheet:

    def __init__(self, tipo_ficha: str, nome_jogador: str, nome_ficha: str):
        with open(tipo_ficha, 'r') as json_file:
            self._sheet_ = json.load(json_file)
        self._sheet_ = self._sheet_[nome_ficha]
        self._sheet_['nome_jogador'] = nome_jogador


    def get_sheet_value(self, value: str) -> str:

        if value in self._sheet_:
            return self._sheet_[value]
        else:
            return 'Elemento inválido'


    def set_sheet_value(self, value: str, new_value: str):
        if value in self._sheet_:
            self._sheet_[value] = new_value
        else:
            return 'Elemento não-adicionado'

    @abstractmethod
    def embed_player(self):
        pass

    def D3(self, quant: int = 1):
        pass

    def D6(self, quant: int = 1):
        pass

    def D8(self, quant: int = 1):
        pass

    def D10(self, quant: int = 1):
        pass

    def D12(self, quant: int = 1):
        pass

    def D20(self, quant: int = 1):
        pass

    def D100(self, quant: int = 1):
        pass