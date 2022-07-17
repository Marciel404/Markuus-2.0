from Outhers.Infos.fi import *

class Moderação(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def setlogs(self, ctx, id: discord.TextChannel = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        server1 = {"_id": ctx.guild.id}

        if id == None:

            await ctx.reply('Chat de logs removido')

            logs.remove(server1)
            
        id2 = int(id.id)

        server = {"_id": ctx.guild.id, "Nome": ctx.guild.name, "canal": id2}

        myquery = { "_id": ctx.guild.id}   

        if (logs.count_documents(myquery) == 0):

            logs.insert_one(server)

            await ctx.reply('Canal de logs setado para {}, se desejar remover as logs use o comando sem mencionar um chat'.format(id.mention))

        else:

            logs.update_one({"_id" : ctx.guild.id}, {"$set":{"canal": id2}})

            await ctx.reply('Canal de logs setado para {}, se desejar remover as logs use o comando sem mencionar um chat'.format(id.mention))
            
    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def setprefix(self, ctx, prefixo = None):

        rand = random.randint(0,2)

        if rand == 1:
            
            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')
            
        elif ctx.author.id == banip:

            return

        prefix.update_one({"_id": ctx.guild.id}, {"$set": {"prefix": prefixo}})

        await ctx.reply('Prefixo mudado para {}'.format(prefixo))

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def autorole(self, ctx, cargo: discord.Role = None):
        rand = random.randint(0,2)

        if ctx.author.id == banip:

            return

        elif rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        else:
            
            cargo2 = cargo.name

            if cargo == None:

                autorule.delete_one({"_id" : ctx.guild.id})

                await ctx.reply('Auto Role desativado')
                
            server = {"_id": ctx.guild.id, "Nome": ctx.guild.name, "Role": cargo2}

            myquery = { "_id": ctx.guild.id}   

            if (autorule.count_documents(myquery) == 0):

                autorule.insert_one(server)

                await ctx.reply('Auto Role setado para o cargo {}'.format(cargo.mention))

            else:

                await ctx.reply('Auto Role setado para o cargo {}'.format(cargo.mention))

                autorule.update({"_id" : ctx.guild.id}, {"$set":{"Role": cargo2}})

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, membro: discord.Member = None, *,motivo=None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:
            
            return

        log = logs.find_one({"_id": ctx.guild.id})

        log2 = log["canal"]

        l1 = self.bot.get_channel(log2)

        if motivo == None:

            motivo = 'Motivo não informado'

        e1 = discord.Embed(title = 'kick', description = f'Voce esta prestes a expulsar {membro.mention}')

        R = f'Pessoa expulsa: {membro} \n Quem expulsou: {ctx.author.name} \n Motivo: {motivo}'

        E = discord.Embed(title = 'kick', description = f'Pessoa expulsa: {membro} \n Quem expulsou: {ctx.author.mention} \n motivo: {motivo}')

        if membro == self.bot.user:

            await ctx.reply('Não posso expulsar a mim mesmo')

            return

        elif  membro == ctx.author:

            await ctx.reply('Você não pode expulsar a si mesmo')

            return

        message = await ctx.reply(embed = e1)

        await message.add_reaction("✅")

        await message.add_reaction("❎")

        def check(reaction, user):

            return user == ctx.author and str(reaction.emoji) in ["✅", "❎"]

        try:
            reaction, user = await self.bot.wait_for("reaction_add", check=check)

            if str(reaction.emoji) == "✅":

                await message.delete()

                try:

                    await l1.send(embed = E)

                    await ctx.reply(f'{membro.name} expulso com sucesso')

                    await membro.guild.kick(reason = R)

                except:

                    await ctx.reply(embed = E)

                    await ctx.reply('Canal de logs não setado use o setlogs')

                    await membro.guild.kick(reason = R)

            elif str(reaction.emoji) == "❎":

                await message.delete()

                await ctx.reply(f'ufa, ainda bem que expulsar o {membro.mention}')

        except asyncio.TimeoutError:

            return

    @commands.command()
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Ban(self, ctx, membro: discord.Member = None, *,motivo=None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        log = logs.find_one({"_id": ctx.guild.id})

        log2 = log["canal"]

        l1 = self.bot.get_channel(log2)

        if motivo == None:

            motivo = 'Motivo não informado'

        else:

            motivo = motivo

        e1 = discord.Embed(title = 'kick', description = f'Voce esta prestes a expulsar {membro}')

        R = f'Pessoa expulsa: {membro} \n Quem expulsou: {ctx.author.name} \n Motivo: {motivo}'

        E = discord.Embed(title = 'kick', description = f'Pessoa expulsa: {membro} \n Quem expulsou: {ctx.author.mention} \n motivo: {motivo}')

        if membro == self.bot.user:

            await ctx.reply('Não posso expulsar a mim mesmo')

        elif  membro == ctx.author:

            await ctx.reply('Você não pode expulsar a si mesmo')
        
        elif membro == None:

            await ctx.reply('Você precisa mencionar uma pessoa para banir')

        else:

            message = await ctx.reply(embed = e1)

            await message.add_reaction("✅")

            await message.add_reaction("❎")

            def check(reaction, user):

                return user == ctx.author and str(reaction.emoji) in ["✅", "❎"]

            try:

                reaction, user = await self.bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "✅":

                    await message.delete()

                    try:

                        await l1.send(embed = E)

                        await ctx.reply(f'{membro.name} banido com sucesso')

                        await membro.ban(reason = R)

                    except:

                        await ctx.reply(embed = E)

                        await ctx.reply('Canal de logs não setado use o setlogs')

                        await membro.ban(reason = R)

                elif str(reaction.emoji) == "❎":

                    await message.delete()

                    await ctx.reply(f'ufa, ainda bem que banir o {membro}')
                                
            except asyncio.TimeoutError:
                return

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_channels = True)
    async def say(self, ctx, *, msg = None):

        if msg == None:

            await ctx.reply('Você precisa falar algo')

        else:

            await ctx.message.delete()

            await ctx.send(f'{msg} \n\nFalado por {ctx.author.mention}')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(manage_channels = True)
    @commands.has_permissions(manage_channels = True)
    async def clear(self, ctx, quantidade = 0):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
            
        if quantidade > 1000:

            await ctx.reply('O limite maximo é de 1000 palavras')

            return
            
        elif quantidade == 0:

            await ctx.reply('Você precisa escolher uma quantidade de mensagens, a quantidade maxima é 1000 mensagens')

        else:

            purge = await ctx.channel.purge(limit=quantidade)

            await ctx.reply(f"O chat teve {len(purge)} mensagens apagadas por {ctx.author.mention}")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def banid(self, ctx, membro: int, *,motivo=None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
            
        log = logs.find_one({"_id": ctx.guild.id})

        log2 = log["canal"]

        l1 = self.bot.get_channel(log2)

        member1 = await self.bot.fetch_user(membro)

        if motivo == None:

            motivo = 'Motivo não informado'

        else:

            motivo = motivo

        e1 = discord.Embed(title = 'BanId', description = f'Voce esta prestes a banir {membro}')

        R = f'Pessoa banida: {membro} \n Quem baniu: {ctx.author.name} \n Motivo: {motivo}'

        E = discord.Embed(title = 'ban', description = f'Pessoa banida: <@{membro}> \n Quem baniu: {ctx.author.mention} \n Motivo: {motivo} \n id: {membro}')

        if membro == self.bot.user:

            await ctx.reply('Não posso banir a mim mesmo')

        elif  membro == ctx.author:

            await ctx.reply('Você não pode banir a si mesmo')

        else:

            message = await ctx.reply(embed = e1)

            await message.add_reaction("✅")

            await message.add_reaction("❎")
                        
            def check(reaction, user):

                return user == ctx.author and str(reaction.emoji) in ["✅", "❎"]

            try:

                reaction, user = await self.bot.wait_for("reaction_add", check=check)

                if str(reaction.emoji) == "✅":

                    await message.delete()

                    try:

                        await ctx.guild.ban(member1, reason = R)

                        await l1.send(embed = E)

                        await ctx.reply(f'{membro} banido com sucesso')

                    except Exception:

                        await ctx.guild.ban(member1, reason = R)

                        await ctx.reply(embed = E)

                        await ctx.reply('Canal de logs não setado use o setlogs')

                elif str(reaction.emoji) == "❎":

                    await message.delete()

                    await ctx.reply(f'ufa, ainda bem que banir o {membro}')

            except asyncio.TimeoutError:

                return

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id: int, *, razão = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        log = logs.find_one({"_id": ctx.guild.id})

        log2 = log["canal"]

        l1 = self.bot.get_channel(log2)

        if razão == None:

            razão = 'Não informado'

        else:

            razão = razão

        e = discord.Embed(title = 'UnBan',

        description = f'Quem desbaniu: {ctx.author}\n quem foi desbanido: <@{id}> \nrazão: {razão}')

        try:

            user = await self.bot.fetch_user(id)

            await ctx.guild.unban(user)

            await l1.send(embed = e)

            await ctx.reply(f'{id} desbanido com sucesso')
            
        except:

            user = await self.bot.fetch_user(id)

            await ctx.guild.unban(user)

            await ctx.reply(embed = e)


    @autorole.error
    async def setlogs_error(self,ctx: commands.context, error):

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.reply(":x: || Você não tem permissão para usar esse comando")

    @kick.error
    async def kick_error(self,ctx, error):

        if isinstance(error, commands.CommandOnCooldown):

            await ctx.reply(':x: || Você precisa esperar 5 segundos parta usar esse comando de novo')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.reply(":x: || Você não tem permissão para usar esse comando")

        if isinstance(error, commands.BadArgument):

            await ctx.reply(':x: || Eu não encontrei esse membro no server para expulsar')

        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.reply(':x: || Desculpa, mas eu não tenho permissão "Kick_Members" para usar esse commando')

    @Ban.error
    async def ban_error(self,ctx: commands.context, error):

        if isinstance(error, commands.CommandOnCooldown):

            await ctx.reply(':x: || Você precisa esperar 5 segundos parta usar esse comando de novo')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.reply(":x: || Você não tem permissão para usar esse comando")

        if isinstance(error, commands.MemberNotFound):

            await ctx.reply(':x: || Eu não encontrei esse membro no server para banir, se deseja banir ele, use o "BanId"')

        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.reply(':x: || Desculpa, mas eu não tenho permissão "Ban_Members" para usar esse commando')

    @unban.error
    async def unban_error(self,ctx: commands.context, error):

        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.reply(':x: || Desculpa, mas eu não tenho permissão "Ban_Members" para usar esse commando')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.reply(":x: || Você não tem permissão para usar esse comando")

        if isinstance(error, commands.MemberNotFound):

            await ctx.reply(':x: || Não encontrei esse membro nos ban do server')

    @say.error
    async def say_error(self,ctx: commands.context, error):

        if isinstance(error, commands.CommandOnCooldown):

            await ctx.reply(f':x: || Você precisa esperar 5 segundos para  usar esse comando de novo')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.reply(":x: || Você não tem permissão para usar esse comando")

    @clear.error
    async def clear_error(self,ctx: commands.context, error):

        if isinstance(error, commands.CommandOnCooldown):

            await ctx.reply(f':x: || Você precisa esperar 5 segundos para  usar esse comando de novo')
        
        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.reply(':x: || Desculpa, mas eu não tenho permissão "Manage_chennels" para usar esse commando')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.reply(":x: || Você não tem permissão para usar esse comando")

    @banid.error
    async def clear_error(self,ctx: commands.context, error):

        if isinstance(error, commands.CommandOnCooldown):

            await ctx.reply(f':x: || Você precisa esperar 5 segundos para  usar esse comando de novo')
        
        if isinstance(error, commands.BotMissingPermissions):
            
            await ctx.reply(':x: || Desculpa, mas eu não tenho permissão "Manage_chennels" para usar esse commando')

        if isinstance(error, commands.MissingPermissions):
            
            await ctx.reply(":x: || Você não tem permissão para usar esse comando")

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Moderação(bot))