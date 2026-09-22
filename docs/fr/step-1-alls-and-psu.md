---
title: "🛠️ 1 - ALLS et PSU"
---

# 🛠️ Étape 1 : Le remplacement du PC central (ALLS)

## Explications techniques

??? note "Cliquez ici pour l'explication technique"
    L'ancien PC *RingEdge 2* ne peut pas être utilisé pour faire tourner *DX*. Vous avez besoin d'un PC **ALLS HX2**.  
    Outre un matériel plus récent et plus performant, le système d'exploitation change radicalement entre un RingEdge 2 et un ALLS HX2. **Le remplacement est obligatoire.**
    
    Il est également possible d'utiliser un **ALLS MX2**, dont les caractéristiques techniques dépassent le minimum requis pour *DX*. A priori, tous les ALLS de deuxième génération (ceux dont la référence se termine par 2) sont compatibles d'un point de vue logiciel, mais certains modèles n'ont pas les spécifications suffisantes pour faire tourner correctement le jeu. C'est par exemple le cas du ALLS X2 qui, bien que compatible, ne possède pas la puissance requise pour une expérience agréable. Il reste possible de mettre ces modèles à niveau, mais la tâche devient vite complexe et il est souvent plus simple de se procurer un modèle adapté dès le départ.

    Un ALLS ressemble beaucoup à un PC gaming moderne : son architecture ne diffère pas fondamentalement de celle d'un PC classique. En plus des composants usuels, on remarque un port USB renfoncé sur le dessus de la carte mère. Celui-ci est destiné à accueillir le "keychip", la clé USB qui sert à identifier le propriétaire de la borne sur le réseau officiel Sega et à déchiffrer les données de jeu. De plus, les modèles de deuxième génération embarquent deux cartes d'extension, qui exposent trois ports série RS-232 et une prise audio jack 2,5mm. Ces ports série sont utilisés, avec le port COM de la carte mère, pour connecter le lecteur Aime, le VFD et les dalles tactiles des deux écrans. La prise jack, quant à elle, est dédiée à l'une des deux prises casque des joueurs.

    !!! tip "L'alimentation électrique du ALLS"
        Le connecteur C13 de l'alimentation du ALLS peut être raccordé indifféremment à du 100V, 110V, 220V ou 240V : l'alimentation intègre une commutation automatique de tension. Aucun transformateur externe n'est donc nécessaire.

    !!! warning "Stockage"
        Un ALLS HX2 de *DX* officiel contient deux disques : un SSD de 120Go et un disque dur de 500Go (nommé "SUB STORAGE"). Le jeu s'attend à trouver ces deux espaces de stockage, et dans le cas de *DX*, le SSD seul ne suffit pas. Si votre ALLS n'est équipé que d'un seul disque, vous devrez vous en procurer un second et l'installer à l'intérieur. (**Note :** consultez le [Service Manual ALLS HX2](../resources/pdfs/alls-hx2-service-manual-full.pdf) pour savoir comment installer le SUB STORAGE. Il ne suffit pas de brancher le disque : une étape logicielle, détaillée dans le manuel, est également nécessaire.)

## Installation dans la borne

--8<-- "includes/wip-fr.md"

## Branchements

Voici la planche du [manuel officiel maimai DX](../resources/pdfs/maimai-dx-instruction-manual-full.pdf) (page 128) qui détaille l'ensemble de la connectique d'un ALLS HX2. Voyons chacune des connexions en détail.

