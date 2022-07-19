import discord

from Outhers.db.Economi import *

class confirminv(discord.ui.View):

    def __init__(self, timeout = 180):

        super().__init__(timeout = timeout)
        
    @discord.ui.button(label = 'Ver', style = discord.ButtonStyle.blurple)
    async def confirm(self,  button: discord.ui.Button, interaction: discord.Interaction):

        inv2 = inv.find_one({"_id": interaction.user.id})

        embed = discord.Embed(

        title = 'Inventario',

        description = 
        f'''
Picareta ferro {inv2['picareta ferro']}
Picareta de ouro {inv2['picareta ouro']}
Picareta de diamante {inv2['picareta diamante']}
Carro {inv2['carro']}
Arma {inv2['arma']}
Diamante {inv2['diamante']}
Ouro {inv2['ouro']}
Anel de casamento {inv2['anel casamento']}
Ferro {inv2['ferro']}
Madeira {inv2['madeira']}
Computador {inv2['computador']}
        ''')

        await interaction.response.send_message(embed = embed, ephemeral = True)
        
        self.stop()

class ticket(discord.ui.View):
    
    def __init__(self):

        super().__init__(timeout = None)
        
    @discord.ui.button(label = '📩', style = discord.ButtonStyle.blurple)
    async def confirm(self,  button: discord.ui.Button, interaction: discord.Interaction):

        guild = interaction.guild

        Chat = discord.utils.get(guild.channels, name=f'ticket-{interaction.user.id}')

        if Chat is None:

            guild = interaction.guild

            ticket = f'ticket-{interaction.user.id}'

            member = interaction.user

            admin = discord.utils.get(guild.roles, name="Admin")
            
            mod = discord.utils.get(guild.roles, name="Mod")

            suporte = discord.utils.get(guild.roles, name="Suporte")

            overwrites = {

                guild.default_role: discord.PermissionOverwrite(read_messages=False),

                member: discord.PermissionOverwrite(read_messages=True),

                admin:  discord.PermissionOverwrite(read_messages=True),

                mod:  discord.PermissionOverwrite(read_messages=True),

                suporte:  discord.PermissionOverwrite(read_messages=True)

                }

            channel = await guild.create_text_channel(name=ticket, overwrites = overwrites)

            await interaction.response.send_message('Ticket criado com sucesso', ephemeral = True)

            await channel.send(f'{interaction.user.mention} {admin.mention} {mod.mention} {suporte.mention}')
        
        else:

            await interaction.response.send_message('Ticket já existente, encerre o ultimo para criar outro', ephemeral = True)