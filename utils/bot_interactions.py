from discord.ext import commands

class BotInteractions(commands.Cog):
    def __init__(self, bot, other_bot):
        self.bot = bot
        self.other_bot = other_bot

    @commands.command(name='question_gilfoyle')
    async def question_gilfoyle(self, ctx):
        await ctx.send("Je ne connais pas la réponse. Demande à Gilfoyle, il doit savoir.")

    @commands.command(name='question_dinesh')
    async def question_dinesh(self, ctx):
        await ctx.send("Ça dépasse mes compétences. Demande à Dinesh, c'est son domaine.")
