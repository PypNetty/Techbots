# Techbots

Bots Discord inspirés de Gilfoyle et Dinesh de *Silicon Valley*, développés avec Python et déployables via Docker.

## Fonctionnalités

- **Gilfoyle**: Sarcastique, gère des commandes d'admin système
- **Dinesh**: Enthousiaste, tente d'impressionner (parfois échoue)

## Technologies

Python, Bash, Docker, docker-compose

## Prérequis

- Docker
- docker-compose
- Python 3 (dev local)

## Installation rapide

1. Cloner le dépôt
2. Configurer les tokens Discord
3. Lancer `docker-compose up --build -d`

## Utilisation

- `./build_and_replace.sh` pour déployer/reconstruire
- `docker ps` pour vérifier l'exécution
- Voir les logs avec `docker-compose logs`

## Personnalisation

Modifiez les scripts Python dans `gilfoyle/` ou `dinesh/`

## Contributions

Bienvenues via pull requests ou issues

## License

MIT
