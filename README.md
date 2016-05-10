# RocketSchool

Projet de traitement d'image dont le but est d'extraire les informations d'une capture d'écran de fin de partie pour le jeu Rocket League.

Les objectifs du projet étaient d'extraire les informations suivantes :

* L'équipe gagnante / perdante
* Le score final de la partie
* Le nom des joueurs
* Leur classement	(définit le skill)
* Leur rang			(représente approx le temps de jeu)
* Les résultats individuels des joueurs
* Enregistrer les résultats dans un fichier de type "spreadsheet" quelconque (probablement CSV)

Un objectif n'a pas été atteint, et un autre à été obtenu à l'aide d'un work-around

L'objectif qui n'a pas été atteint est l'extraction du nom des joueurs.

La raison pour cela est la simple décision de ne pas la faire à cause de la variété des caractères dont les joueurs peuvent se servir pour représenter leur surnoms en jeu. De plus, lorsque les noms sont trop long, le jeu va "tasser" les caractères pour faire apparaître l'intégralité du nom dans une zone de largeur fixe. Entraîner un OCR pour ça aurait été bien trop long et fastidieux.

Le second objectif atteint à l'aide d'un work-around est celui du score final de la partie
Plutôt que d'utiliser un OCR pour reconnaître le score final, on se sert du résultat obtenu sur le score individuel des joueurs puisque le compte des buts fait partie des statistiques.

# Comment utiliser ?
Lancer le script `main.py` avec le chemin de la capture d'écran à analyser en argument de la ligne de commande
Les captures d'écran doivent être de taille 1920x1080 et l'indicateur "winner" doit être indiqué à l'écran

Exemple : 
```
python main.py ./path/to/image.png
```

## Pourquoi ?
Parce que c'est beaucoup trop hardcore de détecter la position du scoreboard à cause de beaucoup de facteurs 
* Le dégradé de couleur change en fonction de l'équipe gagnante
* La position du scoreboard change en fonction de la résolution de la capture
* La taille du scoreboard change en fonction du nombre de joueurs dans la partie
 * Nature de la partie (1v1, 2v2, 3v3)
 * Personnes déconnectées pendant la partie n'apparaissent pas sur l'écran de fin
* Selon la capture, l'arrière plan se confond vraiment bien avec le délimiteur du scoreboard

# Dépendances
* Tesseract OCR
 * Installer Tesseract OCR 3.02.02 : https://sourceforge.net/projects/tesseract-ocr-alt/files/
 * Installer le module pytesseract : `pip install pytesseract`
* Pillow
 * `pip install pillow`
* Numpy
 * `pip install numpy`
* Open CV
 * Download on the right hand side of the page : http://opencv.org/
