from Outhers.Infos.fi import *

def get_prefix(client, message):

    prefixes = prefix.find_one({"_id": message.guild.id})

    pre = prefixes['prefix']

    return pre

intents = discord.Intents.all()

token = getenv('TOKEN')

load_dotenv()

client = commands.Bot(

command_prefix = get_prefix,

intents = intents,

help_command = None,

case_insensitive = True,

application_id = 931932629085847552,

)

for filename in os.listdir('./Commands'):

        if filename.endswith('.py'):

                client.load_extension(f'Commands.{filename[:-3]}')

for filename in os.listdir('./Commands_Slash'):

        if filename.endswith('.py'):

                client.load_extension(f'Commands_Slash.{filename[:-3]}')

for filename in os.listdir('./Outhers'):

        if filename.endswith('.py'):

                client.load_extension(f'Outhers.{filename[:-3]}')

client.run(token)