!!! lightbox wide
    ![Vue arrière d'un ALLS HX2 et détail de sa connectique.](../resources/images/step-1-alls-and-psu/alls-hx2-rear-connectors-fr.jpg)

La plupart des appareils à connecter au ALLS sont présentés plus en détail dans les sections suivantes : en cas de doute sur un branchement, terminez le chapitre correspondant, puis revenez sur cette page. D'après le manuel officiel de *DX*, l'ordre des ports USB a son importance.

### PSU interne

- **Connecteur C13** : Raccordement au secteur, accepte toute tension d'entrée de 100V à 240V.

### Keychip

- **Port USB** : Réservé au keychip. Ne peut **pas** servir de port USB classique.

### Carte mère

- **COM1 - Port DB9** : Lecteur Aime
- **LAN1 - Port RJ45** : Port réseau, à connecter au routeur de service. Le second port réseau est inutilisé.
- **Audio Jacks 2,5mm** :
    - **C/W** : Prise casque Joueur 1
    - **FRONT** : Haut-parleurs Joueur 1
    - **REAR** : Haut-parleurs Joueur 2
- **USB** :
    - **USB 1** : SEGA IO4
    - **USB 2** : Hub USB, sur lequel sont branchés les deux caméras de QR codes et le hub `4x RS-232 vers USB` des deux contrôleurs de LEDs.
    - **USB 3** : Caméra des joueurs
    - **USB 4** : Port d'installation, pour y insérer une clé USB contenant les données de jeu à installer.

### Carte graphique

- **HDMI** : Raccordé à l'écran du joueur 1 via un câble HDMI - DVI-D.
- **DVI** : Raccordé à l'écran du joueur 2 via un câble DVI-D.
- **DisplayPort** : Inutilisé, duplique le signal vidéo du joueur 1.

### Cartes d'extension

- **COM2 - Port DB9** : VFD
- **COM3 - Port DB9** : Dalle tactile du joueur 1
- **COM4 - Port DB9** : Dalle tactile du joueur 2
- **SIDE** : Prise casque Joueur 2

## Alimentation

Si le branchement de la plupart des composants est assez explicite, un connecteur indispensable du RingEdge 2 n'a en revanche pas d'équivalent sur le ALLS : celui fournissant l'alimentation aux périphériques externes.

Sur le RingEdge 2, à côté du port du keychip, se trouve un connecteur Molex Mini-Fit Jr 2x7 broches femelle sortant du PC. Il sert à raccorder plusieurs éléments de la borne à l'alimentation interne du RingEdge 2, notamment l'IO3. Pour éviter d'avoir à recâbler toute cette zone, l'idéal est de fabriquer un petit adaptateur à partir d'un connecteur Molex Mini-Fit Jr identique. Pour cela, procurez-vous une alimentation de type "Mean Well" capable de fournir du 5V et du 12V. Le connecteur d'origine fournit également du 3,3V, mais aucun matériel de la zone ne l'utilise.

!!! warning "Ne réutilisez pas les alimentations de la borne"
    Ce faisceau de câbles va notamment servir à alimenter l'IO4. Si réutiliser l'alimentation 5V n'aurait que peu de conséquences, réutiliser l'alimentation 12V des LEDs serait une erreur. En effet, pour éviter le phénomène de courant de retour, l'IO4 et les LEDs doivent chacune disposer de leur propre alimentation, l'IO4 n'étant pas conçue pour supporter une telle quantité de courant.

!!! warning "Raccordez les masses"
    N'oubliez pas de relier la masse de votre nouvelle alimentation à celle des autres alimentations de la borne. Ne laissez pas l'alimentation flottante : cela peut engendrer divers problèmes inattendus. Raccordez simplement le GND de votre nouvelle alimentation à celui d'une alimentation déjà en place.

![Connecteur Molex Mini-Fit Jr 2x7 femelle, vue de face côté contacts : broches 1 à 7 en GND, 8 à 10 en +12V, 11 à 13 en +5V et 14 en +3,3V](../resources/images/step-1-alls-and-psu/molex-minifit-jr-2x7.svg)

Pour câbler le connecteur femelle, respectez le schéma ci-dessus. Il s'agit d'une vue de face du connecteur femelle, celui que vous devez câbler. Le schéma représente le côté contacts : ne le confondez pas avec le côté câbles.

- Broche 14 : **3,3V** (optionnel, inutilisé)
- Broches 13-11 : **5V**
- Broches 10-8 : **12V**
- Broches 7-1 : **GND**

Raccordez ces différents câbles aux terminaux appropriés de votre alimentation Mean Well, puis installez-la dans la borne. Fixez-la solidement avec des vis à bois : elle ne doit pas pouvoir bouger. Il ne vous reste plus qu'à brancher votre connecteur maison sur le câble d'origine.

## En résumé
!!! tldr "Les grandes lignes"
    Pour le ALLS et l'alimentation :

    * Sortir le RingEdge2
    * Installer le ALLS HX2 à sa place
    * Raccorder les différents périphériques au ALLS (voir étapes suivantes)
    * Confectionner un câble adaptateur pour la connectique d'alimentation externe
    * Installer l'alimentation externe et le câble adaptateur dans la borne, raccorder le connecteur existant

---

Passons à l'[Étape 2 : Affichage et dalles tactiles HDX](step-2-touchscreen-display.md).
