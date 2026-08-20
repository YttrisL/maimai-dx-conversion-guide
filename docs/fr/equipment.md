---
title: "🛒 Liste de courses"
---

# 🛒 Liste de courses : Le matériel nécessaire

## Préambule

La plupart des composants requis ne se trouveront pas dans un supermarché. Il s'agit de matériel d'arcade précis et pointu, que seuls vendent les fabricants officiels. Il sera bien sûr totalement impossible pour nous de passer par le service après-vente de Sega pour récupérer le matériel dont nous avons besoin, nous ne pouvons donc que nous tourner vers le marché de l'occasion.

De ce fait, __nous sommes tributaires de la disponibilité des articles sur ces marchés de l'occasion__. S'il n'est, par exemple, pas très compliqué de trouver une carte I/O IO4 ou un lecteur Aime, il est beaucoup plus compliqué de trouver un ALLS HX2 et pour ainsi dire impossible de trouver une dalle tactile officielle provenant d'une borne maimai DX. Pour certaines de ces pièces, des alternatives existent, pour d'autres il n'y aura pas d'autre choix que de prendre son mal en patience et de rester à l’affût d'une offre sur le marché de l'occasion japonais.

!!! tip ""
    La plupart des pièces détachées sur le marché de l'occasion japonais proviennent de bornes qui ont été démantelées pour être liquidées plus facilement. Le plus souvent suite à une fin d'activité du game-center l'ayant possédée, ou parce que la borne en question n'attire plus le public. Dans le cas de maimai DX, le jeu étant très populaire il est rare qu'une borne soit vendue à l'exportation, et encore plus qu'une d'entre elles soit démontée pour être vendue en pièces détachées. 
    
    Heureusement, la plupart des composants des bornes Sega sont interchangeables et réutilisés d'une borne à l'autre, y compris dans des machines beaucoup moins populaires que maimai DX pour lesquelles il est infiniment plus probable de trouver des pièces détachées.

Pour chacune de ces pièces, le tableau priorise l'option la plus optimisée. Cela peut être pour plusieurs raisons : simplicité d'installation, prix, disponibilité. Lorsqu'il en existe, le tableau mentionnera les alternatives disponibles. Toutefois, ce guide part du principe que vous avez choisi l'option principale et ne s'attardera pas sur les alternatives.

## Matériel obligatoire

### ALLS HX2
* Où : JDirectItems Auction 
* Info : En fonction des périodes il peut être assez difficile à trouver. C'est le système utilisé par maimai DX et peu d'autres bornes l'utilisent.

*Alternative* : **ALLS MX2**

* Où : JDirectItems Auction 
* Info : Celui-ci est moins rare et apparaît plus souvent, toutefois il nécessitera un downgrade pour être rendu compatible avec maimai DX. L'opération n'est pas documentée publiquement.

---

### Carte I/O Sega IO4
* Où : JDirectItems Auction 
* Info : Simple à trouver, utilisée universellement dans toutes les bornes Sega depuis plusieurs années. À ne pas confondre avec une IO3, elles se ressemblent. Le meilleur moyen de reconnaître une IO4 est de vérifier si elle a bien ses dip switches sur le dessus de la PCB.

---

### Lecteur Aime (Gen. 3)
* Où : JDirectItems Auction
* Info : Il faut impérativement un lecteur de génération 3. Il vient souvent avec le VFD intégré. On peut les reconnaître au logo Aime qui diffère de celui de la génération précédente. Ils ne sont pas très rares et on en trouve souvent venant d'une borne Star Horse 4.

---

