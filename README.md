# LocalAIOllama

Ce projet permet de télécharger un fichier PDF depuis Dropbox, d'extraire son contenu et de poser des questions à un modèle Llama basé sur le texte extrait.

## Prérequis

Avant de commencer, assure-toi d'avoir les éléments suivants :

- Python 3.8+ installé.
- Un compte Dropbox et un token d'accès (voir `dropbox_config.py`).
- Un environnement virtuel Python configuré.

## Installation

1. Clone le projet :
   ```bash
   git clone https://github.com/AbrahamLawson/LocalAIOllama.git
Accède au répertoire du projet :

bash
Copier le code
cd LocalAIOllama
Crée et active un environnement virtuel :

bash
Copier le code
python3 -m venv venv
source venv/bin/activate  # Sur Windows, utilise `venv\Scripts\activate`
Installe les dépendances nécessaires :

bash
Copier le code
pip install -r requirements.txt
Configuration
Crée un fichier dropbox_config.py et ajoute ton token d'accès Dropbox :

python
Copier le code
DROPBOX_ACCESS_TOKEN = "votre_token_dropbox"
Si tu utilises Ollama, assure-toi que le modèle est disponible et configuré sur ton environnement local.

Lancer l'application
Lance le serveur Flask avec cette commande :

bash
Copier le code
python app.py
L'application sera accessible à l'adresse http://127.0.0.1:5000/.

Utilisation
Pour poser une question au modèle Llama :

Envoie une requête POST à http://127.0.0.1:5000/ask avec un JSON contenant :

file_path : Le chemin du fichier PDF sur Dropbox.
question : La question à poser au modèle.
Exemple de requête :

json
Copier le code
{
  "file_path": "/chemin/vers/le/fichier.pdf",
  "question": "Quel est le sujet principal de ce document ?"
}
La réponse sera retournée sous forme de JSON, contenant la réponse du modèle.
