from Outhers.Infos.fi import *

class Economia(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def edinhos(self, ctx, membro: discord.Member = None):
        
            rand = random.randint(0,2)

            if rand == 1:

                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

            elif ctx.author.id == banip:

                return
            
            if membro == None:

                membro = ctx.author

            else:

                membro = membro

            await open_account(membro)

            bal = bank.find_one({"_id": membro.id})
            
            em = discord.Embed(title = f"{membro.name} Edinhos", color = discord.Color.red())

            em.add_field(name ='Edinhos', value = bal["Edinhos"])


            await ctx.reply(embed = em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Transferir(self, ctx, membro: discord.Member = None, edinhos = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        if ctx.author.id == banip:

            return

        if membro == None:

            await ctx.reply('Você precisa mencionar alguem')

            return

        if edinhos == None:

            await ctx.reply('Você precisa escolher a quantidade para transferir')

            return

        if membro.bot:

            await ctx.reply('Você não pode transferir dinheiro para bots')

            return

        await open_account(ctx.author)

        await open_account(membro)

        bal = bank.find_one({"_id": ctx.author.id})

        dindin = int(edinhos)

        b1 = bal["Edinhos"]

        if dindin > b1:

            await ctx.reply(f'Você não tem dinheiro suficiente')

            return

        elif dindin == 0:

            await ctx.reply('A quantia tem que ser maior que zero')

            return

        elif dindin < 0:
            await ctx.reply(f'A quantia deve ser positiva')

            return

        await update_bank(ctx.author,- dindin)

        await update_bank(membro,+ dindin)

        await ctx.reply('Voce transferiu {1} edinhos para {0}'.format(membro.mention, dindin))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def loteria(self, ctx, edinhos = None):

            rand = random.randint(0,2)

            if rand == 1:

                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

            elif ctx.author.id == banip:

                return
            
            await open_account(ctx.author)

            if edinhos == None:

                await ctx.reply(f'Você precisa selecionar uma quantidade de edinho para Jogar')

            bal = bank.find_one({"_id": ctx.author.id})

            dindin = int(edinhos)

            if dindin > bal["Edinhos"]:

                await ctx.reply(f'Você não tem dinheiro suficiente')

                return

            elif dindin == 0:

                await ctx.reply('A quantia deve ser maior que 0')
            
                return

            elif dindin < 0:

                await ctx.reply(f'A quantia deve ser positiva')

                return

            final = []

            for i in range(3):

                a = random.choice([':pineapple:',':grapes:',':kiwi:',])

                final.append(a)

            await ctx.reply(str(final))


            if final[0] == final[1] == final[2]:

                await update_bank(ctx.author,4*dindin)

                await ctx.reply(f'Você ganhou {4*dindin} edinhos!!')

            else:

                await update_bank(ctx.author,-1*dindin)

                await ctx.reply(f'Você perdeu {dindin} edinhos')

    @commands.command(aliases = ['ccap'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Caraoucoroaap(self, ctx, edinhos: int = None, escolha = None):

            rand = random.randint(0,2)

            if rand == 1:

                await ctx.send('Sabia que Me manter está ficando dificil?\nQue tal me ajudar doando algo?')

            elif ctx.author.id == banip:

                return

            if edinhos == None:

                await ctx.reply('Você precisa escolher uma quantidade de edinhos para apostar')

            elif escolha == None:

                await ctx.reply('Você precisa escolher cara ou coroa')
            
            bal = bank.find_one({"_id": ctx.author.id})

            dindin = int(edinhos)

            if dindin > bal["Edinhos"]:

                await ctx.reply(f'Você não tem dinheiro suficiente para apostar')

                return

            elif dindin < 0:

                await ctx.reply(f'A quantia deve ser positiva')

                return


            random1 = random.choice(['cara', 'coroa'])

            if random1 == escolha.lower():

                await ctx.reply(f'Caiu {escolha}\nParabens, você ganhou {dindin*2} edinhos')

                await update_bank(ctx.author, + dindin*2)

            elif random1 != escolha.lower():

                await ctx.reply(f'Caiu {random1}\nSad, você perdeu {dindin} edinhos')

                await update_bank(ctx.author, - dindin)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def edinhostop(self, ctx):

            rand = random.randint(0,2)

            if rand == 1:

                await ctx.reply('Sabia que Me manter está ficando dificil?\nque tal me ajudar doando algo?')

            elif ctx.author.id == banip:

                return

            rankings = bank.find().sort("Edinhos",-1)

            i=1

            embed = discord.Embed(title = f"***Top 5 mais ricos***")

            for x in rankings:

                user_xp = x["Edinhos"]

                embed.add_field(name=f"{i}: {x['Nome']}", value=f"{user_xp}", inline=False)

                if i == 5:

                    break

                else:

                    i += 1

            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon}")

            await ctx.reply(embed=embed)

    @commands.command(aliases = ['mercado'])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def Shop(self, ctx, opção = None, qnd = None, *,item = None):
        rand = random.randint(0,2)
        
        if rand == 1:

            await ctx.send('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        embed = discord.Embed(title = 'Mercado')

        await open_inv(ctx.author)

        if opção == None:

            embed = discord.Embed(title = 'Mercado',

        description = '''
Ande pelos setores do mercado
e escolha o que comprar
        ''')

            await ctx.reply(embed = embed, view = shop())

        elif opção.lower() == 'buy':

            if qnd == None:

                await ctx.reply('Você precisa escolher a quantidade que deseja comprar')

            elif item == None:

                await ctx.reply('Você precisa escrever o que deseja comprar')

            else:

                item_name = item.capitalize()

                await open_inv(ctx.author)

                for it in shopping:

                    name = it["Nome"]

                    if name == item_name:

                        price = it["compra"]

                        print(price,int(qnd))

                        cost = price*int(qnd)

                        bal = bank.find_one({"_id": ctx.author.id})

                        if bal['Edinhos'] < cost:

                            await ctx.reply('Você não tem edinhos suficientes')

                        else:
                        
                            q = None

                            if int(qnd) == 1:

                                q = 'unidade'

                            elif int(qnd) > 1:

                                q = 'unidades'

                            await ctx.reply(f'Você comprou {int(qnd)} {q} de {item} por {cost} edinhos')

                            await update_bank(ctx.author, - cost)

                            await update_inv(ctx.author, item_name, int(qnd))

        elif opção.lower() == 'sell':

            if qnd == None:

                await ctx.reply('Você precisa escolher a quantidade que deseja vender')

            elif item == None:

                await ctx.reply('Você precisa escrever o que deseja vender')

            else:

                item_name = item.capitalize()

                item_name2 = item.lower()

                await open_inv(ctx.author)

                for it in shopping:

                    name = it["Nome"]

                    if name == item_name:

                        price = it["Venda"]

                        cost = price*int(qnd)

                        bal = inv.find_one({"_id": ctx.author.id})

                        if bal[f'{item_name2}'] < 1:

                            await ctx.reply('Você não tem esse item para vender')

                        else:
                        
                            q = None

                            if int(qnd) == 1:

                                q = 'unidade'

                            elif int(qnd) > 1:

                                q = 'unidades'

                            await ctx.reply(f'Você vendeu {int(qnd)} {q} de {item} por {cost} edinhos')
                            
                            await update_bank(ctx.author, + cost)

                            await update_inv(ctx.author, item_name, - int(qnd))

    @commands.command(aliases = ['inv'])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def inventario(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        await open_inv(ctx.author)
            
        await reload_inv(ctx.author)

        await ctx.send('Deseseja ver seu Inventario?', view = confirminv())
                
        
    @commands.command(aliases = ['craftar'])
    @commands.cooldown(1,5, commands.BucketType.user)
    async def craft(self, ctx, opção = None, *, craft = None):

            rand = random.randint(0,2)

            if rand == 1:

                await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

            elif ctx.author.id == banip:
                
                return
            
            if opção == None:

                e = discord.Embed(title = 'Crafts')

                for i in crafts:

                    name = i["Nome"]

                    compra = i["1"]

                    venda = i["2"]

                    e.add_field(name = name, value = f' {compra}\n {venda}')

                await ctx.reply(embed = e)

            elif opção == 'craftar':

                item_ = craft.lower()

                b1 = inv.find_one({"_id": ctx.author.id})

                if item_ == 'picareta diamante':

                    if b1['madeira'] < 1:

                        await ctx.reply('Você não tem madeira suficiente')

                        return
                    elif b1['diamante'] < 10:

                        await ctx.reply('Você não tem diamante suficiente')

                        return
                    else:

                        await update_inv(ctx.author, 'madeira', - 1)

                        await update_inv(ctx.author, 'diamante', -3)

                        await update_inv(ctx.author, 'picareta diamante', 1)

                        await ctx.reply('Picareta diamante craftada com sucesso')
                
                elif item_ == 'picareta ferro':

                    if b1['madeira'] < 1:

                        await ctx.reply('Você não tem madeira suficiente')

                        return
                    elif b1['ferro'] < 5:

                        await ctx.reply('Você não tem ferro suficiente')

                        return
                    else:
                        await update_inv(ctx.author, 'madeira', - 1)

                        await update_inv(ctx.author, 'ferro', -3)

                        await update_inv(ctx.author, 'picareta ferro', 1)

                        await ctx.reply('Picareta ferro craftada com sucesso')
            
                elif item_ == 'picareta ouro':

                    if b1['madeira'] < 1:

                        await ctx.reply('Você não tem madeira suficiente')

                        return

                    elif b1['ouro'] < 6:

                        await ctx.reply('Você não tem ouro suficiente')

                        return
                    else:
                        await update_inv(ctx.author, 'madeira', - 1)

                        await update_inv(ctx.author, 'ouro', -3)

                        await update_inv(ctx.author, 'picareta ouro', 1)

                        await ctx.reply('Picareta ouro craftada com sucesso')

    @edinhos.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

        if isinstance(error, commands.MemberNotFound):

            await ctx.reply('Não encontrei esse membro no server')

    @edinhostop.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @loteria.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @Transferir.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

        if isinstance(error, commands.MemberNotFound):

            await ctx.reply('Não encontrei esse membro no server')

    @Caraoucoroaap.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @inventario.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @craft.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Economia(bot))