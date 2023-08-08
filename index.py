import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import datetime

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user}')

    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_daily_message, 'cron', day_of_week='mon-fri', hour=9, minute=30)
    scheduler.add_job(send_daily_message, 'cron', day_of_week='mon-fri', hour=13, minute=10)
    scheduler.start()

async def send_daily_message():
    guild = bot.get_guild(your_id)  #Substitua your_id pelo ID do servidor onde o bot estará operando.
    channel = discord.utils.get(guild.text_channels, name='name_channel')  #Substitua name_channel pelo nome do canal onde deseja enviar a mensagem.
    message = "@everyone Hey pessoal, vamos colocar um sorriso no rosto e ativar o reloginho das tarefas no Asana! 😄 Vamos espalhar essa energia positiva e fazer do nosso dia uma verdadeira festa produtiva! Obrigado pela colaboração! 🎉🌟"
    await channel.send(message)


bot.run('your_token') # Substitua your_token pelo token do seu bot.