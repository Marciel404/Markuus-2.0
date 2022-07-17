from pymongo import MongoClient
from dotenv import load_dotenv
from discord.ext import commands
from os import getenv

load_dotenv()

mongo = getenv('MONGOKEY')

cluster = MongoClient(mongo)
db = cluster["Bank"]

bank = db["Bank"]
inv = db["Inv"]

Minerios = [
    {'Nome': 'Ferro', 'compra': 450, 'Venda':405},
    {'Nome': 'Ouro', 'compra': 290880, 'Venda':261792},
    {'Nome': 'Diamante', 'compra': 293504, 'Venda':264153},
]

utilitarios = [
    {'Nome': 'Picareta ferro','compra': 500, 'Venda': 450},
    {'Nome': 'Picareta ouro','compra': 290900, 'Venda': 261810},
    {'Nome': 'Picareta diamante','compra': 293900, 'Venda': 264510},
    {'Nome': 'Madeira', 'compra': 50, 'Venda': 45},
    {'Nome': 'Anel casamento', 'compra': 60, 'Venda':54},
    {'Nome': 'Computador', 'compra': 3500, "Venda": 2000},
    {'Nome': 'Arma', 'compra': 25000, 'Venda': 22500},
]

cosmeticos = [
    {'Nome': 'Carro', 'compra': 10000, 'Venda':9000},
]
    
crafts = [
    {"Nome": 'Picareta ferro', '1': '1 Madeira', '2': '5 Ferros'},
    {"Nome": 'Picareta ouro', '1': '1 Madeira', '2': '6 Ouros'},
    {"Nome": 'Picareta diamante', '1': '1 Madeira', '2': '10 Diamante'},
]

shopping = [
    {'Nome': 'Picareta ferro','compra': 500, 'Venda': 450},
    {'Nome': 'Picareta ouro','compra': 290900, 'Venda': 261810},
    {'Nome': 'Picareta diamante','compra': 293900, 'Venda': 264510},
    {'Nome': 'Arma', 'compra': 25000, 'Venda': 22500},
    {'Nome': 'Carro', 'compra': 10000, 'Venda':9000},
    {'Nome': 'Ferro', 'compra': 450, 'Venda':405},
    {'Nome': 'Ouro', 'compra': 290880, 'Venda':261792},
    {'Nome': 'Diamante', 'compra': 293504, 'Venda':264153},
    {'Nome': 'Anel casamento', 'compra': 60, 'Venda':54},
    {'Nome': 'Madeira', 'compra': 50, 'Venda': 45},
    {'Nome': 'Computador', 'compra': 3500, "Venda": 2000}
]

async def open_account(id):

    if id is not None:

        user = {"_id": id.id, "Nome": id.name, "Edinhos": 0}
        myquery = { "_id": id.id}   
        if (bank.count_documents(myquery) == 0):

            bank.insert_one(user)

async def update_bank(id, Edinhos : int):
    if id is not None:
        bank.update_one({"_id": id.id}, {"$inc": {"Edinhos": Edinhos}})

async def open_inv(id):
    if id is not None:
        user = {'_id': id.id, 
        'Nome': id.name, 
        'picareta ferro' : 0, 
        'picareta ouro' : 0,
        'picareta diamante' : 0,
        'carro' : 0,
        'arma' : 0,
        'diamante' : 0,
        'ouro' : 0,
        'anel casamento' : 0,
        'ferro' : 0,
        'madeira': 0,
        'computador': 0,
        }
        myquery = { "_id": id.id}   
        if inv.count_documents(myquery) == 0:

            inv.insert_one(user)

async def update_inv(id, item, quantidade : int):

    if id is not None:
        inv.update_one({"_id": id.id}, {"$inc": {f"{item.lower()}": quantidade}})

async def reload_inv(id):

    if id is not None:
        inv.update_one({"_id": id.id}, {"$inc": {f"computador": 0}})
        inv.update_one({"_id": id.id}, {"$inc": {f"madeira": 0}})

class EconomiaOuthers(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
def setup(bot: commands.Bot) -> None:
    bot.add_cog(EconomiaOuthers(bot))