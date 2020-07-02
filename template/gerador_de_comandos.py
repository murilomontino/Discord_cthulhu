import json

ficha = []
with open("cthulhu_7e_sheet.json", 'r') as json_file:
    ficha = json.load(json_file)

comandos: dict = {}
with open("comandos.json", 'r') as json_file:
    comandos = json.load(json_file)
try:
    ultimo_comando = list(zip(comandos, comandos.values()))[-1]
except:
    ultimo_comando = None


caminhos = []
def caminho_percorrido(dicionario: dict, percurso=None):

    if not isinstance(dicionario, dict):
        return percurso.split("@")
    else:
        for rota in dicionario:
            if percurso == None:
                caminhos.append(caminho_percorrido(dicionario[rota], percurso=rota))
            else:
                caminhos.append(caminho_percorrido(dicionario[rota], percurso=f"{percurso}@{rota}"))

def posicao_ultimo_comando(ultimo_comando) -> int:
    global caminhos
    contador = 0

    if ultimo_comando == None:
        return 0
    else:
        ultimo_comando = ultimo_comando[-1][-1]


    while contador < len(caminhos):
        print(caminhos[contador][-1])
        nome = caminhos[contador][-1]

        if nome == ultimo_comando:
            return contador

        contador += 1


def criando_comandos(caminhos: list, ultimo_comando=None ) -> dict:
    contador = posicao_ultimo_comando(ultimo_comando)
    comandos: dict = {}
    while contador < len(caminhos):

        if caminhos[contador] == None:
            contador += 1
            continue

        print(caminhos[contador])
        start = input("Digite o comando: \n "
                      " break -> para parar \n "
                      " prox -> pra o próximo comanod \n")

        if start == "prox":
            contador += 1
            continue
        elif start == "break":
            break
        comandos[start] = caminhos[contador]

    return comandos

def salvando_comandos(comandos_A: dict, comandos_B: dict):
    comandos_A.update(comandos_B)
    with open("comandos.json", 'w') as json_file:
        json.dump(comandos, json_file, indent=4)


def main():
    global caminhos, comandos, ultimo_comando
    caminho_percorrido(ficha)
    new_comandos = criando_comandos(caminhos, ultimo_comando)
    salvando_comandos(comandos, new_comandos)


if __name__ == '__main__':
    main()