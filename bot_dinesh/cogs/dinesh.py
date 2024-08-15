from discord.ext import commands
from utils.dinesh_sarcasm import DineshSarcasm

class DineshCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='windows_help')
    async def windows_help(self, ctx, *, command: str):
        await ctx.send(f"Voici comment utiliser la commande Windows '{command}': `{command} /?`")

    @commands.command(name='compliment')
    async def compliment(self, ctx):
        await ctx.send(DineshSarcasm.get_sarcasm())

async def setup(bot):
    await bot.add_cog(DineshCog(bot))