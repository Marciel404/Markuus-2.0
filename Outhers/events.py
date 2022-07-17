from Outhers.Infos.fi import *

data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
dt = data_e_hora_sao_paulo.strftime('%H:%M %d/%m/%Y')

class events(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url('https://discord.com/api/webhooks/996776097658183700/eXZT0GxuGceZfEW8cCeVZpxha6lQ6R0yd0ZqeIj6mXdMrmjnJ3YskQq8AVx680bn6eWP', session=session)
            e = discord.Embed(title = self.bot.user.name)
            e.add_field(name = 'Acordou as', value = dt)
            e.add_field(name = 'Id', value = self.bot.user.id, inline = False)
            if self.bot.user.avatar == None:
                e.set_thumbnail(url =  '')
            else:
                e.set_thumbnail(url = self.bot.user.avatar)
            await webhook.send(embed = e)

        print(f'EU entrei como {self.bot.user}')
        print(discord.__version__)
        while True:
            await self.bot.change_presence(status = discord.Status.online, activity = Game)
            await asyncio.sleep(10)
            await self.bot.change_presence(activity = listening)
            await asyncio.sleep(10)
            await self.bot.change_presence(activity = stream)
            await asyncio.sleep(10)
            await self.bot.change_presence(activity = watching)
            await asyncio.sleep(10)

    @commands.Cog.listener()
    async def on_message(self, message):

        prefixo = prefix.find_one({"_id": message.guild.id})
        pre = prefixo['prefix']

        if message.author == self.bot.user: return

        if message.author.bot: return
        
        if message.author.id == banip:
            return
        elif message.mention_everyone:
            return
        elif self.bot.user.mentioned_in(message):
            if ' ' in message.content:
                return
            else:
                await message.reply('Meu prefixo nesse servidor é {0} , use {0}help para saber meus comandos'.format(pre))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        user = self.bot.get_user(int(IdS))

        embed = discord.Embed(title = f':inbox_tray: | Entrada')
        embed.add_field(name = f':regional_indicator_s: | Nome do servidor:', value = guild.name, inline = False)
        embed.add_field(name = f':regional_indicator_i: | ID do servidor:', value = guild.id, inline = False)
        embed.add_field(name = f':regional_indicator_m: | Membros', value = len(guild.members), inline = False)

        await user.send(embed = embed)
        await set_prefix(guild, '==')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        server = {"_id": guild.id}

        logs.delete_one(server)
        prefix.delete_one(server)
        autorule.delete_one(server)

        user = self.bot.get_user(int(IdS))

        embed = discord.Embed(title = f':inbox_tray: | Saida')
        embed.add_field(name = f':regional_indicator_s: | Nome do servidor:', value = guild.name, inline = False)
        embed.add_field(name = f':regional_indicator_i: | ID do servidor:', value = guild.id, inline = False)
        embed.add_field(name = f':regional_indicator_m: | Membros', value = len(guild.members), inline = False)

        await user.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):

        try:
            r = autorule.find_one({"_id": member.guild.id})
            r1 = r["Role"]
        finally:
            role = discord.utils.get(member.guild.roles, name=f'{r1}')
            await member.add_roles(role)

async def set_prefix(id, prefixo):
    user = {'_id': id.id, 'Nome': id.name, 'prefix': prefixo}
    myquery = { "_id": id.id}   
    if (prefix.count_documents(myquery) == 0):

        prefix.insert_one(user)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(events(bot))