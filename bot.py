import discord
from funciones_bot import gen_pasword, gen_historia


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hi!")
    elif message.content.startswith("$bye"):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("Hola"):
        await message.channel.send("Hola, buenas")
    elif message.content.startswith("Hola"):
        await message.channel.send("Gracias")
    elif message.content.startswith("Denada"):
        await message.channel.send(gen_pasword(10))
    elif message.content.startswith("Cuéntame una historia"):
        await message.channel.send(gen_historia())
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
