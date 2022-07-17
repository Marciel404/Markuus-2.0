from Outhers.Infos.fi import *

class FeedBack(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def sugest(self, ctx, *, sugestão = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        
        user = self.bot.get_user(int(IdS))

        embed = discord.Embed(name = 'Sugest', 
        description = f'**Enviado por:** \n {ctx.author} \n\n **Sugestão:** \n {sugestão} \n\n  **No server:** \n {ctx.guild.name} \n\n **ID:** {ctx.author.id}')

        await ctx.reply('Sua sugestão foi enviada ao meu dono')

        await user.send(embed=embed)

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def report(self, ctx, *, report = None):

        rand = random.randint(0,2)

        if rand == 1:

            await ctx.reply('Sabia que Me manter está ficando dificil?\n que tal me ajudar doando algo?')

        elif ctx.author.id == banip:

            return
        
        
        user = self.bot.get_user(int(IdS))

        embed = discord.Embed(name = 'report', 
        description = f'**Enviado por:** \n {ctx.author} \n\n **Report:** \n {report} \n\n  **No server:** \n {ctx.guild.name} \n\n **ID:** {ctx.author.id}')

        await ctx.reply('Seu report foi enviada ao meu dono')

        await user.send(embed=embed)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(FeedBack(bot))