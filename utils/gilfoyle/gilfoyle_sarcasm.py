import random

class GilfoyleSarcasm:
    
    @staticmethod
    def get_sarcasm():
        sarcasms = [
            "Oh, je vois que tu as encore besoin de mon cerveau. Quelle surprise.",
            "Tu as vraiment cherché cette réponse tout seul ou tu t'es dit que demander à un bot serait plus rapide ?",
            "Ah, Windows... l’équivalent informatique de la roulette russe.",
            "Tu sais, si tu passais autant de temps à apprendre Linux qu'à me poser des questions, tu serais peut-être moins incompétent.",
            "Je suppose que lire un manuel est hors de question, n'est-ce pas ?",
            "Encore une question ? Tu sais que Google existe, n’est-ce pas ?",
            "Tu es aussi utile qu'un kernel panic un lundi matin.",
            "Ne t'inquiète pas, je suis là pour compenser tes lacunes.",
            "Rappelle-moi pourquoi tu as choisi de t'occuper d'informatique ?",
            "Oh, une question basique ? C'est vraiment ton jour de chance."
        ]
        return random.choice(sarcasms)
