import discord
from discord.utils import get
from datetime import datetime

now = datetime.now()

intents=discord.Intents.default()
client = discord.Client(intents=intents)

현타통장 = 10000

@client.event
async def on_ready():
        
        game = discord.Game("현타야로 시작해서 도움말로 끝냐야 한다.")

       
        await client.change_presence(status=discord.Status.online, activity=game)
    
        print("현타봇에 로그인하였습니다!")




@client.event
async def on_message(message):
    if message.content.startswith('현타야 뭐'):
      await message.channel.send('왜')

    if message.content.startswith('현타야 하이'):
      await message.reply('ㅎ2')

    if message.content.startswith('현타야 도움말'):
      embed = discord.Embed(title="도움말", description="도움말 열람시 현타야 + (원하는 도움말)로 하시기 바랍니다.", color=0x62c1cc) 
      embed.add_field(name="기타", value="기타 도움말 열람 가능", inline=False)
      embed.add_field(name="아직없음", value="이거하면 ㅗ를 드립니다.", inline=False)
      await message.channel.send(embed=embed)

    if message.content.startswith('현타야 기타 도움말'):
      embed = discord.Embed(title="기타 도움말입니다,", description="하단참고(접두사 현타야)", color=0x62c1cc) 
      embed.add_field(name="현타야 작동언어", value="작동언어를 알려드립니다.", inline=False)
      embed.add_field(name="현타야 현재시각", value="현재시각을 알려드립니다.", inline=False)
      await message.channel.send(embed=embed)

    if message.content.startswith('현타야 아직없음'):
      await message.reply('ㅗ')
    if message.content.startswith('현타야 추가중'):
      await message.reply('ㅗ')
    if message.content.startswith('현타야 작동 언어'):
      await message.reply('파이썬으로 작동중!')
    
    if message.content.startswith('현타야 현재시각'):
      embed = discord.Embed(title="현재시각", description= "아래참고" , color=0x62c1cc) 
      embed.add_field(name= now.year, value= "년도", inline=True)
      embed.add_field(name=now.month, value= "월", inline=True)
      embed.add_field(name=now.day, value= "일", inline=True)
      embed.add_field(name=now.hour, value= "시", inline=True)
      embed.add_field(name=now.minute, value= "분", inline=True)
      embed.add_field(name=now.second, value= "초", inline=True)
      await message.channel.send(embed=embed)
   



client.run('ODEwNjk1MDYzOTgxNzg1MDk4.YCnYnQ.QC8VH7tRFtcyFEOfj_rWO1A-2eM')
    