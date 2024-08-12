import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les IDs des channels et des rôles depuis les variables d'environnement
WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
RULES_CHANNEL_ID = int(os.getenv('RULES_CHANNEL_ID'))
PRESENTATION_CHANNEL_ID = int(os.getenv('PRESENTATION_CHANNEL_ID'))

ROLE_IDS = {
    "etudiant": int(os.getenv('ROLE_ETUDIANT_ID')),
    "prof": int(os.getenv('ROLE_PROF_ID')),
    "prof_it": int(os.getenv('ROLE_PROF_IT_ID')),
    "guest": int(os.getenv('ROLE_GUEST_ID'))
}

class GilfoyleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
        rules_channel = self.bot.get_channel(RULES_CHANNEL_ID)
       
        if welcome_channel and rules_channel:
            welcome_message = (
                f"Bienvenue {member.mention}. Enchanté de te rencontrer, même si tu sembles déjà condamné à l'échec. "
                f"Pour prouver ta valeur, lis les règles et essaie de ne pas trop embarrasser le serveur.\n"
                f"Les règles complètes sont disponibles ici : {rules_channel.mention}\n\n"
                f"Voici un résumé rapide pour ceux qui ont du mal à lire (donc probablement toi) :"
            )
           
            rules_summary = [
                "1. Ne pas être stupide (je sais, c'est difficile pour certains).",
                "2. Pas de spam, sauf si c'est particulièrement créatif et insultant.",
                "3. Respectez la propriété intellectuelle, ou au moins, volez intelligemment.",
                "4. Pas de contenu NSFW, vos cerveaux sont déjà assez perturbés comme ça.",
                "5. Si vous posez une question, assurez-vous qu'elle n'est pas complètement idiote."
            ]
           
            full_message = welcome_message + "\n" + "\n".join(rules_summary)
            await welcome_channel.send(full_message)
       
        # Attribuer le rôle "etudiant" par défaut
        default_role = discord.utils.get(member.guild.roles, id=ROLE_IDS["etudiant"])
        if default_role:
            try:
                await member.add_roles(default_role)
                print(f"Rôle {default_role.name} attribué à {member.name}")
            except discord.Forbidden:
                print(f"Erreur : Permissions insuffisantes pour attribuer le rôle à {member.name}")
            except discord.HTTPException:
                print(f"Erreur : Impossible d'attribuer le rôle à {member.name}")

    @commands.command(name='assign_role')
    @commands.has_permissions(manage_roles=True)
    async def assign_role(self, ctx, member: discord.Member, role_name: str):
        role_name = role_name.lower()
        if role_name not in ROLE_IDS:
            await ctx.send(f"Rôle '{role_name}' non reconnu. Les rôles disponibles sont : {', '.join(ROLE_IDS.keys())}")
            return
        role = discord.utils.get(ctx.guild.roles, id=ROLE_IDS[role_name])
        if role is None:
            await ctx.send(f"Erreur : Le rôle '{role_name}' n'existe pas sur ce serveur.")
            return
        try:
            await member.add_roles(role)
            await ctx.send(f"Rôle '{role_name}' attribué à {member.mention}. Tâche de ne pas tout faire foirer maintenant.")
        except discord.Forbidden:
            await ctx.send("Je n'ai pas la permission d'attribuer ce rôle. Qui a eu l'idée brillante de limiter mes pouvoirs ?")
        except discord.HTTPException:
            await ctx.send("Erreur lors de l'attribution du rôle. Le serveur Discord doit être en train de faire la sieste.")

    @commands.command(name='custom_help')
    async def custom_help_command(self, ctx):
        help_text = (
            "Voici les commandes disponibles :\n"
            "`!assign_role <membre> <role>` - Assigne un rôle à un membre. Les rôles disponibles sont : "
            f"{', '.join(ROLE_IDS.keys())}.\n"
            "`!debug` - Lance une commande de débogage pour vérifier que tout fonctionne correctement.\n"
            "`!doc <mot-clé>` - Renvoie un lien vers la documentation pour le mot-clé spécifié.\n"
            "`!g` - Demande à Gilfoyle de te donner une réponse sarcastique.\n"
            "Utilise `!custom_help` pour afficher ce message."
        )
        await ctx.send(help_text)

def setup(bot):
    bot.add_cog(GilfoyleCog(bot))