### Dalle tactile HDX (x2)
* Où : [Sur le discord HanDevice](https://discord.gg/xABCFMWmTK)
* Info : Il s'agit d'une dalle tactile créée par un particulier, dans le but de fournir un « pad », une sorte de manette personnalisée permettant de jouer au jeu hors d'une borne, dans le confort de son domicile. Officiellement ils ne vendent pas de kit de conversion directement, mais il est possible de [contacter le fabricant via son discord](https://discord.com/channels/1336383976721616897/1393421596190048266/1393822351094841375) pour lui demander une offre portant uniquement sur la dalle tactile **et** la HanDevice IO (sa carte I/O dédiée) qui va avec. Cette carte I/O a l'avantage d'exposer un port série UART que nous pouvons exploiter pour la connecter directement au ALLS HX2 sans avoir besoin de transformer le signal.

*Alternative* : **Kit de conversion Yuancon — à base d'une dalle ADX (x2)**

* Où : [Sur le site de yuancon](https://yuancon.store/controller/UPDATEKIT)
* Info : Yuancon propose des kits de conversion incluant la dalle tactile et huit boutons, un kit permettant de convertir un côté de la borne. Ils sont équivalents aux HDX à ceci près que leur carte I/O n'inclut pas de port série. Elle communique uniquement en USB-CDC avec le PC, ce qui rend sa connexion à un ALLS HX2 difficile puisque ce signal ne peut pas être adapté directement via un simple convertisseur RS-232. C'est toutefois toujours possible [via un logiciel faisant office de proxy](https://gitea.farewell.dev/Yttris/maitouch_rs) en tournant sur un Raspberry Pi installé entre le ALLS et l'ADX, mais cela introduit une complexité que nous ne détaillerons pas dans ce guide. (Si vous décidez de partir sur cette option, vous n'avez pas besoin des boutons supplémentaires du point suivant.)

---

### Boutons HDX (x16)
* Où : [Sur le discord HanDevice](https://discord.gg/xABCFMWmTK)
* Info : Les boutons de jeu pour l'anneau. Les boutons de FiNALE sont techniquement compatibles, mais le ressenti est totalement différent (et bien meilleur) sur DX. Il vaut donc largement la peine de mettre les boutons à jour. Il faut huit boutons par joueur, soit seize au total, mais il peut être utile d'en acheter quelques-uns en réserve à l'avance. C'est une pièce d'usure.

*Alternative* : **Boutons "Rabbit" (x16)** 

* Où : [Sur le site de yuancon](https://yuancon.store/controller/UPDATEKIT)
* Info : **En cours d'écriture**

!!! warning "N'achetez pas les contrefaçons!"
    Il existe effectivement des boutons beaucoup moins chers qui sont en apparence très similaires, trouvables sur Taobao ou AliExpress. Ne succombez pas à la tentation d'économiser quelques euros, c'est le pire achat que vous puissiez faire. Ils sont de **très** mauvaise qualité, présentent une liste sans fin de problèmes et une durabilité minime. Préférez des boutons de qualité venant d'un vendeur fiable.

---

### Boutons triangle
**En cours d'écriture**

## Petites fournitures

| Nom | Où le trouver | Commentaire |
| --- | --- | --- |
| Un câble DisplayPort (ou DisplayPort vers DVI) pour les écrans | | |
| Un câble DVI-D pour les écrans | | |
| Deux petits amplificateurs audio pour gérer les prises casques | | |

## Pour le Proxy ("Traduction" des données)

| Nom | Où le trouver | Commentaire |
| --- | --- | --- |
| Deux Raspberry Pi 5 avec leur bloc d'alimentation | | |
| Deux adaptateurs "USB-to-Serial" avec puces FTDI (prévoyez-en 6 si vous gérez le tactile **et** les LEDs via proxy) | | |
| Deux adaptateurs "Null Modem" pour faire correspondre les fiches mâle-femelle des adaptateurs "USB-to-Serial" à la connectique du ALLS | | |

## Matériel Optionnel (Son, Caméras, Finitions)

| Nom | Où le trouver | Commentaire |
| --- | --- | --- |
| Une webcam classique et bon marché pour la caméra du joueur | | |
| Deux webcams au format strict UVC 640x480 pour les lecteurs de QR-Code | | |
| Un Hub USB (de préférence avec sa propre alimentation) | | |

Assurez-vous d'avoir reçu et testé tout le matériel que vous aurez commandé avant de vous lancer dans la conversion à proprement parler.

---

Maintenant que vous disposez du matériel, commençons par l'[Étape 1 : Le Remplacement du PC Central (ALLS)](step-1-alls-and-psu.md).
