from discord.ext import commands
import random

class GilfoyleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gilfoyle')
    async def gilfoyle_command(self, ctx):
        responses = [
            "Ah, encore toi ? Qu'est-ce que tu veux cette fois ? Un cours magistral sur Linux ?",
            "Tu as enfin réalisé que l'open-source, c'est la seule chose qui vaille ? Bravo, on progresse.",
            "Je savais que tu finirais par revenir vers moi. Personne ne peut se passer de ma sagesse.",
            "Si c'est pour parler de Windows, passe ton chemin. Ici, on parle de choses sérieuses.",
            "Oh, une autre question sur la cybersécurité ? Laisse-moi deviner, tu as encore cliqué sur un lien suspect ?"
        ]
        response = random.choice(responses)
        await ctx.send(response)

    @commands.command(name='man')
    async def man_command(self, ctx, *, tool: str):
        await ctx.send(f"Ouvre la page de manuel pour {tool}. [Documentation Man Pages](https://man7.org/linux/man-pages/)")

    @commands.command(name='help_cmd')
    async def help_cmd(self, ctx, *, tool: str):
        await ctx.send(f"Affiche la page d'aide de la commande {tool} : `{tool} -h`.")

    @commands.command(name='apropos')
    async def apropos_command(self, ctx, *, keyword: str):
        await ctx.send(f"Recherche dans les descriptions de pages de manuel le mot-clé {keyword}.")

    @commands.command(name='cat')
    async def cat_command(self, ctx):
        await ctx.send("Concatène et affiche les fichiers. [Documentation cat](https://man7.org/linux/man-pages/man1/cat.1.html)")

    @commands.command(name='whoami')
    async def whoami_command(self, ctx):
        await ctx.send("Affiche le nom d'utilisateur actuel.")

    @commands.command(name='id')
    async def id_command(self, ctx):
        await ctx.send("Retourne l'identité de l'utilisateur.")

    @commands.command(name='hostname')
    async def hostname_command(self, ctx):
        await ctx.send("Définit ou affiche le nom de l'hôte actuel.")

    @commands.command(name='uname')
    async def uname_command(self, ctx):
        await ctx.send("Affiche le nom du système d'exploitation.")

    @commands.command(name='pwd')
    async def pwd_command(self, ctx):
        await ctx.send("Affiche le nom du répertoire de travail.")

    @commands.command(name='ifconfig')
    async def ifconfig_command(self, ctx):
        await ctx.send("Assignation ou affichage d'une adresse à une interface réseau. [Documentation ifconfig](https://man7.org/linux/man-pages/man8/ifconfig.8.html)")

    @commands.command(name='ip')
    async def ip_command(self, ctx):
        await ctx.send("Utilitaire pour montrer ou manipuler le routage, les interfaces réseau, etc. [Documentation ip](https://man7.org/linux/man-pages/man8/ip.8.html)")

    @commands.command(name='netstat')
    async def netstat_command(self, ctx):
        await ctx.send("Affiche le statut du réseau.")

    @commands.command(name='ss')
    async def ss_command(self, ctx):
        await ctx.send("Un autre utilitaire pour enquêter sur les sockets.")

    @commands.command(name='ps')
    async def ps_command(self, ctx):
        await ctx.send("Affiche le statut des processus. [Documentation ps](https://man7.org/linux/man-pages/man1/ps.1.html)")

    @commands.command(name='who')
    async def who_command(self, ctx):
        await ctx.send("Affiche les utilisateurs connectés.")

    @commands.command(name='env')
    async def env_command(self, ctx):
        await ctx.send("Affiche l'environnement ou exécute une commande.")

    @commands.command(name='lsblk')
    async def lsblk_command(self, ctx):
        await ctx.send("Liste les périphériques de bloc.")

    @commands.command(name='lsusb')
    async def lsusb_command(self, ctx):
        await ctx.send("Liste les périphériques USB.")

    @commands.command(name='lsof')
    async def lsof_command(self, ctx):
        await ctx.send("Liste les fichiers ouverts.")

    @commands.command(name='lspci')
    async def lspci_command(self, ctx):
        await ctx.send("Liste les périphériques PCI.")

    @commands.command(name='sudo')
    async def sudo_command(self, ctx):
        await ctx.send("Exécute une commande en tant qu'utilisateur différent.")

    @commands.command(name='su')
    async def su_command(self, ctx):
        await ctx.send("Change l'utilisateur avec des informations d'identification appropriées.")

    @commands.command(name='useradd')
    async def useradd_command(self, ctx):
        await ctx.send("Crée un nouvel utilisateur ou met à jour les informations de l'utilisateur.")

    @commands.command(name='userdel')
    async def userdel_command(self, ctx):
        await ctx.send("Supprime un compte utilisateur et les fichiers associés.")

    @commands.command(name='usermod')
    async def usermod_command(self, ctx):
        await ctx.send("Modifie un compte utilisateur.")

    @commands.command(name='addgroup')
    async def addgroup_command(self, ctx):
        await ctx.send("Ajoute un groupe au système.")

    @commands.command(name='delgroup')
    async def delgroup_command(self, ctx):
        await ctx.send("Supprime un groupe du système.")

    @commands.command(name='passwd')
    async def passwd_command(self, ctx):
        await ctx.send("Change le mot de passe de l'utilisateur.")

    @commands.command(name='dpkg')
    async def dpkg_command(self, ctx):
        await ctx.send("Installe, supprime et configure les paquets basés sur Debian.")

    @commands.command(name='apt')
    async def apt_command(self, ctx):
        await ctx.send("Outil de gestion de paquets de haut niveau pour Debian. [Documentation apt](https://man7.org/linux/man-pages/man8/apt.8.html)")

    @commands.command(name='aptitude')
    async def aptitude_command(self, ctx):
        await ctx.send("Une alternative à apt.")

    @commands.command(name='snap')
    async def snap_command(self, ctx):
        await ctx.send("Installe, supprime et configure les paquets snap.")

    @commands.command(name='gem')
    async def gem_command(self, ctx):
        await ctx.send("Gestionnaire de paquets standard pour Ruby.")

    @commands.command(name='pip')
    async def pip_command(self, ctx):
        await ctx.send("Gestionnaire de paquets standard pour Python. [Documentation pip](https://pip.pypa.io/en/stable/)")

    @commands.command(name='git')
    async def git_command(self, ctx):
        await ctx.send("Système de contrôle de version distribué. [Documentation git](https://git-scm.com/doc)")

    @commands.command(name='systemctl')
    async def systemctl_command(self, ctx):
        await ctx.send("Gestionnaire de services et de systemd en ligne de commande. [Documentation systemctl](https://man7.org/linux/man-pages/man1/systemctl.1.html)")

    @commands.command(name='journalctl')
    async def journalctl_command(self, ctx):
        await ctx.send("Interroge le journal de systemd.")

    @commands.command(name='kill')
    async def kill_command(self, ctx):
        await ctx.send("Envoie un signal à un processus.")

    @commands.command(name='bg')
    async def bg_command(self, ctx):
        await ctx.send("Met un processus en arrière-plan.")

    @commands.command(name='jobs')
    async def jobs_command(self, ctx):
        await ctx.send("Liste tous les processus en arrière-plan.")

    @commands.command(name='fg')
    async def fg_command(self, ctx):
        await ctx.send("Met un processus au premier plan.")

    @commands.command(name='curl')
    async def curl_command(self, ctx):
        await ctx.send("Outil en ligne de commande pour transférer des données d'un serveur ou vers un serveur. [Documentation curl](https://curl.se/docs/)")

    @commands.command(name='wget')
    async def wget_command(self, ctx):
        await ctx.send("Une alternative à curl qui télécharge des fichiers à partir d'un serveur FTP ou HTTP(s).")

    @commands.command(name='python3_http')
    async def python3_http_command(self, ctx):
        await ctx.send("Démarre un serveur web Python3 sur le port TCP 8000.")

    @commands.command(name='ls')
    async def ls_command(self, ctx):
        await ctx.send("Liste le contenu d'un répertoire.")

    @commands.command(name='cd')
    async def cd_command(self, ctx):
        await ctx.send("Change de répertoire.")

    @commands.command(name='clear')
    async def clear_command(self, ctx):
        await ctx.send("Efface le terminal.")

    @commands.command(name='touch')
    async def touch_command(self, ctx):
        await ctx.send("Crée un fichier vide.")

    @commands.command(name='mkdir')
    async def mkdir_command(self, ctx):
        await ctx.send("Crée un répertoire.")

    @commands.command(name='tree')
    async def tree_command(self, ctx):
        await ctx.send("Liste le contenu d'un répertoire de manière récursive.")

    @commands.command(name='mv')
    async def mv_command(self, ctx):
        await ctx.send("Déplace ou renomme des fichiers ou des répertoires.")

    @commands.command(name='cp')
    async def cp_command(self, ctx):
        await ctx.send("Copie des fichiers ou des répertoires.")

    @commands.command(name='nano')
    async def nano_command(self, ctx):
        await ctx.send("Éditeur de texte en ligne de commande. [Documentation nano](https://www.nano-editor.org/docs.php)")

    @commands.command(name='which')
    async def which_command(self, ctx):
        await ctx.send("Renvoie le chemin vers un fichier ou un lien.")

    @commands.command(name='find')
    async def find_command(self, ctx):
        await ctx.send("Recherche des fichiers dans une hiérarchie de répertoires.")

    @commands.command(name='updatedb')
    async def updatedb_command(self, ctx):
        await ctx.send("Met à jour la base de données locale pour les contenus existants sur le système.")

    @commands.command(name='locate')
    async def locate_command(self, ctx):
        await ctx.send("Utilise la base de données locale pour trouver des contenus sur le système.")

    @commands.command(name='more')
    async def more_command(self, ctx):
        await ctx.send("Pager utilisé pour lire la sortie standard ou des fichiers.")

    @commands.command(name='less')
    async def less_command(self, ctx):
        await ctx.send("Une alternative à more avec plus de fonctionnalités.")

    @commands.command(name='head')
    async def head_command(self, ctx):
        await ctx.send("Affiche les dix premières lignes de la sortie standard ou d'un fichier.")

    @commands.command(name='tail')
    async def tail_command(self, ctx):
        await ctx.send("Affiche les dix dernières lignes de la sortie standard ou d'un fichier.")

    @commands.command(name='sort')
    async def sort_command(self, ctx):
        await ctx.send("Trie le contenu de la sortie standard ou d'un fichier.")

    @commands.command(name='grep')
    async def grep_command(self, ctx):
        await ctx.send("Recherche des résultats spécifiques contenant des motifs donnés. [Documentation grep](https://man7.org/linux/man-pages/man1/grep.1.html)")

    @commands.command(name='cut')
    async def cut_command(self, ctx):
        await ctx.send("Supprime des sections de chaque ligne de fichiers.")

    @commands.command(name='tr')
    async def tr_command(self, ctx):
        await ctx.send("Remplace certains caractères.")

    @commands.command(name='column')
    async def column_command(self, ctx):
        await ctx.send("Formate l'entrée en plusieurs colonnes.")

    @commands.command(name='awk')
    async def awk_command(self, ctx):
        await ctx.send("Langage de balayage et de traitement de texte. [Documentation awk](https://man7.org/linux/man-pages/man1/awk.1.html)")

    @commands.command(name='sed')
    async def sed_command(self, ctx):
        await ctx.send("Éditeur de flux pour filtrer et transformer du texte. [Documentation sed](https://man7.org/linux/man-pages/man1/sed.1.html)")

    @commands.command(name='wc')
    async def wc_command(self, ctx):
        await ctx.send("Affiche le nombre de lignes, de mots et de bytes pour une entrée donnée.")

    @commands.command(name='chmod')
    async def chmod_command(self, ctx):
        await ctx.send("Change les permissions d'un fichier ou d'un répertoire.")

    @commands.command(name='chown')
    async def chown_command(self, ctx):
        await ctx.send("Change le propriétaire et le groupe d'un fichier ou d'un répertoire.")

def setup(bot):
    bot.add_cog(GilfoyleCommands(bot))
