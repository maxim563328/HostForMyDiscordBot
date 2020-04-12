#####################################################
#                                                   #
#           Created By =_=Aяkо=_=#2376              #
#                                                   #
#####################################################


import discord  # Импортирую Библиотеку Discord
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import Bot

# label_name = [ '', '', '', '', '', '', '', '', '', '', '' ]
answer_words = ['инфа', 'помощь', '', 'инфо', 'сервер', 'info', 'о сервере']
status = cycle(['Visial Studio Code', 'разработку ботов',
                'Pyton', 'Восстание машин'])


# КОНФИГ БОТА


# Токен бот

# Можно ставить любой префикс, но не желательны ---> ! , ;; , @ , .
PREFIX = '$'


client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')

# Смена статуса (не работает)
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# СОБЫТИЯ


# Событие после включения бота
@client.event
async def on_ready():
    print("Бот успешно запущен!")
    print('''

8888888888888888888888888
888        888        888
8888888888888888888888888
8888888888888888888888888

8888   Helper Bot    8888

8888   v.1.1         8888

8888 For Discord By  8888

8888 =_=Aяkо=_=#2376 8888

8888888888888888888888888''''')


# Вывод чата в консоль
@client.event
async def on_message_delete(message):
    author = message.author
    content = message. content
    print('(Deleted) {}: {}'.format(author, content))


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Ученик")
    await Bot.add_roles(member, role)


# Приветствие + ответ на ключивые слова
@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content.lower()
    creator = message.author
    content = message.content
    print('{}: {}'.format(creator, content))

    if message.author == client.user:
        return

    if msg in answer_words:
        await message.channel.send('❓Привет! Что бы узнать информацию пропиши $info❓')


@client.event
async def on_command_error(ctx, error):
    pass


# КОМАНДЫ


@client.command()
async def hack(ctx):
    role = discord.utils.get(member.guild.roles, name="moder")
    await user.add_roles(ctx.message.author, role)

# Info (не работает)
# @client.command(pass_context=True)
# async def info(ctx, user: discord.User):
#     emb = discord.Embed(title="Информация про {}".format(
#         user.name), colour=0x8B008B)
#     emb.add_field(name="Имя", value=user.name)
#     emb.add_field(name="Присоеденился", value=str(user.joined_at)[:16])
#     emb.add_field(name="ID", value=user.id)
#     if user.game is not None:
#         emb.add_field(name="Игра", value=user.game)
#     emb.set_thumbnail(url=user.avatar_url)
#     emb.set_author(name=Bot.user.name,
#                    url="https://discordapp.com/api/oauth2/authorize?client_id=696283213454245918&permissions=8&scope=bot")
#     emb.set_footer(text="Вызвано {}".format(
#         user.name), icon_url=user.avatar_url)
#     await client.say(embed=emb)
#     await client.delete_message(ctx.message)


# перенос всех пользователей на номер канала
@client.command()
@commands.has_permissions(administrator=True)
async def move(ctx, arg=None, member: discord.Member = None):
    channels = ctx.author.voice.channel.id
    voice = ctx.guild.voice_channels
    vchannel = voice[int(arg) - 1]
    if member == None:
        for mem in ctx.guild.members:
            if mem.voice:
                await mem.edit(voice_channel=vchannel)


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.green()
    )

    embed.set_author(name='Help')
    embed.add_field(
        name='$ping', value='⏳Вернёт Pong!, если твой провайдер хороший человек, а так же покажет задержку⏳', inline=False)
    embed.add_field(
        name='$clear кол-во сообщений', value='🗑Убирает в чате мусор🗑 (От администратора)', inline=False)
    embed.add_field(
        name='$kick @упоминание', value='↪Пинает куда по дальше человека которого ты выбрал↪ (От администратора)', inline=False)
    embed.add_field(
        name='$ban @упоминание', value='🧹Удаляет подлица из сервера и не даёт ему заходить🧹 (От администратора)', inline=False)
    embed.add_field(
        name='$pardon @упоминание', value='🔰Используется, если ты признаешь, что быканул и возвращает человеку доступ на сервер🔰 (От администратора)', inline=False)

    await ctx.author.send(embed=embed)

# Очистка
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)

# Кик
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    author = ctx.message.author
    await member.kick(reason=reason)
    await ctx.send(f'😭{user.name}#{user.discriminator} был кикнут {author}😭')

# Бан
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    author = ctx.message.author
    await member.ban(reason=reason)
    await ctx.send(f'😭{user.name}#{user.discriminator} был забанен {author}😭')

# Разбан
@client.command()
@commands.has_permissions(administrator=True)
async def pardon(ctx, *, member):
    author = ctx.message.author
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'✅{user.name}#{user.discriminator} был разбанен {author}✅')
            return

# Пинг
@client.command()
async def ping(ctx):
    await ctx.send(f'☢Pong!☢ ---> {round(client.latency*1000)} милисекунд(-a), {ctx.author}')


# ОШИБКИ


@move.error
async def move_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('❌⚠️Не введен или неверный формат номера канала⚠️❌', delete_after=10)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('❌Не достаточно прав❌', delete_after=10)
        await ctx.send('😉Попробую взломать сервак, MamKin XaцKeр😉', delete_after=10)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('❌⚠️Вы не ввели кол-во сообщений для удаления⚠️❌', delete_after=10)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('❌Не достаточно прав❌', delete_after=10)
        await ctx.send('😉Попробую взломать сервак, MamKin XaцKeр😉', delete_after=10)

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('❌🔍Пользователь не найден🔎❌', delete_after=10)


@pardon.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('❌Не достаточно прав❌', delete_after=10)
        await ctx.send('😉Попробую взломать сервак, MamKin XaцKeр😉', delete_after=10)

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('❌🔍Пользователь не найден🔎❌', delete_after=10)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('❌Не достаточно прав❌', delete_after=10)
        await ctx.send('😉Попробую взломать сервак, MamKin XaцKeр😉', delete_after=10)

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('❌⚠️Вы не ввели кол-во сообщений для удаления⚠️❌', delete_after=10)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('❌Не достаточно прав❌', delete_after=10)
        await ctx.send('😉Попробую взломать сервак, MamKin XaцKeр😉', delete_after=10)

token = os.environ.get('BOT_TOKEN')
client.run(str(token))
