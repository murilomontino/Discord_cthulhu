import json
from abc import abstractmethod
from d20 import roll
from template import TEMPLATE_SHEET
from ficha_rpg import FICHA

# classe TEMPLATE DE FICHAS
# PADRONIZANDO TODAS AS FICHAS DE TAL MANEIRA QUE SEJA POSSÌVEL ADICIONAR O MAIOR NÚMERO DE SISTEMAS POSSÌVEIS DE RPG
# DE MANEIRA FÁCIL E PRATICA
class TypeSheet(object):

    def __init__(self):
        self.template_sheet = TEMPLATE_SHEET
        self.FICHA = FICHA

    #FUNCAO QUE MONTARÁ O PAINEL COM AS PRINCIPAIS CARACTERISTICAS DO PERSONAGEM DO JOGADOR
    def painel_do_jogador(self, cls, player):
        return self.FICHA[cls].painel_do_jogador(player)

    #PRINCIPAL ROLAGEM DE DADOS DO SISTEMA
    def rolagem_principal(self, cls):
        return self.FICHA[cls].rolagem_principal()

