import os
import random

# Charger les variables d'environnement
ROLE_IDS = {
    "etudiant": int(os.getenv('ROLE_ETUDIANT_ID')),
    "prof": int(os.getenv('ROLE_PROF_ID')),
    "prof_it": int(os.getenv('ROLE_PROF_IT_ID')),
    "guest": int(os.getenv('ROLE_GUEST_ID'))
}

# Messages pour différents niveaux de difficulté
end_messages_easy = [
    "J'espère que tu sais lire.",
    "Bonne chance avec ça !",
    "Essaie de ne pas trop te perdre dans la documentation."
]

end_messages_medium = [
    "Ça semble un peu plus compliqué, hein ?",
    "N'hésite pas à relire plusieurs fois.",
    "Si tu es perdu, je ne peux pas t'aider davantage."
]

end_messages_hard = [
    "Wow, c'est assez obscur, tu es sûr de ce que tu cherches ?",
    "Tu es vraiment allé chercher loin, bravo !",
    "Si tu trouves une réponse, fais-le moi savoir, ça m'intéresse."
]

def determine_difficulty(keyword: str) -> str:
    """Détermine la difficulté basée sur une liste de commandes connues."""
    command_difficulty = {
        # Réseau
        "ping": "easy",
        "traceroute": "medium",
        "netstat": "medium",
        "tcpdump": "hard",
        "wireshark": "hard",

        # Windows Server
        "ipconfig": "easy",
        "netsh": "medium",
        "powershell": "medium",
        "dism": "hard",
        "gpupdate": "hard",

        # Linux
        "ip a": "easy",
        "ls": "easy",
        "grep": "medium",
        "find": "medium",
        "awk": "hard",
        "sed": "hard",
        "EOF": "hard"
    }
    return command_difficulty.get(keyword, 'medium')  # Défaut à 'medium' si non trouvé

def get_document_link(keyword: str) -> str:
    # Implémentation de récupération du lien de documentation (exemple fictif)
    return f"https://docs.example.com/{keyword}"
