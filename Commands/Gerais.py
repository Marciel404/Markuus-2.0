from Outhers.Infos.fi import *

class Gerais(commands.Cog):
    bot: commands.Bot

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx):
        
        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

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

        await ctx.reply(embed = h, view = staff())

    @commands.command()
    async def hello(self, ctx):

        rand = random.randint(0,2)

        if ctx.author.id == banip:

            return

        elif rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        else:
            
            await ctx.reply('Hello, World {}'.format(ctx.author.name))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def aleatorio(self, ctx,numero = 0):

        rand = random.randint(0,2)
        
        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        elif numero == 0:

            await ctx.reply('Você precisa escolher um numero')

            return
        
        dado = random.randint(0,int(numero))

        if numero == 0:

            await ctx.reply('Voce precisa escolher um numero para esse comando funcionar')

        else:

            await ctx.reply('Seu numero foi {}'.format(dado))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        p1 = discord.Embed(title = 'ping', 
        description = '**🏓Calculando ping.**',

        color = 0x2ecc71)

        start_time = time.time()

        msg = await ctx.reply(embed = p1)

        end_time = time.time()

        Ping = round(self.bot.latency * 1000)

        p4 = discord.Embed(title = 'ping', 

        description = f'''
Meu ping: {Ping}ms
API: {round((end_time - start_time) * 1000)}ms''', 

        color = 0x2ecc71)

        await msg.edit(embed = p4)

    @commands.command()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def servers(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        await ctx.reply('Eu estou em ' + str(len(self.bot.guilds)) + ' servers!')

    @commands.command(aliases = ['si', 'serveri'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverInfo(self, ctx, server : discord.Guild = None):

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

        await ctx.reply(embed = embed)

    @commands.command(aliases = ['ui', 'useri'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self, ctx, membro: discord.Member = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        if membro == None:

            membro = ctx.author

        await open_account(membro)

        user = bank.find_one({"_id": membro.id})

        edinhos = user["Edinhos"]

        embed = discord.Embed(colour=membro.color)

        embed.set_author(name=f"User Info - {membro}"),

        if membro.avatar == None:

            embed.set_thumbnail(url=''),

        else:

            embed.set_thumbnail(url=membro.avatar),

        embed.add_field(name = 'Nome:',

        value = membro.display_name,inline=True)

        embed.add_field(name = 'ID:',

        value = membro.id,inline=True)

        embed.add_field(name = 'Conta  criada em:',

        value = membro.created_at.strftime(f" %d %m %Y"),inline=True)

        embed.add_field(name = 'Entrou no server em:',

        value = membro.joined_at.strftime(f" %d %m %Y") ,inline=True)

        embed.add_field(name = 'Maior cargo:',

        value = membro.top_role.mention,inline=True)

        embed.add_field(name = 'Edinhos',

        value = edinhos, inline = True)

        await ctx.reply(embed=embed)

    @commands.command()
    async def avatar(self, ctx, membro: discord.Member = None):

        rand = random.randint(0,2)

        if rand == 1:
            
            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        if membro == None:

            membro = ctx.author

        else:

            membro = membro

        embed = discord.Embed(title = f'Avatar de {membro}', 

        description = f'clique [aqui]({membro.avatar}) para baixar a imagem')

        embed.set_image(url = f'{membro.avatar.url}')
        
        await ctx.reply(embed = embed)

    @commands.command()
    async def invite(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        e = discord.Embed(title = 'Invite', 

        description = 'Convide-me clicando [aqui](https://discord.com/api/oauth2/authorize?client_id=930619804593819699&permissions=8&scope=bot%20applications.commands)')

        e.set_thumbnail(url = self.bot.user.avatar)

        await ctx.reply(embed=e)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def hug(self, ctx, membro: discord.Member = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        elif membro == None:

            await ctx.reply('Você precisa mencionar alguem')

            return

        r = requests.get(

        'http://nekos.life/api/v2/img/hug')

        res = r.json()
        
        hug = discord.Embed(title = 'Abraço',

        description = '<@{}> abraçou <@{}>'.format(ctx.author.id,membro.id))

        hug.set_image(url = res['url'])

        hug.set_footer(text = 'Clique no 🔁 para retribuir')

        hug2 = discord.Embed(title = 'Abraço',

        description = '<@{}> abraçou <@{}>'.format(membro.id,ctx.author.id))

        hug2.set_image(url = res['url'])

        message = await ctx.reply(membro.mention,embed = hug)

        await message.add_reaction("🔁")

        def check(reaction, user):

            if user == self.bot.user:

                return

            else:

                return user == membro and str(reaction.emoji) in "🔁"

        reaction, user = await self.bot.wait_for("reaction_add", check=check)

        if str(reaction.emoji) == "🔁":

            await ctx.reply(embed = hug2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def kiss(self, ctx, membro: discord.Member = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\nque tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        elif membro == None:

            await ctx.reply('Você precisa mencionar alguem')

            return

        r = requests.get(

        'http://nekos.life/api/v2/img/kiss')

        res = r.json()
        
        if membro == self.bot.user:

            await ctx.reply('Acho melhor só sermos amigos')

        else:

            kiss = discord.Embed(title = 'Beijo',

            description = '<@{}> beijou <@{}>'.format(ctx.author.id, membro.id))

            kiss.set_image(url = res['url'])

            kiss.set_footer(text = 'Clique no 🔁 para retribuir')
            
            kiss2 = discord.Embed(title = 'Beijo',

            description = '<@{}> beijou <@{}>'.format(membro.id, ctx.author.id))

            kiss2.set_image(url = res['url'])

            message = await ctx.reply(membro.mention,embed = kiss)

            await message.add_reaction("🔁")

            def check(reaction, user):

                if user == self.bot.user:

                    return

                else:

                    return user == membro and str(reaction.emoji) in "🔁"

            reaction, user = await self.bot.wait_for("reaction_add", check=check)

            if str(reaction.emoji) == "🔁":

                await ctx.reply(embed = kiss2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def slap(self, ctx, membro: discord.Member = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\nque tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        elif membro == None:

            await ctx.reply('Você precisa mencionar alguem')

            return

        r = requests.get(

        'http://nekos.life/api/v2/img/slap')

        res = r.json()
        
        if membro == self.bot.user:

            s = discord.Embed(title = 'Tapa', description = '<@{1}> estapeou <@{0}>'.format(ctx.author.id, membro.id))

            s.set_image(url = res['url'])

            await ctx.reply(embed = s)

        else:

            slap = discord.Embed(title = 'Tapa', description = '<@{}> estapeou <@{}>'.format(ctx.author.id, membro.id))

            slap.set_image(url = res['url'])

            slap.set_footer(text = 'Clique no 🔁 para retribuir')

            slap2 = discord.Embed(title = 'Tapa', description = '<@{1}> estapeou <@{0}>'.format(ctx.author.id, membro.id))

            slap2.set_image(url = res['url'])

    
            message = await ctx.reply(membro.mention,embed = slap)

            await message.add_reaction('🔁')


            def check(reaction, user):

                if user == self.bot.user:

                    return

                else:

                    return user == membro and str(reaction.emoji) in "🔁"

            reaction, user = await self.bot.wait_for("reaction_add", check=check)

            if str(reaction.emoji) == "🔁":

                await ctx.reply(embed = slap2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def shoot(self, ctx, membro: discord.Member = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\nque tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return   

        elif membro == None:

            await ctx.reply('Você precisa mencionar alguem')

            return

        r = requests.get(
        'http://nekos.life/api/v2/img/fire')
        res = r.json()

        shoot = discord.Embed(title = 'Tiro', description = f'<@{ctx.author.id}> atirou em <@{membro.id}>')

        shoot.set_image(url = res['url'])

        shoot.set_footer(text = 'Clique no 🔁 para retribuir')

        shoot2 = discord.Embed(title = 'Tiro', description = f'<@{membro.id}> atirou em <@{ctx.author.id}>')

        shoot2.set_image(url = res['url'])

        message = await ctx.reply(membro.mention,embed = shoot)

        await message.add_reaction("🔁")

        def check(reaction, user):

            if user == self.bot.user:

                return

            else:

                return user == membro and str(reaction.emoji) in "🔁"

        reaction, user = await self.bot.wait_for("reaction_add", check=check)

        if str(reaction.emoji) == "🔁":

            await ctx.reply(embed = shoot2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def punch(self, ctx, membro: discord.Member = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\nque tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        elif membro == None:

            await ctx.reply('Você precisa mencionar alguem')

            return
        
        if membro.bot:

            await ctx.reply('Você não faria isso com um pobre bot indefeso?')

        elif membro == None:

            await ctx.reply('Voce precisa mencionar alguem')

            choice = random.choice(punch)

            choice2 = random.choice(punch)

            punch1 = discord.Embed(title = 'Soco', description = f'<@{ctx.author.id}> Socou <@{membro.id}>')

            punch1.set_image(url = choice)

            punch1.set_footer(text = 'Clique no 🔁 para retribuir')

            punch2 = discord.Embed(title = 'Soco', description = f'<@{membro.id}> Socou <@{ctx.author.id}>')

            punch2.set_image(url = choice2)
    
            message = await ctx.reply(membro.mention,embed = punch)

            await message.add_reaction("🔁")

            def check(reaction, user):

                if user == self.bot.user:

                    return

                else:

                    return user == membro and str(reaction.emoji) in "🔁"

            reaction, user = await self.bot.wait_for("reaction_add", check=check)

            if str(reaction.emoji) == "🔁":

                await ctx.reply(embed = punch2)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def sad(self,ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        choice = random.choice(sad)

        embed = discord.Embed(title = 'Sad', description = f'{ctx.author.mention} está triste')

        embed.set_image(url = choice)

        await ctx.reply(embed = embed)

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def Vote(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        e1 = self.bot.get_emoji(972895959191289886)

        server = '[Server Suport](https://discord.com/invite/xSs6xEjuvf)'

        top = '[Top.gg](https://top.gg/bot/930619804593819699)'

        inv = '[Invite](https://discord.com/api/oauth2/authorize?client_id=930619804593819699&permissions=8&scope=bot%20applications.commands)'

        topgg = discord.Embed(title = 'Vote', 

        description = f'''
Muito obrigado por escolher votar em mim {ctx.author.mention}
isso me ajuda bastante e voce sabia que eu tbm tenho 
um server de suporte, está tudo aqui a baixo
''')
        topgg.add_field(name = f':grey_question: Está com alguma dúvidas? Entre no meu Servidor de Suporte!', value = server, inline = False)
        
        topgg.add_field(name = f'{e1} Quer me ajudar a crescer? Aqui está o link do Top.gg', 
        
            value = top, inline = False)

        topgg.add_field(name = f':partying_face: Querendo me convidar? Aqui está o link', 

            value = inv, inline = False)

        topgg.set_thumbnail(url = self.bot.user.avatar.url)

        await ctx.reply(embed = topgg)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def donate(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        embed = discord.Embed(title = 'Donate')

        embed.add_field(

        name = 'Metodos',

        value = 
        '''
Pix: rafaelucas@protonmail.com(Brasil)
Paypal: rafaelucas@protonmail.com
        ''')

        await ctx.reply(embed = embed)

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def Lembrete(self, ctx, tempo  = None, *, lembrete = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        if lembrete == None:

            ctx.reply('Você precisa escrever a descrição do lembrete')

        elif tempo == None:

            ctx.reply('Você precisa escolher o tempo do lembrete')

        embed = discord.Embed(color=self.bot.user.color)

        seconds = 0

        if lembrete is None:

            embed.add_field(name='Erro', value='Você precisa definir o lembrete')

        if tempo.lower().endswith("d"):

            seconds += int(tempo[:-1]) * 60 * 60 * 24

            counter = f"{seconds // 60 // 60 // 24} dias"

        if tempo.lower().endswith("h"):

            seconds += int(tempo[:-1]) * 60 * 60

            counter = f"{seconds // 60 // 60} horas"

        elif tempo.lower().endswith("m"):

            seconds += int(tempo[:-1]) * 60

            counter = f"{seconds // 60} minutos"

        elif tempo.lower().endswith("s"):

            seconds += int(tempo[:-1])

            counter = f"{seconds} segundos"

        if seconds == 0:

            embed.add_field(name='Erro',
                            value='A duração precisa ser maior que 0 Segundos')

        elif seconds > 7776000:

            embed.add_field(

            name='Erro', 

            value=
            '''
A duração desse lembrete é muito longo
Limite de dias é de 90 dias
            '''
            )

        else:

            await ctx.reply('Okay, Eu irei te lembrar de {} daqui a {}'.format(lembrete, counter))

            await asyncio.sleep(seconds)

            await ctx.reply('Ola {1}, estou passando aqui para te lembrar de "{0}" como você me pediu'.format(lembrete, ctx.author.mention))

            return

        await ctx.reply(embed=embed)

    @commands.command()
    async def botinfo(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        pyton = self.bot.get_emoji(971189876986884186)

        disocrd = self.bot.get_emoji(971212878763917362)

        bot = self.bot.get_emoji(971571054046773250)

        Vs = self.bot.get_emoji(971571518532354118)

        name = self.bot.get_emoji(971487187361218620)

        e = discord.Embed(title = 'Minhas informações')

        e.set_thumbnail(url = self.bot.user.avatar.url)

        e.add_field(name = f'{name} Nome', value = self.bot.user.name, inline = True)

        e.add_field(name = f'{Vs} Linguagem', value = f'{pyton} Python', inline = True)

        e.add_field(name = '════════════', value = '════════════', inline = False)

        e.add_field(name = f'{disocrd} Pycord Version', value = discord.__version__, inline = False)

        e.add_field(name = '════════════', value = '════════════', inline = False)

        e.add_field(name = f'{pyton} Python Version', value = platform.python_version())

        e.add_field(name = f'{bot} Comandos', value = len(self.bot.commands))

        e.add_field(name = '════════════', value = '════════════', inline = False)

        e.add_field(name = ':calendar_spiral: Ideia inicial', value = '2019', inline = True)

        e.add_field(name = ':calendar_spiral: Realização', value = '2021', inline = True)

        await ctx.reply(embed = e)
        
    @commands.command()
    async def EmojiInfo(self, ctx, emoji : discord.Emoji = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        if emoji == None:

            await ctx.reply('Você precisa colocar o emoji')

            return

        e1 = self.bot.get_emoji(971487187361218620)

        embed = discord.Embed(title = f'{emoji} Emoji Info')

        embed.set_thumbnail(url = emoji.url)

        embed.add_field(name = ':notepad_spiral: Nome do Emoji', value = emoji.name, inline = True)
        
        embed.add_field(name = f'{e1} Id do Emoji', value = emoji.id, inline = True)

        embed.add_field(name = ':goggles: Menção', value = f'`<:{emoji.name}:{emoji.id}>`', inline = True)

        embed.add_field(name = ':chains: Url', value = emoji.url, inline = True)

        embed.add_field(name = ':date: Adicionado em', value = emoji.created_at.strftime('%d %m %Y'), inline = True)

        embed.add_field(name = ':mag_right: Servidor de origem', value = emoji.guild, inline = True)


        await ctx.reply(embed = embed)

    @commands.command()
    async def emoji(self, ctx, emoji : discord.Emoji = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:
            
            return

        await ctx.reply(emoji)

    @hello.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @aleatorio.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @ping.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @servers.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')
    
    @userinfo.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @serverInfo.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @invite.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @hug.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @slap.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @kiss.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @shoot.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @punch.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @Vote.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @sad.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @donate.error
    async def o(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @Lembrete.error
    async def o(self, ctx: commands.Context, error):
        
        if isinstance(error, commands.CommandOnCooldown):

            cd = round(error.retry_after)

        if cd == 0:
            
            cd = 1

        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Gerais(bot))