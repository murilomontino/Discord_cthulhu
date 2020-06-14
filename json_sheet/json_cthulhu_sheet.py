import json


personagem = {
     'cthuhu_sheet': {
        "tipo_de_ficha": "cthulhu_7e",
        "url_image": "",
        "id": "",
        'nome_personagem': '',
        'nome_jogador': '',
        'idade': '',
        'ocupacao': '',
        'sexo': '',
        'nascimento': '',
        'residencia': '',

        'caracteristicas': {
            'FOR': 0,
            'DES': 0,
            'POD': 0,
            'CON': 0,
            'APA': 0,
            'EDU': 0,
            'TAM': 0,
            'INT': 0
            
            },
        
        'SORTE': 0,
        'SANIDADE': 0,
        'PTs_DE_VIDA': 0,
        'PTs_DE_MAGIA': 0,
        'NV_DE_CREDITO': 0,
        'CTHULHU_MITOS': 0,
        'TAXA_DE_MOVIMENTO': 0,

        'combate':  {
            'BNs_de_DANO': 0,
            'CORPO': 0,
            'ESQUIVA': 0

            },

        'pericias':{

            'ANTROPOLOGIA': 1,
            'ARMAS_DE_FOGO_(REVOLVER)': 20,
            'ARMAS_DE_FOGO_(RIFLES)': 25,
            'ARQUEOLOGIA': 1, 
            'ARREMESSAR': 20,
            'ARTE/OFICIO': 5,
            'AVALIAÇÃO': 5,

            'CAVALGAR': 5,
            'CHARME': 15,
            'CHAVEIRO': 1,
            'CIÊNCIA': 1,
            'CONSERTOS_ELETRICOS': 10,
            'CONSERTOS_MECÂNICOS': 5,
            'CONTABILIDADE': 5,

            'DIREITO': 5,
            'DIRIGIR_AUTOMÓVEL': 20,
            'DISFARCE': 5,

            'ENCONTRAR': 25,
            'ESCUTAR': 20,
            'ESCALAR': 20,

            'LÁBIA': 5,
            
            'INTIMIDAÇÃO': 15,
            
            'HISTÓRIA': 5,
            
            'FURTIVIDADE': 20,
            
            'LINGUA_NATURAL': 1,
            'LINGUA_(OUTRA)': 1,
            'LUTAR(BRIGAR)': 25,

            'MEDICINA': 1,
            'MUNDO_NATURAL': 10,

            'NATAÇÃO': 20,
            'NAVEGAÇÃO': 10,

            'OCULTISMO': 5,
            'OPERAR_MAQUINÁRIO': 1,

            'PERSUASSÃO': 10,
            'PILOTAR': 1,
            'PREDIGITAÇÃO': 10,
            'PRIMEIROS SOCORROS': 30,
            'PSICANÁLISE': 1,
            'PSICOLOGIA': 10,

            'SALTAR': 20,
            'SOBREVIVÊNCIA': 10,

            'RASTREAR': 10,

            'USAR_BIBLIOTECA': 20
            },

        'armas': {
            'DESARMADO': {'DIFICULDADE': 1, 'DANO': '1D3+BD', 'ALCANCE': '-', 'ATAQUE': '-',
                          'MUNIÇÃO': '-', 'DEFEITO': '-'}
            },
        
        'antecedentes': {
            'DESCRIÇÃO PESSOAL': '',
            'CARACTERÍSTICAS': '',
            'IDEOLOGIAS/CRENÇAS': '',
            'PESSOAS SIGNIFICATIVAS': '',
            'LOCAIS IMPORTANTES': '',
            'PERTENCES QUERIDOS': '',
            'FERIMENTOS E CICATRIZES': '',
            'FOBIAS E MANIAS': '',
            'TOMOS ARCANOS, FEITIÇOS E ARTEFATOS': '',
            'ENCONTROS COM ENTIDADES ESTRANHAS': ''

            },

        'equipamentos/pertences': '',
        
        'recursos': {
            'NV DE GASTO': 0,
            'DINHEIRO': 0,
            'PATRIMÔNIO': ''

            }
        }
    }

with open("cthulhu_sheet.json", 'w') as json_file:
    json.dump(personagem, json_file, indent=4)
