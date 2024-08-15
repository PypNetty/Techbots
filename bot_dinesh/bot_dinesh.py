import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from utils.dinesh_sarcasm import DineshSarcasm
from utils.responses import Responses

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN_DINESH')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} est connecté et prêt à fonctionner !')
    await bot.change_presence(activity=discord.Game(name="Donner des conseils IT"))
    
    try:
        await bot.load_extension('cogs.dinesh')
        print("DineshCog chargé")
    except Exception as e:
        print(f"Erreur lors du chargement de DineshCog: {e}")
    
    print("Commandes disponibles:")
    for command in bot.commands:
        print(f"- {command.name}")
    
    await bot.tree.sync()

@bot.command(name='d')
async def dinesh_sarcasm(ctx):
    await ctx.send(DineshSarcasm.get_sarcasm())

@bot.command(name='windows_doc')
async def windows_doc_command(ctx: commands.Context, *, keyword: str | None = None):
    if keyword is None:
        await ctx.send("Tu dois spécifier une commande Windows pour obtenir sa documentation.")
        return

    doc_link = Responses.get_windows_document_link(keyword)
    if doc_link:
        await ctx.send(f"Voici la documentation Windows pour '{keyword}' : {doc_link}")
    else:
        await ctx.send(f"Aucune documentation Windows trouvée pour '{keyword}'. Es-tu sûr que c'est une vraie commande Windows ?")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Commande non trouvée. Utilise !help pour voir la liste des commandes disponibles.")
    else:
        print(f"Une erreur s'est produite : {error}")

bot.run(TOKEN)