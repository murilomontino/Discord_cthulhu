
CONFIG = {
    "PREFIX": "!",
    "TOKEN": "NzE1NjgyMDcxOTQyNTI5MTM0.XuW_-w.UGFoK5PZ38PADlRy3qyrNGJk_1Q",
    "MODULOS": [
        "cogs.comandos", 
        "cogs.database", 
        "cogs.dados", 
        "cogs.efeitos_sonoros"
    ],
    "DATABASE": "mongodb+srv://murilomontiono:kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/rpg?retryWrites=true&w=majority"
}

class Config():
    
    def __init__(self):
        self.prefix = CONFIG['PREFIX']
        self.database = CONFIG['DATABASE']
        self.modulos = CONFIG['MODULOS']
        self.token = CONFIG['TOKEN']

config = Config()

