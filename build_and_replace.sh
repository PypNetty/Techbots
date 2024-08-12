#!/bin/bash

# Définissez le nom et le tag de votre image
IMAGE_NAME="nom_de_votre_image"
TAG="latest"

# Construisez la nouvelle image
docker build -t ${IMAGE_NAME}:${TAG} .

# Vérifiez si la construction a réussi
if [ $? -eq 0 ]; then
    echo "Nouvelle image construite avec succès"
    
    # Supprimez les anciennes images non taguées (dangling images)
    docker image prune -f

    echo "Les anciennes images non utilisées ont été supprimées"
else
    echo "Échec de la construction de l'image"
    exit 1
fi

# Optionnel : Affichez les images actuelles pour vérification
docker images | grep ${IMAGE_NAME}