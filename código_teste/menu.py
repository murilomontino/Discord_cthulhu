import pymongo

from discord import Embed

emoji = {

    "seguinte": "➡",
    "anterior": "⬅",

    "play": "▶",
    "pause": "⏸",
    "stop": "⏹",

    "confirmar": "🟢",
    "negar": "🔴",
    "editar": "🔵",

    "dinheiro": "💲",
}

emoji_number = {
    "0": "0️⃣",
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣",
    "10": "🔟"
}

database = pymongo.MongoClient('mongodb+srv://murilomontiono:'
                               'kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/'
                               'rpg?retryWrites=true&w=majority')['RPG']['sheets']

template = database.find_one({'template': 'cthulhu_7e'}, {'template': 0, '_id': 0})



def main():
    print(emoji_number.get('7️⃣', 'valor inválido') )

if __name__ == "__main__":
    main()
