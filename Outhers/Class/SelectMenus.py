import discord

from Outhers.db.Economi import *

class staff(discord.ui.View):

    def __init__(self, timeout = 300):

        super().__init__(timeout=timeout)

    @discord.ui.select(
        placeholder = "Meus comandos!",
        options = [
            discord.SelectOption(
                label = 'Moderação',
                description = 'Mostra de moderação',
            ),
            discord.SelectOption(
                label = 'Gerais',
                description = 'Comandos gerais'
            ),
            discord.SelectOption(
                label = 'Economia',
                description = 'Commandos de economia'
            ),
            discord.SelectOption(
                label = 'Suporte',
                description = 'Comandos de suporte'
            ),
            discord.SelectOption(
                label = 'Imagens',
                description = 'Comandos de imagens'
            )
        ]
    )
    async def select_callback(self,  select, interaction : discord.Interaction):

        if select.values[0] == 'Moderação':
            m = discord.Embed(title = 'Meus comandos',
            description = '**Nome/Permissão/Função**',
            color = 000000)
            m.add_field(
            name = 'Moderação',
            value = 
            '''
Ban - (Ban members) - Bane membros no seu servidor
BanId - (Ban Members) - Bane uma pessoa que não está no seu server pelo id
Unban - (Ban Members) - Desbane um membro no seu servr
Kick - (Kick Members) - Expulsa uma pessoa do seu server
Clear - (Manage channels) - Limpa o chat do seu server
Say - (Administrator) - Fala algo no server
SetLogs - (Manage_chnnels) - Seta o canal de logs do bot
AutoRole - (Manage_chnnels) - Seta um cargo para Autorole
Setprefix - (Administrator) - Seta o prefixo do bot
            ''',
            inline = False)
            m.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/930619804593819699/7f52c9696a8ee80732bcf7796429845e.webp?size=1024')
            await interaction.response.edit_message(embed = m)
        elif select.values[0] == 'Gerais':
            g = discord.Embed(title = 'Meus comandos',
            color = 000000)
            g.add_field(
            name='Gerais',
            value = 
            '''
Hello - Comando teste do markuus
Aleatorio - Escolhe um numero aleatorio para você
Ping - Mostra o meu ping e da api do discord
Servers - Diz em quantos servers eu estou
Userinfo - puxa as informações de algum membro ou as suas
ServerInfo - puxa as informações do server
Invite - Manda o link para convidar o bot
Hug - Abraça um membro
slap - Bate em algum membro
kiss - Beija um membro
Shoot - Atira em algum membro
Punch - Soca algum membro
Donate - Envia as formas de ajudar o bot
Lembrete -  Define um lembrete
            ''',
            inline = False)
            g.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/930619804593819699/7f52c9696a8ee80732bcf7796429845e.webp?size=1024')

            await interaction.response.edit_message(embed=g)
        elif select.values[0] == 'Economia':
            e = discord.Embed(title = 'Meus comandos',
            color = 000000)
            e.add_field(
            name= 'Comandos Economia', 
            value=
            '''
Rolar - Voce pode ganhar de 0 a 2000 edinhos
Edinhos - Mostra quantos edinhos você tem ou do membro mencionado
Edinhostop - Mostra o rank de pessoas mais ricas
Loteria - Você pode apostar na sorte e quadruplicar seus edinhos
Transferir - Você pode transferir edinhos para outras pessoas
ccap - Jogue cara ou coroa valendo seus edinhos
Shop - Compra itens e venda
Inventario - Mostra os itens do seu iventario
Minerar - Minera, tem chance de vir recursos
Craft - Crafta alguns itens
            ''',
            inline = False)
            e.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/930619804593819699/7f52c9696a8ee80732bcf7796429845e.webp?size=1024')

            await interaction.response.edit_message(embed=e)

        elif select.values[0] == 'Suporte':

            s = discord.Embed(title = 'Meus comandos',
            color = 000000)
            s.add_field(
                name = 'Comandos suporte',
                value = 
                '''
Ticket - Cria um ticket no server
Ft - Fecha um ticket aberto
Adc - Adiciona um membro ao ticket
Rmv - Remove um membro do ticket
Sugest - Envia uma sugestão para meu dono
Report - Envia um report para meu dono
                ''',
                inline = False)
            s.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/930619804593819699/7f52c9696a8ee80732bcf7796429845e.webp?size=1024')

            await interaction.response.edit_message(embed=s)
        elif select.values[0] == 'Imagens':
            i = discord.Embed(title = 'Meus comandos',
            color = 000000)
            i.add_field(
                name = 'Imagens',
                value = 
                '''
ConquistaMine - Criar uma conquista do minecraft
Perfeição - Cria um meme de "perfeição"
Safadão -  envia uma imagem do Meliodas "safadão"
                ''',
                inline = False)
            i.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/930619804593819699/7f52c9696a8ee80732bcf7796429845e.webp?size=1024')

            await interaction.response.edit_message(embed=i)

class shop(discord.ui.View):

    def __init__(self, timeout = 300):

        super().__init__(timeout=timeout)

    @discord.ui.select(
            placeholder = 'Mercado',
            options = [
                discord.SelectOption(
                    label = 'Minerios',
                    description = 'Lista os minerios do mercado'
                ),
                discord.SelectOption(
                    label = 'Utilitarios',
                    description = 'Lista os utilitarios do mercado'
                ),
                discord.SelectOption(
                    label = 'Cosmeticos',
                    description = 'Lista os cosmeticos do mercado'
                ),
            ]
        )
    async def select_callback(self, select, interaction : discord.Interaction):
        if select.values[0] == 'Minerios':

            embed = discord.Embed(title = 'Minerios')
            for i in Minerios:
                name = i["Nome"]
                compra = i["compra"]
                venda = i["Venda"]
                embed.add_field(name = name, value = f'Compra {compra}\n Venda {venda}')

            await interaction.response.edit_message(embed = embed)
        elif select.values[0] == 'Utilitarios':

            embed = discord.Embed(title = 'Utilitarios')
            for i in utilitarios:
                name = i["Nome"]
                compra = i["compra"]
                venda = i["Venda"]
                embed.add_field(name = name, value = f'Compra {compra}\n Venda {venda}')

            await interaction.response.edit_message(embed = embed)
        elif select.values[0] == 'Cosmeticos':

            embed = discord.Embed(title = 'Cosmeticos')
            for i in cosmeticos:
                name = i["Nome"]
                compra = i["compra"]
                venda = i["Venda"]
                embed.add_field(name = name, value = f'Compra {compra}\n Venda {venda}')

            await interaction.response.edit_message(embed = embed)