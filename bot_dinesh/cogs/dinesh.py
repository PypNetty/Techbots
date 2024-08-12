from discord.ext import commands
import discord
import random

class DineshCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.windows_commands = {
            'dir': {'description': 'Lists directory contents.', 'comment': "C'est comme ls sur Linux, mais avec plus de colonnes que tu n'en liras jamais."},
            'cd': {'description': 'Changes the directory.', 'comment': "Comme sur Linux, mais avec des backslashes parce que la cohérence c'est surfait."},
            'mkdir': {'description': 'Creates a directory.', 'comment': "Pour créer des dossiers que tu oublieras d'utiliser."},
            'echo': {'description': 'Displays messages or turns command echoing on/off.', 'comment': "Parce que parfois, tu as besoin que Windows répète ce que tu dis."},
            'type': {'description': 'Displays the contents of a text file.', 'comment': "L'équivalent Windows de cat, pour quand tu veux lire des fichiers sans le confort d'un éditeur."},
            'copy': {'description': 'Copies files.', 'comment': "Comme cp sur Linux, mais avec plus de chances de se tromper de direction."},
            'move': {'description': 'Moves files.', 'comment': "Pour déplacer des fichiers et les perdre immédiatement."},
            'del': {'description': 'Deletes files.', 'comment': "Pour supprimer des fichiers et le regretter instantanément."},
            'ipconfig': {'description': 'Displays network configuration.', 'comment': "Pour voir toutes les configurations réseau que tu n'as jamais touchées."},
        }

    @commands.command(name='dinesh')
    async def windows_command_info(self, ctx, command: str = None):
        if command:
            command = command.lower()
            if command in self.windows_commands:
                info = self.windows_commands[command]
                response = f"Hey, c'est Dinesh ! `{command}`: {info['description']}\n\n{info['comment']}\nMais bon, Gilfoyle dirait probablement que c'est pour les faibles d'esprit."
            else:
                response = f"Euh, la commande `{command}` ? Je ne suis pas sûr. Peut-être que c'est une de ces nouvelles fonctionnalités de Windows que je n'ai pas encore cassées."
        else:
            responses = [
                "Bienvenue ! Je suis ici pour équilibrer les choses.",
                "Pas de sarcasme ici, juste du soutien.",
                "Si tu as besoin d'aide, n'hésite pas à demander."
            ]
            response = random.choice(responses)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(DineshCog(bot))