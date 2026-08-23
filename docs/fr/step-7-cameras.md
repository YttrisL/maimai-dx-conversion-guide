---
title: "📷 7 - Caméras (Optionnel)"
---

# 📷 Étape 7 : Caméras (Optionnel)

--8<-- "includes/wip-fr.md"

Si vous souhaitez finaliser votre borne pour qu'elle soit parfaite, vous pouvez ajouter les caméras. Cependant, le jeu est tout à fait fonctionnel sans elles.

## 1. Caméra des joueurs (Photos in-game)

Prenez une webcam très basique et bon marché. Imprimez un support en 3D pour la fixer au sommet de la borne, sur la vitre en acrylique.

* **Branchement :** Sur l'ordinateur *ALLS* posé à plat, cette webcam doit se brancher sur le port USB situé **en bas à droite** *([Manuel](../resources/pdfs/maimai-dx-manual-full.pdf), page 128)*.
  Deux LEDs dédiées sont également à câbler sur l'IO4. Sur le connecteur CN9, en position 7 "CAMERA LED WARM" et en position 8 "CAMERA LED RED". *(Voir [manuel](../resources/pdfs/maimai-dx-manual-full.pdf), page 194)*.
* La plupart des réseaux privés ne gèrent pas la caméra, son usage se résumera donc à l'affichage en jeu.

## 2. Caméras des lecteurs de QR-Code

Dans *DX*, les joueurs peuvent scanner des cartes avec des QR codes.

* Pour que cela fonctionne, vous devez obligatoirement utiliser des webcams capables de filmer en **format UVC 640x480**.
* **L'éclairage :** Le jeu exige d'éclairer ces cartes avec des LEDs blanches (alimentées en 12V). Ces LEDs sont contrôlées par l'IO4, via les broches 55 et 56. *(Voir [manuel](../resources/pdfs/maimai-dx-manual-full.pdf), page 194)*.
* **Branchement :** Sur une véritable borne *DX*, ces caméras sont reliées à la même multiprise USB (Hub) que les lumières de la borne. Vous pouvez faire la même chose en utilisant un simple Hub USB branché sur le PC. Sur l'ordinateur *ALLS* posé à plat, le Hub doit être branché sur le port USB situé en **haut à droite** *([Manuel](../resources/pdfs/maimai-dx-manual-full.pdf), page 128)*.

!!! tip "Éclairage diffus"
    Ne braquez pas les LEDs directement sur la lentille de la caméra. Éclairez plutôt la paroi en plastique pour que la lumière rebondisse de façon diffuse sur la carte.

!!! question "Faut-il vraiment installer les caméras QR Code ?"
    C'est tout à fait optionnel. À moins que vous n'ayez accès à une autre borne très spécifique (le *Sega CardMaker*) pour imprimer vos cartes, elles ne vous serviront à rien. De plus, la plupart des réseaux privés offrent virtuellement un "DX Pass" à tous les joueurs, débloquant les fonctionnalités sans avoir besoin de scanner de cartes.

    Sachez qu'il est souvent possible lors de l'enregistrement de votre borne sur un réseau privé de demander à l'administrateur de désactiver complètement la recherche de ces caméras si vous ne souhaitez pas les installer.

---

Vous avez terminé toutes les étapes ? Direction la [conclusion](conclusion.md) !
