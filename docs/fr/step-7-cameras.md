---
title: "📷 7 - Caméras (Optionnel)"
---

# 📷 Étape 7 : Caméras (Optionnel)

À ce stade, une seule fonctionnalité sépare encore votre conversion d'une véritable *DX* : **les caméras**. Le jeu s'en sert très peu, et elles sont largement considérées comme optionnelles. Mais si vous voulez vous rapprocher au maximum d'une vraie *DX*, elles sont heureusement assez simples à installer.

## Explications techniques

??? note "Cliquez ici pour l'explication technique"
    Une véritable *DX* compte **trois caméras** : une pointée vers les joueurs, et deux qui servent de lecteurs de QR-Code pour les *DX Pass*.

    - **La caméra des joueurs** : une simple caméra USB UVC, en 1280x960 avec un HFOV de 95°. [[référence]]({{SHIKINO_PLAYER_CAMERA_REFERENCE}})
    - **Les caméras des lecteurs de QR-Code** : deux caméras USB UVC, en 640x480 avec un FOV de 50°.

    !!! info "Les DX Pass"
        Les DX Pass sont des cartes physiques que les joueurs font imprimer sur la borne "Sega CardMaker". Cette borne est rare hors du Japon, et plus encore en état d'imprimer. De plus, les DX Pass sont aujourd'hui associés automatiquement au compte du joueur : la carte physique n'est plus nécessaire. **Les lecteurs de QR-Code sont donc largement optionnels**, voire inutiles.

        Certains événements en jeu ne se déclenchent qu'en scannant des cartes spécifiques, mais la plupart des serveurs privés les débloquent par défaut.

    **Pour la caméra des joueurs, n'importe quelle caméra USB UVC fait l'affaire**, même une webcam bon marché. Le jeu s'en sert uniquement pour afficher une photo des joueurs à la fin de chaque musique, une option que la plupart des joueurs désactivent pour gagner du temps.

    **Pour les lecteurs de QR-Code, le jeu est bien plus exigeant** : il faut obligatoirement des caméras USB UVC capables de filmer en 640x480, avec un FOV précis, sans quoi les QR-Codes ne sont pas reconnus.

    Dans les deux cas, le jeu prévoit **un éclairage dédié pour chaque caméra**, piloté par l'IO4. Il n'est pas indispensable de le raccorder, mais sans éclairage adapté, les lecteurs de QR-Code risquent de très mal fonctionner. Pour la caméra des joueurs, l'éclairage devient nécessaire si votre borne est dans une salle sombre. Le jeu pilote aussi une LED rouge, qui prévient les joueurs que la caméra filme.

    Les caméras se branchent en USB sur le ALLS : la caméra des joueurs directement sur la carte mère, les deux caméras des lecteurs de QR-Code sur le hub USB qui accueille déjà l'adaptateur RS-232 vers USB des contrôleurs de LEDs (voir l'[étape 6](step-6-lighting.md)).

## Caméra des joueurs (Photos in-game)

Chaque modèle de caméra est différent, il est donc difficile de proposer un support universel. Le mieux est de **concevoir un support imprimable en 3D** à installer au sommet de la borne, en profitant des vis existantes de la vitre en acrylique.

* **Installation sur la borne :** Impression 3D.
* **Branchement au ALLS :** En USB, sur le port **n°3**.
* **Branchement à l'IO4 :**
    - **CAMERA LED WARM : CN9 - Broche 7** : cathode de l'anneau de LEDs blanches qui éclaire la zone filmée.
    - **CAMERA LED RED : CN9 - Broche 8** : cathode de la LED rouge qui indique aux joueurs que la caméra filme.

Si vous avez fabriqué votre propre nappe de câbles et suivi la suggestion de l'[étape 6](step-6-lighting.md), vous avez déjà un connecteur prêt pour l'IO4. Avec la PCB de conversion, deux connecteurs dédiés sont disponibles pour ces LEDs.

!!! lightbox
    ![Schéma du ALLS : port USB n°3 utilisé pour la caméra des joueurs, mis en évidence par la flèche rouge](../resources/images/step-7-cameras/alls-hx2-rear-connectors-emphasis-on-usb-no3.jpg)
    ![PCB de conversion [maiConvert-IO4]({{IO4_CONVERSION_PCB}}) : repérage des connecteurs J29 (`CAMERA LED RED`) et J30 (`CAMERA LED WARM`)](../resources/images/step-7-cameras/camera-led-on-convertion-pcb.jpg)

## Caméras des lecteurs de QR-Code

