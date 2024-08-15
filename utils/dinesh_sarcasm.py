import random

class DineshSarcasm:
    
    @staticmethod
    def get_sarcasm():
        sarcasms = [
            "Laisse-moi deviner, tu as encore cassé ton Windows ?",
            "Ah, les utilisateurs Windows... toujours à la pointe du déni de compétence.",
            "J'espère que tu as fait un point de restauration avant de venir me voir.",
            "Tu me demandes ça, alors que tu pourrais tout simplement ne pas utiliser Windows.",
            "Ah, les joies de l'informatique... où chaque clic peut être fatal.",
            "Windows, c'est un peu comme les relations humaines : une succession d'erreurs et de bugs.",
            "Et dire qu'ils appellent ça un 'système d'exploitation'.",
            "Ah, la gestion des utilisateurs sous Windows... ça revient un peu à jouer à la roulette avec un revolver chargé.",
            "Tu sais, parfois je me demande si le vrai bug, ce n'est pas l'utilisateur.",
            "Tu pourrais presque m'impressionner, si seulement tu savais ce que tu faisais."
        ]
        return random.choice(sarcasms)
