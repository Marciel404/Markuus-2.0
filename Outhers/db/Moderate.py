from pymongo import MongoClient
from dotenv import load_dotenv
from discord.ext import commands
from os import getenv

load_dotenv()

mongo = getenv('MONGOKEY')

cluster = MongoClient(mongo)

db = cluster["Bank"]
logs = db["Logs"]
autorule = db["AutoRole"]
prefix = db["Prefix"]

class ModerateOuthers(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
def setup(bot: commands.Bot) -> None:
     bot.add_cog(ModerateOuthers(bot))