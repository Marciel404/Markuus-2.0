from Outhers.Infos.fi import *



class SlashGerais(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name = 'help',
        description = 'Mostra os comandos do Markuus')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx: Interaction):
        
        rand = random.randint(0,2)

        if rand == 1:

            await ctx.response.send_message('Sabia que Me manter está ficando dificil?\nQue tal me ajudar doando algo?', ephemeral = True)

        if ctx.author.id == banip:

            return

        h = discord.Embed(title = 'Meus comands',
        description = 
        '''
Escolha a categoria
desejada para saber
meus comandos
        '''
        )
        h.set_thumbnail(url = self.bot.user.avatar)

        await ctx.response.send_message(embed = h, view = staff(), ephemeral = True)

    
    @slash_command(
        name = 'hello',
        description = 'Comando teste do Markuus'
    )
    async def hello(self, ctx):

        rand = random.randint(0,2)

        if ctx.author.id == banip:

            return

        if rand == 1:

            await ctx.response.send_message('Sabia que Me manter está ficando dificil?\nQue tal me ajudar doando algo?', ephemeral = True)
  
        await ctx.respond('Hello, World {}'.format(ctx.author.name))

    @slash_command(
        name = 'aleatorio',
        description = 'Escolhe um numero leatorio para você'
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def aleatorio(self, ctx,
    numero: Option(input_type = int, description = 'escolha um numero', required = True) = 0):

        rand = random.randint(0,2)
        
        if rand == 1:

            await ctx.response.send_message('Sabia que Me manter está ficando dificil?\nQue tal me ajudar doando algo?', ephemeral = True)

        if ctx.author.id == banip:

            return
        
        dado = random.randint(0,int(numero))

        if numero == 0:

            await ctx.respond('Voce precisa escolher um numero para esse comando funcionar', ephemeral = True)

        else:

            await ctx.respond('Seu numero foi {}'.format(dado), ephemeral = True)

    @slash_command(name = 'ping', description = 'Mostra o ping do Markuus')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.response.send_message('Sabia que Me manter está ficando dificil?\nQue tal me ajudar doando algo?', ephemeral = True)

        if ctx.author.id == banip:

            return

        p1 = discord.Embed(title = 'ping', 
        description = '**🏓Calculando ping.**',


        color = 0x2ecc71)

        start_time = time.time()

        msg = await ctx.respond(embed = p1, ephemeral = True)

        end_time = time.time()

        Ping = round(self.bot.latency * 1000)

        p4 = discord.Embed(title = 'ping', 

        description = f'''
Meu ping: {Ping}ms
API: {round((end_time - start_time) * 1000)}ms''', 

        color = 0x2ecc71)

        await msg.edit_original_message(embed = p4)

    @slash_command(name = 'servers', description = 'Mostra em quantos servers o Markuus está')
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def servers(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.response.send_message('Sabia que Me manter está ficando dificil?\nQue tal me ajudar doando algo?', ephemeral = True)

        if ctx.author.id == banip:

            return

        await ctx.respond('Eu estou em {0} servers!'.format(str(len(self.bot.guilds))), ephemeral = True)

    @slash_command(name = 'serverinfo', description = 'Mostra as informações do server')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverInfo(self, ctx, server: discord.Guild = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        if server == None:

            server = ctx.guild

        embed = discord.Embed(title = f'**{server.name}**',

        color = random.randint(00000, 99999))

        embed.add_field(name = ':scroll: Nome:', 

        value = server.name,
        
        inline = True)
        
        embed.add_field(name = ':computer:  Id do server:', 

        value = server.id,

        inline = True)

        embed.add_field(name = ':busts_in_silhouette: Membros:', 

        value = server.member_count,

        inline = True)

        embed.add_field(name = f':speech_balloon: Canais:({len(server.voice_channels)+len(server.voice_channels)})',

        value = f':keyboard: texto: {len(server.voice_channels)}\n :loud_sound: Voz:{len(server.voice_channels)}',

        inline = True)

        embed.add_field(name = ':shield: Verificação:',

        value = '{}'.format(str(server.verification_level).upper()),

        inline = True)

        embed.add_field(name = ':crown: Dono:', 

        value = '<@{0}>\n ({0})'.format(server.owner_id),

        inline = True)

        embed.add_field(name = ':calendar_spiral:Criado em:', 
        
        value = server.created_at.strftime('%d %m %Y'),

        inline = True)

        if server.icon == None:

            embed.set_thumbnail(url='')

        else:

            embed.set_thumbnail(url=server.icon)

        await ctx.respond(embed = embed, ephemeral = True)

    
def setup(bot: commands.Bot) -> None:
    bot.add_cog(SlashGerais(bot))