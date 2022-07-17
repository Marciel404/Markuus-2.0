from Outhers.Infos.fi import *

class Atendimento(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx):
        rand = random.randint(0,2)
        
        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        guild = ctx.guild

        Chat = discord.utils.get(guild.channels, name=f'ticket-{ctx.author.id}')

        if Chat is None:

            guild = ctx.guild

            embed = discord.Embed(

                    title = 'Ticket criado com sucesso',

                    description = 'Agora só esperar a resposta',

                    color = 0
                )

            embed.set_footer(text=f'Ticket de {ctx.author.name}')

            msg = await ctx.reply(embed=embed)

            await msg.add_reaction("📩")

            ticket = f'ticket-{ctx.author.id}'

            member = ctx.author

            overwrites = {

                guild.default_role: discord.PermissionOverwrite(read_messages=False),

                member: discord.PermissionOverwrite(read_messages=True),

                }

            channel = await guild.create_text_channel(name=ticket, overwrites = overwrites)

            await channel.send(ctx.author.mention)

        else:

            await ctx.reply('Ticket já existente, encerre o ultimo para criar outro')

    @commands.command()
    async def ft(self, ctx):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        

        if f'ticket-{ctx.author.id}' in ctx.channel.name:

            await ctx.channel.delete()

        elif f'ticket-' in ctx.channel.name and ctx.author.guild_permissions.manage_channels:

            await ctx.channel.delete()

        else:

            await ctx.reply('Esse não é um chat  de ticket')
        

    @commands.command()
    async def adc(self, ctx, id: discord.Member):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        if f'ticket-{ctx.author.id}' in ctx.channel.name or ctx.author.guild_permissions.manage_channels:

            await ctx.channel.set_permissions(id, read_messages=True)

            await ctx.reply(f'{id.mention} adicionado')

        elif ctx.channel.name != f'ticket-{ctx.author.id}':

            await ctx.reply('Este ticket não te pertence ou você não pode gerenciar canais')

    @commands.command()
    async def rmv(self, ctx, membro: discord.Member):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return

        if f'ticket-{ctx.author.id}' in ctx.channel.name or ctx.author.guild_permissions.manage_channels:

            await ctx.channel.set_permissions(membro, read_messages=False)

            await ctx.reply(f'{membro.mention}')

        elif ctx.channel.name != f'ticket-{ctx.author.id}':

            await ctx.reply('Este ticket não te pertence ou você não pode gerenciar canais')

    @ticket.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')
    
    @ft.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @adc.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

    @rmv.error
    async def beg_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            cd = round(error.retry_after)
        if cd == 0:
            cd = 1
        await ctx.reply(f'Você precisa esperar {better_time(cd)} para  usar esse comando de novo')

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Atendimento(bot))