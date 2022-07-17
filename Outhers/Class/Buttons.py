import discord

class help(discord.ui.View):
    def __init__(self, timeout = 180):

        super().__init__(timeout=timeout)

        self.value = None

    @discord.ui.button(label="0️⃣",style=discord.ButtonStyle.blurple)
    async def help(self, interaction: discord.Interaction, button: discord.ui.Button):
        h = discord.Embed(
        title = 'Meus Comandos',
        description = 
        '''
0️⃣ | Menu.....1️⃣ | Moderação
2️⃣ | Gerais....3️⃣ | Economia
4️⃣ | Suporte.5️⃣ | Imagens
        ''')
        h.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/930619804593819699/7f52c9696a8ee80732bcf7796429845e.webp?size=1024')
        await interaction.response.edit_message(embed=h)
        self.value = False

    @discord.ui.button(label="1️⃣",style=discord.ButtonStyle.blurple)
    async def mod(self, interaction: discord.Interaction, button: discord.ui.Button):

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
        
        await interaction.response.edit_message(embed=m)
        self.value = False

    @discord.ui.button(label="2️⃣",style=discord.ButtonStyle.blurple)
    async def gerais(self, interaction: discord.Interaction, button: discord.ui.Button):

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
        self.value = False

    @discord.ui.button(label="3️⃣",style=discord.ButtonStyle.blurple)
    async def economis(self, interaction: discord.Interaction, button: discord.ui.Button):

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
        self.value = False

    @discord.ui.button(label="4️⃣",style=discord.ButtonStyle.blurple)
    async def suporte(self, interaction: discord.Interaction, button: discord.ui.Button):
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
        self.value = False

    @discord.ui.button(label="5️⃣",style=discord.ButtonStyle.blurple)
    async def imagens(self, interaction: discord.Interaction, button: discord.ui.Button):

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
        self.value = False

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