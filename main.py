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
        await message.channel.send("게임해용!")
    if message.content.startswith("공부해"):
        await message.channel.send("알겠어용")
    if message.content.startswith("사랑해"):
         await message.channel.send("감사해요!!")
    if message.content.startswith("미워"):
        await message.channel.send("힝ㅠㅠ")
    if message.content.startswith("게임해"):
        await message.channel.send("감사합니당!")
    if message.content.startswith("구매"):
        await message.channel.send("https://drive.google.com/file/d/1gyDQnpxZsnyowazH9lxrjyYrH9zuxF6p/view?usp=sharing")
    if message.content.startswith("감사합니다"):
        await message.channel.send("저도 감사해용!")
    if message.content.startswith("쭈니야"):
        await message.channel.send("무슨일이죠? 지금의 감정은 무엇인가요?(ex.짜증나,화나,기뻐,슬퍼,우울해)")
    if message.content.startswith("짜증나"):
         await message.channel.send("어몽어스를 잠깐 플래이해보는것은 어떨까요?")
    if message.content.startswith("싫어"):
        await message.channel.send("그럼 다른방법을 네이버에서 검색해보세요.")
    if message.content.startswith("좋아"):
        await message.channel.send("도움이 되었으면 좋겠네용!")
    if message.content.startswith("화나"):
        await message.channel.send("어몽어스를 잠깐 플레이해보는것은 어떨까요?")
    if message.content.startswith("기뻐"):
        await message.channel.send("신난 마음으로 어몽어스를 잠깐 플레이해보세요!")
    if message.content.startswith("슬퍼"):
        await message.channel.send("한숨 자고 일어나보세요!")
    if message.content.startswith("우울해"):
        await message.channel.send("산책을 해보세요 그럼 우울하지 않을거에용!")
    if message.content.startswith("고마워"):
        await message.channel.send("도움이 되서 기쁘네용!")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
