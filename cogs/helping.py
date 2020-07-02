import json

var_help = dict()
with open('.\\database_json\\help.json', 'r') as json_file:
    var_help = json.load(json_file)

def helping(nome_comando):
    try:
        return var_help[nome_comando]['help']
    except:
        return

def brief(nome_comando):
    try:
        return var_help[nome_comando]['brief']
    except:
        return

def description(nome_comando):
    try:
        return var_help[nome_comando]['description']
    except:
        return


        
