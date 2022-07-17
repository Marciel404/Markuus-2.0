import discord

Game = discord.Game(name = f'Estou em desenvolvimento')

listening  =  discord.Activity(type = discord.ActivityType.listening, name = f"Futuras atualizações por vir")

stream = discord.Streaming(name = 'Meu criador', url = 'https://www.twitch.tv/mncoverz')

watching = discord.Activity(type = discord.ActivityType.watching, name = f'Meu criador fazendo novos codigos')

def better_time(cd:int):

        time = f"{cd} s"

        if cd > 60:

            minutes = cd - (cd % 60)

            seconds = cd - minutes

            minutes = int(minutes/ 60)

            time = f"{minutes}min {seconds}s"

            if minutes > 60:

                hoursglad = minutes -(minutes % 60)

                hours = int(hoursglad/ 60)

                minutes = minutes - (hours*60)

                time = f"{hours}h {minutes}min {seconds}s"

        return time

punch = [
    'https://c.tenor.com/6a42QlkVsCEAAAAd/anime-punch.gif',
    'https://c.tenor.com/UH8Jnl1W3CYAAAAS/anime-punch-anime.gif',
    'https://c.tenor.com/SwMgGqBirvcAAAAS/saki-saki-kanojo-mo-kanojo.gif',
    'https://c.tenor.com/wYyB8BBA8fIAAAAS/some-guy-getting-punch-anime-punching-some-guy-anime.gif',
    'https://c.tenor.com/hs6GB44v8aQAAAAd/one-punch-man-%E3%83%AF%E3%83%B3%E3%83%91%E3%83%B3%E3%83%9E%E3%83%B3.gif',
    'https://c.tenor.com/s0bU-NO1QIQAAAAS/anime-punch.gif',
    'https://c.tenor.com/EdV_frZ4e_QAAAAC/anime-naruto.gif',
    'https://c.tenor.com/6pY8YkmSCpcAAAAS/shiki-granbell-shiki-punching.gif',
    'https://c.tenor.com/iJhyeogN3icAAAAS/rimuru-rimuru-punch.gif',
    'https://c.tenor.com/ObgxhbfdVCAAAAAS/luffy-anime.gif',
    'https://c.tenor.com/5AsLKQTjbJ4AAAAC/kasumi-love-live.gif',
    'https://c.tenor.com/o8RbiF5-9dYAAAAS/killua-hxh.gif',
    'https://c.tenor.com/b8XaMD-FD-MAAAAC/anime-punch.gif',
    'https://c.tenor.com/l_zcD2qX5M4AAAAS/double-punch-anime-double-punch.gif',
    'https://c.tenor.com/W3jh93cjuJAAAAAC/anime-girl-punch.gif',
    'https://c.tenor.com/Kbit6lroRFUAAAAC/one-punch-man-saitama.gif',
    'https://c.tenor.com/6Pzqw0wz28QAAAAC/shiki-granbell-shiki.gif',
    'https://c.tenor.com/laW-dCBdPUgAAAAS/dragon-ball-super-goku.gif',
    'https://c.tenor.com/3FCTCA89w90AAAAC/fight-girl.gif',
    'https://c.tenor.com/QYHTfQVvmWMAAAAS/playboy-bunny-bunny-girl.gif',
]

sad = [
    'https://media.giphy.com/media/TRgyI2f0hRHBS/giphy.gif',
    'https://media.giphy.com/media/kXdo4BgGoFC80/giphy.gif',
    'https://media.giphy.com/media/ujZtlj1Y7wXyE/giphy.gif',
    'https://media.giphy.com/media/shVJpcnY5MZVK/giphy.gif',
    'https://media.giphy.com/media/Xqlsn2kLPBquI/giphy.gif',
    'https://media.giphy.com/media/59d1zo8SUSaUU/giphy.gif',
    'https://media.giphy.com/media/b5z9pHJxxcREI/giphy.gif',
    'https://media.giphy.com/media/Ui7MfO6OaLz4k/giphy.gif',
    'https://media.giphy.com/media/on9LDLF5JskaQ/giphy.gif',
    'https://media.giphy.com/media/1hMJTkDXPTBiU/giphy.gif',
    'https://media.giphy.com/media/dYo5SsWTzHu8w/giphy.gif',
    'https://media.giphy.com/media/LVZURY8imFufe/giphy.gif',
    'https://media.giphy.com/media/4xKJUTzWPAVoY/giphy.gif',
    'https://media.giphy.com/media/BSxFhxneZPCvK/giphy.gif',
    'https://media.giphy.com/media/qscdhWs5o3yb6/giphy.gif',
    'https://media.giphy.com/media/ShPv5tt0EM396/giphy.gif',
    'https://media.giphy.com/media/1FG5N1IIC2C4w/giphy.gif',
    'https://media.giphy.com/media/gYMJrE0aj6UyA/giphy.gif',
    'https://media.giphy.com/media/tdn77EB27Whpe/giphy.gif',
    'https://media.giphy.com/media/HyOOyynWxMxig/giphy.gif',
]

prefix = '=c'

Id = '485801281621852175'

IdS = 485801281621852175

banip = 907837744951222322

idban = [907837744951222322]