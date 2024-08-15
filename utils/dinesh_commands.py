from discord.ext import commands

class DineshCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_cmd')
    async def help_cmd(self, ctx, *, tool: str):
        await ctx.send(f"Affiche la page d'aide de la commande {tool} : `{tool} /?`.")

    @commands.command(name='getmac')
    async def getmac_command(self, ctx):
        await ctx.send("Affiche l'adresse MAC de l'ordinateur.")

    @commands.command(name='hostname')
    async def hostname_command(self, ctx):
        await ctx.send("Affiche ou définit le nom d'hôte de l'ordinateur.")

    @commands.command(name='ipconfig')
    async def ipconfig_command(self, ctx):
        await ctx.send("Affiche la configuration IP de l'ordinateur. [Documentation ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig)")

    @commands.command(name='tasklist')
    async def tasklist_command(self, ctx):
        await ctx.send("Affiche une liste de tâches en cours d'exécution.")

    @commands.command(name='taskkill')
    async def taskkill_command(self, ctx):
        await ctx.send("Met fin à une ou plusieurs tâches en fonction du PID ou du nom d'image. [Documentation taskkill](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/taskkill)")

    @commands.command(name='whoami')
    async def whoami_command(self, ctx):
        await ctx.send("Affiche le nom d'utilisateur actuel.")

    @commands.command(name='systeminfo')
    async def systeminfo_command(self, ctx):
        await ctx.send("Affiche les informations sur le système. [Documentation systeminfo](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/systeminfo)")

    @commands.command(name='netstat')
    async def netstat_command(self, ctx):
        await ctx.send("Affiche les connexions réseau et les ports ouverts.")

    @commands.command(name='ping')
    async def ping_command(self, ctx, *, address: str):
        await ctx.send(f"Vérifie la connectivité réseau vers {address}. [Documentation ping](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ping)")

    @commands.command(name='tracert')
    async def tracert_command(self, ctx, *, address: str):
        await ctx.send(f"Affiche l'itinéraire vers {address}. [Documentation tracert](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tracert)")

    @commands.command(name='net')
    async def net_command(self, ctx):
        await ctx.send("Utilitaire pour la gestion des services réseau.")

    @commands.command(name='shutdown')
    async def shutdown_command(self, ctx):
        await ctx.send("Arrête ou redémarre l'ordinateur.")

    @commands.command(name='sfc')
    async def sfc_command(self, ctx):
        await ctx.send("Analyse et restaure les fichiers système corrompus. [Documentation sfc](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sfc)")

    @commands.command(name='chkdsk')
    async def chkdsk_command(self, ctx):
        await ctx.send("Vérifie et répare les erreurs de disque. [Documentation chkdsk](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk)")

    @commands.command(name='format')
    async def format_command(self, ctx):
        await ctx.send("Formate un disque pour être utilisé avec Windows.")

    @commands.command(name='robocopy')
    async def robocopy_command(self, ctx):
        await ctx.send("Copie de fichiers et de répertoires. [Documentation robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)")

    @commands.command(name='powershell')
    async def powershell_command(self, ctx):
        await ctx.send("Ouvre l'environnement PowerShell pour exécuter des scripts et des commandes spécifiques à Windows.")

    @commands.command(name='wmic')
    async def wmic_command(self, ctx):
        await ctx.send("Interface en ligne de commande pour les tâches d'administration Windows. [Documentation wmic](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wmic)")

    @commands.command(name='netsh')
    async def netsh_command(self, ctx):
        await ctx.send("Utilitaire de configuration réseau avancé. [Documentation netsh](https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh)")

    @commands.command(name='schtasks')
    async def schtasks_command(self, ctx):
        await ctx.send("Planifie des tâches sur l'ordinateur. [Documentation schtasks](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks)")

    @commands.command(name='regedit')
    async def regedit_command(self, ctx):
        await ctx.send("Ouvre l'éditeur de registre Windows.")

    @commands.command(name='gpupdate')
    async def gpupdate_command(self, ctx):
        await ctx.send("Mets à jour les paramètres de stratégie de groupe. [Documentation gpupdate](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpupdate)")

    @commands.command(name='gpresult')
    async def gpresult_command(self, ctx):
        await ctx.send("Affiche les informations de stratégie de groupe pour un utilisateur ou un ordinateur. [Documentation gpresult](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult)")

    @commands.command(name='cls')
    async def cls_command(self, ctx):
        await ctx.send("Efface l'affichage de l'écran du terminal.")

def setup(bot):
    bot.add_cog(DineshCommands(bot))
