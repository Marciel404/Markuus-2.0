from Outhers.Infos.fi import *

class Dono(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def anun(self, ctx, id: discord.TextChannel, *, msg):
        if ctx.author.id != IdS:
            return

        id2 = int(id.id)

        channel = self.bot.get_channel(id2)

        await channel.send(msg)

    @commands.command()
    async def RS(self, ctx, id, *,msg):

        if ctx.author.id != IdS:
            return

        user = self.bot.get_user(int(id))

        try:

            await user.send(f'{msg}')

            await ctx.send('Enviado Krai')

        except Exception:

            await ctx.send('Não consegui mandar mensagem para esse membro')

    @commands.command()
    async def SetE(self,ctx, id: int, *, dindin = 0):
            
        if ctx.message.author.id != IdS:
            return

        user = self.bot.get_user(id)

        await open_account(user)

        SetM = int(dindin)

        await update_bank(user, + dindin)
                
        try:
            await user.send(f'Seus {SetM} foram setados <@{id}>')
            await ctx.send(f'Foram dados {SetM} edinhos para <@{id}>')
        except:
            await ctx.send(f'Foram dados {SetM} edinhos para <@{id}>')

    @commands.command()
    async def RmvE(self,ctx, id: int, *, dindin = 0):
            
        if ctx.author.id != IdS:
            return

        if dindin == 0:
            await ctx.send(f'Nenhum edinho foi setado para <@{id}>')
        else:

            user = self.bot.get_user(id)

            await open_account(user)

            SetM = int(dindin)
                
            await ctx.send(f'Foram removidos {SetM} edinhos para <@{id}>')

            await update_bank(user, - dindin)

def setup(bot:commands.Bot):
    bot.add_cog(Dono(bot))