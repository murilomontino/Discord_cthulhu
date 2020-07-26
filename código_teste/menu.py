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

emoji_number = {
    "0️⃣": 0,
    "1️⃣": 1,
    "2️⃣": 2,
    "3️⃣": 3 ,
    "4️⃣": 4,
    "5️⃣": 5,
    "6️⃣": 6,
    "7️⃣": 7,
    "8️⃣": 8,
    "9️⃣": 9,
    "🔟": 10
}

template = database.find_one({'template': 'cthulhu_7e'}, {'template': 0, '_id': 0})

def createMenu(template):
    
    pass

# [{menu1}, {menu2}, {menu3}, {menu4}]

database = pymongo.MongoClient('mongodb+srv://murilomontiono:'
                               'kingdom2012@rpgsheets-ofr2t.gcp.mongodb.net/'
                               'rpg?retryWrites=true&w=majority')['RPG']['sheets']




def main():
    pass

if __name__ == "__main__":
    main()
