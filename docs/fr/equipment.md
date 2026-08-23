---
title: "🛒 Liste de courses"
---

# 🛒 Liste de courses : Le matériel nécessaire

## Préambule
Pour chacune des pièces listées dans la liste de courses, le tableau priorise l'option la plus optimisée. Cela peut être pour plusieurs raisons : simplicité d'installation, prix, disponibilité. *Lorsqu'il en existe, le tableau mentionnera les alternatives disponibles.* Toutefois, ce guide part du principe que vous avez choisi l'option principale et ne s'attardera pas sur les alternatives.

!!! info "Le marché de l'occasion japonais"
    Si vous n'êtes pas familier avec le marché de seconde main japonais et les options disponibles pour vous y procurer du matériel, n'hésitez pas à consulter l'annexe [Le marché de l'occasion japonais](secondhand-market.md).
## Matériel obligatoire

<div class="equipment-card" markdown>

### ALLS HX2
* Où : JDirectItems Auction 
* Info : En fonction des périodes, il peut être assez difficile à trouver. C'est le système utilisé par maimai DX et peu d'autres bornes l'utilisent.

*Alternative* : **ALLS MX2**

* Où : JDirectItems Auction 
* Info : Celui-ci est moins rare et apparaît plus souvent, toutefois, il nécessitera un downgrade pour être rendu compatible avec maimai DX. L'opération n'est pas documentée publiquement.

!!! info "Espace de stockage"
    En fonction du jeu que faisait tourner nativement votre ALLS, il est possible que celui-ci ne contienne qu'un SSD de 64 Go.
    Si c'est le cas, ce ne sera pas suffisant pour installer le jeu. Vous devrez alors vous procurer un SSD de minimum 128 Go, mais idéalement 256 Go.

</div>

<div class="equipment-card" markdown>

### Carte I/O Sega IO4
* Où : JDirectItems Auction 
* Info : Simple à trouver, utilisée universellement dans toutes les bornes Sega depuis plusieurs années. À ne pas confondre avec une IO3, elles se ressemblent. Le meilleur moyen de reconnaître une IO4 est de vérifier si elle a bien ses dip switches sur le dessus de la PCB.

</div>

<div class="equipment-card" markdown>

### Lecteur Aime (Gen. 3)
* Où : JDirectItems Auction
* Info : Il faut impérativement un lecteur de génération 3. Il vient souvent avec le VFD intégré. On peut les reconnaître au logo Aime qui diffère de celui de la génération précédente. Ils ne sont pas très rares et on en trouve souvent venant d'une borne Star Horse 4.

</div>

<div class="equipment-card" markdown>