L'idéal est de vous procurer **deux petits modules de 30mm x 25mm** : ils s'adaptent au [modèle 3D conçu par SpiralGlide](spiralglide-resources.md#support-du-lecteur-de-qr-code-dx-pass-reader), qui se fixe grâce aux vis existantes de la vitre en acrylique.

* **Installation sur la borne :** [Impression 3D](spiralglide-resources.md#support-du-lecteur-de-qr-code-dx-pass-reader).
* **Branchement au ALLS :** En USB, via le hub USB branché sur le port **n°2**. N'importe quel port du hub convient.
* **Branchement à l'IO4 :**
    - **1P CODE READER LED : CN3 - Broche 55** : cathode commune (R, G et B) de la bande de LEDs qui éclaire le lecteur du joueur 1.
    - **2P CODE READER LED : CN3 - Broche 56** : cathode commune (R, G et B) de la bande de LEDs qui éclaire le lecteur du joueur 2.

Si vous avez suivi la suggestion de l'[étape 6](step-6-lighting.md), vous avez déjà un connecteur prêt pour ces deux signaux. Ils sont aussi disponibles sur la PCB de conversion.

**Pour que le jeu identifie les caméras, chacune doit filmer un QR-Code précis** : *SDEZ01* côté joueur 1, *SDEZ02* côté joueur 2. Le modèle 3D de SpiralGlide comporte une encoche à la bonne taille pour ces codes. Imprimez [ce PDF](../resources/images/step-7-cameras/codes-for-qr-code-readers.pdf) en A4, sur une imprimante correctement calibrée, pour obtenir des QR-Codes à la bonne taille, puis collez-les à leur emplacement.

Si vous avez choisi les caméras de la [liste de courses](equipment.md), leur lentille est réglable : vous pouvez ajuster la mise au point.

!!! tip "Les LEDs des lecteurs de QR-Code"
    *DX* utilise d'origine une bande de LEDs RGB, mais ses trois couleurs partagent une seule cathode pilotée par l'IO4 : elles s'allument donc toujours ensemble, à (presque) la même intensité. **Une bande de LEDs blanc chaud donnera le même résultat.**

    **Ne braquez pas les LEDs directement vers la lentille de la caméra.** Éclairez plutôt la paroi en plastique, pour que la lumière se diffuse sur la carte. Un éclairage de face crée un reflet qui éblouit la caméra et empêche la lecture du QR-Code.

!!! tip "Installation des modules de caméra"
    **Le jeu est très exigeant sur l'orientation des caméras** : si l'angle n'est pas le bon, il ne lira pas le QR-Code des cartes. Attention aussi : un QR-Code par défaut bien lu ne garantit pas que les cartes le seront, faites des essais. Pour ajuster la hauteur et l'inclinaison d'un module, vous pouvez par exemple ajouter des écrous sur ses vis. Ce n'est pas idéal, mais ça fonctionne.

    Testez la détection dans le menu Test du jeu. Malheureusement, rien ne remplace les essais successifs pour cette étape.

!!! lightbox
    ![Schéma du ALLS : port USB n°2 utilisé pour le hub des caméras des lecteurs de QR-Code, mis en évidence par la flèche rouge](../resources/images/step-7-cameras/alls-hx2-rear-connectors-emphasis-on-usb-no2.jpg)
    ![PCB de conversion [maiConvert-IO4]({{IO4_CONVERSION_PCB}}) : repérage des connecteurs J25 (`1P CODE READER LED`) et J26 (`2P CODE READER LED`)](../resources/images/step-7-cameras/code-reader-led-on-convertion-pcb.jpg)
    ![Écrous utilisés comme entretoises sur les vis du modèle 3D imprimé, afin d'ajuster la hauteur et l'angle des modules de caméra au-dessus des QR-Codes](../resources/images/step-7-cameras/screw-nuts-used-as-spacers-to-orient-cameras.jpg)

## Validation de l'installation

Le menu Test du jeu propose une page dédiée aux caméras. Le jeu y cherche **trois flux vidéo**, dont deux doivent filmer les QR-Codes par défaut [SDEZ01](../resources/images/step-7-cameras/SDEZ01.svg) et [SDEZ02](../resources/images/step-7-cameras/SDEZ02.svg). Ces deux caméras sont reconnues automatiquement grâce à leur QR-Code, et la caméra restante est attribuée aux joueurs.

**Si les trois caméras sont reconnues dans le bon ordre, félicitations, l'installation est terminée !**

---

Vous avez terminé toutes les étapes ? Direction la [conclusion](conclusion.md) !
