import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("쭈니봇")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("HI")
    if message.content.startswith("뭐해"):
        await message.channel.send("게임해")
        if message.content.startswith("공부"):
            await message.channel.send("알겠어용")




client.run("")