### Dalle tactile HDX (x2)
* Où : [Sur le discord HanDevice](https://discord.gg/xABCFMWmTK)
* Info : Il s'agit d'une dalle tactile créée par un particulier, dans le but de fournir un « game-pad », une sorte de manette personnalisée permettant de jouer à un simulateur de maimai DX dans le confort de son domicile. Officiellement ils ne vendent pas de kit de conversion directement, mais il est possible de [contacter le fabricant via son discord](https://discord.com/channels/1336383976721616897/1393421596190048266/1393822351094841375) pour lui demander une offre portant uniquement sur la dalle tactile **et** la HanDevice IO (sa carte I/O dédiée) qui va avec. Cette carte I/O a l'avantage d'exposer un port série UART que nous pouvons exploiter pour la connecter directement au ALLS HX2 sans avoir besoin de transformer le signal.

*Alternative* : **Kit de conversion Yuancon - à base d'une dalle ADX (x2)**

* Où : [Sur le site de yuancon](https://yuancon.store/controller/UPDATEKIT)
* Info : Yuancon propose des kits de conversion incluant la dalle tactile et huit boutons, un kit permettant de convertir un côté de la borne. Ils sont équivalents aux HDX à ceci près que leur carte I/O n'inclut pas de port série. Elle communique uniquement en USB-CDC avec le PC, ce qui rend sa connexion à un ALLS HX2 difficile puisque ce signal ne peut pas être adapté directement via un simple convertisseur RS-232. C'est toutefois toujours possible [via un logiciel faisant office de proxy](https://gitea.farewell.dev/Yttris/maitouch_rs) en tournant sur un Raspberry Pi installé entre le ALLS et l'ADX, mais cela introduit une complexité que nous ne détaillerons pas dans ce guide. (Si vous décidez de partir sur cette option, vous n'avez pas besoin des boutons supplémentaires du point suivant.)

</div>

<div class="equipment-card" markdown>

### Boutons HDX (x16)
* Où : [Sur le discord HanDevice](https://discord.gg/xABCFMWmTK)
* Info : Les boutons de jeu pour l'anneau. Les boutons de FiNALE sont techniquement compatibles, mais le ressenti est totalement différent (et bien meilleur) sur DX. Il vaut donc largement la peine de mettre les boutons à jour. Il faut huit boutons par joueur, soit seize au total, mais il peut être utile d'en acheter quelques-uns en réserve à l'avance. C'est une pièce d'usure.

*Alternative* : **Boutons "Rabbit" (x16)** 

* Où : [Sur la boutique taobao officielle](https://item.taobao.com/item.htm?id=660013732031&skuId=5395223410039&spm=a1z10.1-c.w4004-24097871292.3.37221e09DSieDY)
* Info : Assez similaires aux boutons officiels de maimai DX, ils représentent une excellente alternative.

!!! failure "N'achetez pas les contrefaçons!"
    Il existe effectivement des boutons génériques beaucoup moins chers qui sont en apparence très similaires, trouvables sur Taobao ou AliExpress. Ne succombez pas à la tentation d'économiser quelques euros, c'est le pire achat que vous puissiez faire. Contrairement aux boutons de HanDevice ou de Rabbit, ils sont de **très** mauvaise qualité, présentent une liste sans fin de problèmes et une durabilité minime. Préférez des boutons de qualité venant d'un vendeur fiable.

</div>

<div class="equipment-card" markdown>

### Bouton OBSF-24TR (x2)

* Où : [SmallCab](https://www.smallcab.net/sanwa-obsf-24tr-p-2080.html) ou [Jammastar](https://jammastar.com/gb/353-sanwa-obsf-24tr)
* Info : Les boutons "triangle" de tri pour le Joueur 1 et le Joueur 2, situés au centre de la borne au-dessus du lecteur Aime. Typiquement **bleu pour le Joueur 1 et rouge pour le Joueur 2**.

*Alternative* : ... Littéralement n'importe quels autres boutons

* Où : AliExpress, amazon, etc
* Info : Ces boutons sont très peu utilisés dans le jeu, et bien qu'il s'agisse de véritables Sanwa OBSF-24TR sur la borne originale, il n'y a vraiment pas besoin d'un bouton de qualité pour le faible usage qu'ils ont. N'importe quelle contrefaçon fera très bien l'affaire.

</div>

<div class="equipment-card" markdown>

### HUB USB 4 ports

!!! warning "Avertissement"
    Cette étape est théorique et n'a pas encore été testée.

* Où : Amazon, AliExpress, votre boutique favorite
* Info : Dans une véritable maimai DX, un des 4 ports USB de la carte mère du ALLS est dédié à un hub USB de quatre ports. Ce hub accueille les deux caméras des lecteurs de QR-Code et l'adaptateur RS-232/USB sur lequel sont connectés les contrôleurs de LEDs du joueur 1 et du joueur 2. Même si vous ne souhaitez pas utiliser les caméras de QR code, vous devez quand même brancher le hub pour que l'adaptateur RS-232/USB des contrôleurs de LEDs soit reconnu nativement par le système d'exploitation du ALLS. N'importe quel hub USB fera l'affaire. (Voir [Étape 1 : Le Remplacement du PC Central (ALLS)](step-1-alls-and-psu.md) pour le détail.)

</div>

D'autres petits achats sont nécessaires pour la suite du guide, et sont repris dans [Petites fournitures](#petites-fournitures).

## Matériel optionnel pour la caméra et les lecteurs de QR-code

L'installation de la caméra des joueurs et des lecteurs de QR-code est optionnelle, mais si vous souhaitez la réaliser, vous aurez besoin du matériel suivant.

<div class="equipment-card" markdown>

### Caméra des joueurs

* Où : Amazon, AliExpress, votre boutique favorite
* Info : N'importe quelle webcam USB bon marché fera l'affaire, si tant est qu'elle supporte UVC (si votre caméra fonctionne dès son branchement initial sans avoir besoin de drivers spécifiques, alors elle est sans doute compatible). Sur une maimai DX originale, la caméra possède une résolution native de 1280x960 pixels, et celle-ci est peu utilisée en jeu. Inutile donc de dépenser des fortunes.

</div>

<div class="equipment-card" markdown>

### Caméra pour QR-Code (x2)

* Où : Amazon, AliExpress, votre boutique favorite ([exemple de caméra compatible](https://www.amazon.com.be/dp/B0DWLGCSJ6))
* Info : Le jeu est très exigeant sur la caméra USB requise pour les lecteurs de QR-Code. Celle-ci doit être UVC et supporter une résolution de 640x480 en 30 fps au format YUY2, un angle de vue de 50°, et il est nécessaire d'avoir une lumière externe pour éclairer la zone.  
(Une LED adaptée est proposée dans les [Petites fournitures](#petites-fournitures))

</div>

## Petites fournitures

Vous trouverez ces articles dans votre boutique préférée (Amazon, AliExpress, ...). Il s'agit de petits achats peu chers dont vous aurez besoin au cours des différentes étapes.

### Câbles

* **1x**{: .quantity-emphasis } **Câble HDMI vers DVI-D (3 m)** 
    - Branchement du ALLS vers l'écran du joueur 1.
* **1x**{: .quantity-emphasis } **Câble DVI-D vers DVI-D (2 m)** 
    - Branchement du ALLS vers l'écran du joueur 2. Votre FiNALE en a peut-être déjà nativement un.
* **1x**{: .quantity-emphasis } **Câble DB-9 Femelle-Femelle** 
    - Le plus court possible, le câble sera coupé pour faire deux connecteurs, pour le lecteur Aime et le VFD.
* **4x**{: .quantity-emphasis } **Câble DB-9 Mâle-Femelle (3 m)** 
    - Utilisé comme rallonge pour raccorder le lecteur Aime au ALLS.
    - Utilisé comme rallonge pour raccorder le VFD au ALLS.
    - Utilisé comme rallonge pour raccorder la dalle tactile du joueur 1 au ALLS.
    - Utilisé comme rallonge pour raccorder la dalle tactile du joueur 2 au ALLS.
* **1x**{: .quantity-emphasis } **Câble IEC C-13 (2 m)** 
    - Branché au ALLS et coupé à hauteur de la prise pour être raccordé en direct à l'alimentation de la borne.

### Convertisseurs

* **2x**{: .quantity-emphasis } **Convertisseur TTL vers RS-232 avec DB-9 Femelle** ([exemple](https://www.amazon.com.be/dp/B09L1BB6F8)) 
    - Pour faire le lien entre l'IO de la dalle tactile du joueur 1 et la connexion DB-9 du ALLS.
    - Pour faire le lien entre l'IO de la dalle tactile du joueur 2 et la connexion DB-9 du ALLS.

### Connecteurs

* **1x**{: .quantity-emphasis } **Connecteur Molex 14 broches femelle** ([exemple](https://www.amazon.com/dp/B078H8F2YQ)) - Pour raccorder proprement le connecteur d'alimentation préalablement raccordé au RingEdge2.

!!! abstract "En cours d'écriture"
    Cette liste est incomplète, elle sera enrichie en même temps que les points suivants.  
    Reste à ajouter une fois les détails connus :
    
    - 2x Prises jack pour le casque et les câbles qui vont avec
    - 2x amplis son pour les casques
    - 2x Raspberry Pi Pico et leurs hats pour le proxy des LEDs
    - Les connecteurs JST-XH 7 et 9 broches mâle/femelle pour connecter le proxy
    - Les connecteurs JST-XH 2 broches mâle/femelle pour l'alimentation à plusieurs endroits
    - Le connecteur JST-XH 7 broches femelle pour le lecteur Aime
    - Le connecteur JST-PH 8 broches femelle pour le VFD
    - Le connecteur JST-PH 4 broches femelle pour l'adaptateur de HanDevice vers le convertisseur TTL
    - Les broches pour JST-RA pour les nouveaux câbles à mettre sur la nappe RA60P de l'IO4
    - Le JST-RA femelle pour la nappe RA20P de l'IO4
    - 2x LED blanches pour les lecteurs de QR-code
    - 1x LED rouge pour indiquer que la caméra filme
    - 1x LED blanche chaude pour éclairer la caméra


---

!!! warning "Vérifiez votre matériel avant de commencer"
    Assurez-vous d'avoir reçu et testé tout le matériel que vous aurez commandé avant de vous lancer dans la conversion à proprement parler. Cela vous épargnera bien des migraines à tenter de comprendre pourquoi votre installation ne fonctionne pas si vous écartez d'entrée la théorie du matériel défectueux.

---

Maintenant que vous disposez du matériel, commençons par l'[Étape 1 : Le Remplacement du PC Central (ALLS)](step-1-alls-and-psu.md).
