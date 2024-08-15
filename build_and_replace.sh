#!/bin/bash

set -e

# Fonction pour forcer la suppression d'une image Docker
force_delete_image() {
    local IMAGE_ID=$1
    local CONTAINERS=$(docker ps -a --filter "ancestor=$IMAGE_ID" -q)

    if [ -n "$CONTAINERS" ]; then
        echo "Arrêt et suppression des conteneurs utilisant l'image $IMAGE_ID..."
        docker stop $CONTAINERS
        docker rm $CONTAINERS
    fi

    echo "Suppression de l'image $IMAGE_ID..."
    docker rmi $IMAGE_ID
}

# Fonction pour construire et nettoyer une image Docker
build_and_clean_image() {
    local SERVICE_NAME=$1
    local CONTEXT=$2
    local DOCKERFILE=$3

    echo "Vérification de l'image pour le service '${SERVICE_NAME}'..."
    local NEW_HASH=$(md5sum ${DOCKERFILE} | awk '{ print $1 }')
    local EXISTING_HASH=$(docker-compose images -q ${SERVICE_NAME} | xargs -I {} docker inspect {} --format='{{index .Config.Labels "dockerfile_hash"}}' 2>/dev/null || echo "")

    if [ "$NEW_HASH" != "$EXISTING_HASH" ]; then
        echo "Modifications détectées. Reconstruction de l'image pour '${SERVICE_NAME}'..."
        docker-compose build --build-arg DOCKERFILE_HASH=$NEW_HASH ${SERVICE_NAME}
        echo "Nouvelle image pour '${SERVICE_NAME}' construite avec succès"
        
        # Nettoyer les anciennes images non taguées
        docker image prune -f
    else
        echo "Aucune modification détectée pour '${SERVICE_NAME}'. Utilisation de l'image existante."
    fi
}

# Fonction pour nettoyer les ressources Docker inutilisées
cleanup() {
    echo "Nettoyage des ressources Docker inutilisées..."
    docker container prune -f
    docker image prune -f
    docker network prune -f
    docker volume prune -f
}

# Fonction pour vérifier et démarrer les conteneurs
start_containers() {
    echo "Démarrage des conteneurs..."
    docker-compose up -d
    echo "Conteneurs démarrés."
}

# Fonction pour vérifier les logs des conteneurs
check_logs() {
    echo "Vérification des logs des conteneurs..."
    docker-compose logs --tail=20
}

# Fonction pour afficher l'utilisation du système Docker
show_docker_usage() {
    echo "Utilisation du système Docker :"
    docker system df
}

# Processus principal
main() {
    echo "Début du processus de déploiement et maintenance..."

    # Lire les noms des services depuis docker-compose.yml
    local SERVICES=$(docker-compose config --services)

    # Construire ou mettre à jour les images pour chaque service
    for SERVICE in $SERVICES; do
        build_and_clean_image "$SERVICE" "." "Dockerfile"
    done

    # Nettoyage
    cleanup

    # Démarrer les conteneurs
    start_containers

    # Vérifier les logs
    check_logs

    # Afficher l'utilisation du système Docker
    show_docker_usage

    echo "Processus terminé. Les services sont déployés et en cours d'exécution."
}

# Exécution du processus principal
main

# Afficher les conteneurs en cours d'exécution
echo "Conteneurs en cours d'exécution :"
docker ps
