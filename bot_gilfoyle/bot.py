from discord.ext import commands
import discord
import os
import random
from dotenv import load_dotenv
from cogs.gilfoyle import ROLE_IDS
from utils import responses

# Chargement des variables d'environnement
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
RULES_CHANNEL_ID = int(os.getenv('RULES_CHANNEL_ID'))
PRESENTATION_CHANNEL_ID = int(os.getenv('PRESENTATION_CHANNEL_ID'))  # Ajout du canal de présentation

# IDs des rôles
ROLE_IDS = {
    "etudiant": int(os.getenv('ROLE_ETUDIANT_ID')),
    "prof": int(os.getenv('ROLE_PROF_ID')),
    "prof_it": int(os.getenv('ROLE_PROF_IT_ID')),
    "guest": int(os.getenv('ROLE_GUEST_ID'))
}

def check_env_vars():
    if not TOKEN:
        raise ValueError("Le token Discord est manquant dans le fichier .env")
    if not all(value for key, value in ROLE_IDS.items()):
        raise ValueError("Certains IDs de rôle sont manquants dans le fichier .env")

check_env_vars()

intents = discord.Intents.all()  # Utilisation de tous les intents pour plus de fonctionnalités
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
@bot.event
async def on_ready():
    print(f'{bot.user.name} est prêt à mépriser l\'humanité.')
    try:
        await bot.load_extension('cogs.gilfoyle')
        print("Extension Gilfoyle chargée avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement de l'extension Gilfoyle: {e}")

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)
    rules_channel = bot.get_channel(RULES_CHANNEL_ID)
    presentation_channel = bot.get_channel(PRESENTATION_CHANNEL_ID)
    
    if welcome_channel and rules_channel and presentation_channel:
        welcome_message = (
            f"Oh, regardez qui vient d'arriver. {member.mention}, bienvenue dans notre petit coin d'enfer numérique.\n\n"
            f"Si tu penses pouvoir contribuer à quelque chose ici, va te présenter dans {presentation_channel.mention}. "
            "Dis-nous quelle formation tu prétends suivre, si tu en as une.\n\n"
            "Les modérateurs, dans leur infinie sagesse, t'attribueront un rôle quand ils auront fini leur sieste. Patience, jeune padawan de l'incompétence.\n\n"
            "Voici les rôles disponibles, si jamais tu arrives à les mériter :\n"
            "- Formateur (🟧) : Pour ceux qui pensent pouvoir enseigner quelque chose.\n"
            "- Professionnel IT (🔵) : Apparemment, certains ici savent utiliser un ordinateur.\n"
            "- Étudiant (🟢) : Les âmes perdues en quête de savoir.\n"
            "- Guest (⚪️) : Pour ceux qui sont juste là pour regarder le chaos.\n\n"
            f"Les règles du serveur sont dans {rules_channel.mention}. Essaie de les lire avant de les enfreindre, ça changera."
        )
        
        await welcome_channel.send(welcome_message)
    
    # Attribution du rôle "guest" par défaut
    default_role = discord.utils.get(member.guild.roles, id=ROLE_IDS["etudiant"])
    if default_role:
        try:
            await member.add_roles(default_role)
            print(f"Rôle {default_role.name} attribué à {member.name}")
        except discord.Forbidden:
            print(f"Erreur : Permissions insuffisantes pour attribuer le rôle à {member.name}")
        except discord.HTTPException:
            print(f"Erreur : Impossible d'attribuer le rôle à {member.name}")

@bot.command(name='manual_assign_role')
@commands.has_permissions(manage_roles=True)
async def manual_assign_role(ctx, member: discord.Member, role_name: str):
    role_name = role_name.lower()
    if role_name not in ROLE_IDS:
        await ctx.send(f"Rôle '{role_name}' non reconnu. Les rôles disponibles sont : {', '.join(ROLE_IDS.keys())}. Essaie encore, Einstein.")
        return

    role = discord.utils.get(ctx.guild.roles, id=ROLE_IDS[role_name])
    if role is None:
        await ctx.send(f"Erreur : Le rôle '{role_name}' n'existe pas sur ce serveur. Tu l'as inventé ou quoi ?")
        return

    try:
        await member.add_roles(role)
        await ctx.send(f"Rôle '{role_name}' attribué à {member.mention}. Félicitations, tu as gravi un échelon dans la hiérarchie de l'insignifiance.")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas la permission d'attribuer ce rôle. Qui a eu l'idée brillante de limiter mes pouvoirs ?")
    except discord.HTTPException:
        await ctx.send("Erreur lors de l'attribution du rôle. Le serveur Discord doit être en train de faire la sieste.")

