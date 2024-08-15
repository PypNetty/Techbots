from discord.ext import commands
from utils.gilfoyle_sarcasm import GilfoyleSarcasm
from utils.roles import RoleManager

class GilfoyleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_manager = RoleManager(bot)

    @commands.command(name='assign_role')
    @commands.has_permissions(manage_roles=True)
    async def assign_role(self, ctx, member: commands.MemberConverter, role_name: str):
        result = await self.role_manager.assign_role(member, role_name)
        await ctx.send(result)

    @commands.command(name='remove_role')
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx, member: commands.MemberConverter, role_name: str):
        result = await self.role_manager.remove_role(member, role_name)
        await ctx.send(result)

    @commands.command(name='insult')
    async def insult(self, ctx):
        await ctx.send(GilfoyleSarcasm.get_sarcasm())

async def setup(bot):
    await bot.add_cog(GilfoyleCog(bot))