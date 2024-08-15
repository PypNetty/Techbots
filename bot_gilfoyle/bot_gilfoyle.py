import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from utils.gilfoyle_sarcasm import GilfoyleSarcasm
from utils.responses import Responses
from utils.roles import RoleManager

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN_GILFOYLE')
WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
RULES_CHANNEL_ID = int(os.getenv('RULES_CHANNEL_ID'))
PRESENTATION_CHANNEL_ID = int(os.getenv('PRESENTATION_CHANNEL_ID'))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} est prêt à mépriser l\'humanité.')
    try:
        await bot.load_extension('cogs.gilfoyle')
        print("Extension Gilfoyle chargée avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement de l'extension Gilfoyle: {e}")
    
    print("Commandes disponibles:")
    for command in bot.commands:
        print(f"- {command.name}")
    
    await bot.tree.sync()

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)
    rules_channel = bot.get_channel(RULES_CHANNEL_ID)
    presentation_channel = bot.get_channel(PRESENTATION_CHANNEL_ID)
    
    if welcome_channel and rules_channel and presentation_channel:
        welcome_message = (
            f"Oh, regardez qui vient d'arriver. {member.mention}, bienvenue dans notre petit coin d'enfer numérique.\n\n"
            f"Si tu penses pouvoir contribuer à quelque chose ici, va te présenter dans {presentation_channel.mention}. "
            f"Les règles du serveur sont dans {rules_channel.mention}. Essaie de les lire avant de les enfreindre, ça changera."
        )
        await welcome_channel.send(welcome_message)
    
    role_manager = RoleManager(bot)
    await role_manager.assign_role(member, "etudiant")

@bot.command(name='g')
async def gilfoyle_sarcasm(ctx):
    await ctx.send(GilfoyleSarcasm.get_sarcasm())

@bot.command(name='doc')
async def doc_command(ctx: commands.Context, *, keyword: str | None = None):
    if keyword is None:
        await ctx.send("Tu dois me donner un mot-clé à rechercher, génie.")
        return

    doc_link = Responses.get_document_link(keyword)
    if doc_link:
        await ctx.send(f"Voici la documentation pour '{keyword}' : {doc_link}")
    else:
        await ctx.send(f"Aucune documentation trouvée pour '{keyword}'. Soit c'est trop obscur, soit tu ne sais pas écrire. Probablement les deux.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Commande non trouvée. Utilise !help pour voir la liste des commandes disponibles.")
    else:
        print(f"Une erreur s'est produite : {error}")

bot.run(TOKEN)