@bot.command(name='remove_role')
@commands.has_permissions(manage_roles=True)
async def remove_role(ctx, member: discord.Member, role_name: str):
    role_name = role_name.lower()
    if role_name not in ROLE_IDS:
        await ctx.send(f"Rôle '{role_name}' non reconnu. Tu inventes des rôles maintenant ?")
        return

    role = discord.utils.get(ctx.guild.roles, id=ROLE_IDS[role_name])
    if role is None:
        await ctx.send(f"Le rôle '{role_name}' n'existe pas. Tu vis dans un monde parallèle ou quoi ?")
        return

    try:
        await member.remove_roles(role)
        await ctx.send(f"Rôle '{role_name}' retiré à {member.mention}. Retour à la case départ, comme c'était prévisible.")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas la permission de retirer ce rôle. Quelle surprise, on bride encore mes capacités.")
    except discord.HTTPException:
        await ctx.send("Erreur lors du retrait du rôle. Discord doit être en train de méditer sur son existence.")

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} a été banni. Un problème de moins à gérer, n'est-ce pas merveilleux ?")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas la permission de bannir. Quel dommage, j'aurais vraiment aimé le faire.")

@bot.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} a été expulsé. J'espère que la porte ne l'a pas frappé en sortant... ou peut-être que si, en fait.")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas la permission d'expulser. Quelle déception, j'avais déjà préparé mon pied.")

@bot.command(name='mute')
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not mute_role:
        mute_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mute_role, speak=False, send_messages=False)
    
    await member.add_roles(mute_role, reason=reason)
    await ctx.send(f"{member.mention} a été réduit au silence. Enfin, un peu de paix dans ce monde de bruits.")

@bot.command(name='unmute')
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(mute_role)
    await ctx.send(f"{member.mention} peut à nouveau parler. Préparez-vous au retour du chaos sonore.")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and not message.author.bot:
        responses = [
            "Oui, c'est moi. Que veux-tu, humain insignifiant ?",
            "Tu m'as appelé ? J'espère que c'est pour une bonne raison.",
            "Encore toi ? J'espérais avoir un moment de paix.",
            "Quoi ? Tu as besoin d'aide pour allumer ton ordinateur ?",
            "Ah, le doux son de l'incompétence qui m'appelle."
        ]
        await message.channel.send(random.choice(responses))
    
    await bot.process_commands(message)

@bot.command(name='custom_help')
async def custom_help_command(ctx):
    help_text = (
         "Voici les commandes disponibles, si tu arrives à les utiliser correctement :\n"
        "`!assign_role` - Laisse Gilfoyle déterminer ton rôle à travers un interrogatoire sarcastique.\n"
        "`!manual_assign_role <membre> <role>` - Pour les modos, attribue manuellement un rôle à un membre. Les rôles disponibles sont : "
        f"{', '.join(ROLE_IDS.keys())}.\n"
        "`!remove_role <membre> <role>` - Retire un rôle à un membre. Même liste de rôles.\n"
        "`!ban <membre> [raison]` - Banni un membre. Utilise-la avec sagesse, ou pas.\n"
        "`!kick <membre> [raison]` - Expulse un membre. Pour quand le ban est trop extrême.\n"
        "`!mute <membre> [raison]` - Réduit au silence un membre. Paix et tranquillité.\n"
        "`!unmute <membre>` - Redonne la parole à un membre. Préparez-vous au bruit.\n"
        "`!debug` - Lance une commande de débogage. Comme si ça allait vraiment aider.\n"
        "`!doc <mot-clé>` - Cherche un lien vers la documentation. Bonne chance pour la comprendre.\n"
        "`!g` - Demande à Gilfoyle une réponse sarcastique. Comme si tu en avais besoin.\n"
        "Utilise `!custom_help` pour revoir ce message, au cas où ta mémoire serait aussi fiable que Windows Vista."
    )
    await ctx.send(help_text)

@bot.command(name='doc')
async def doc_command(ctx, *, keyword: str):
    doc_link = responses.get_document_link(keyword)
    
    # Liste des messages de fin aléatoires
    end_messages = [
        "J'espère que tu sais lire.",
        "Bonne chance avec ça !",
        "Ne me dis pas que tu as déjà tout oublié.",
        "Essaie de ne pas trop te perdre dans la documentation.",
        "Si tu n'as pas trouvé ce que tu cherches, c'est peut-être une bonne chose."
    ]
    
    if doc_link:
        end_message = random.choice(end_messages)
        await ctx.send(f"Voici la documentation pour '{keyword}' : {doc_link}\n{end_message}")
    else:
        end_message = random.choice(end_messages)
        await ctx.send(f"Aucune documentation trouvée pour '{keyword}'. Soit c'est trop obscur, soit tu ne sais pas écrire. Probablement les deux.\n{end_message}")

bot.run(TOKEN)