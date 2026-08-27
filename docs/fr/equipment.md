---
title: "🛒 Liste de courses"
---

# 🛒 Liste de courses : Le matériel nécessaire

!!! tip "Pas besoin du détail ?"
    La [checklist d'achats](equipment-checklist.md) reprend tous les articles à acheter, sans les explications.

## Préambule
Pour chacune des pièces listées ci-dessous, l'option la plus adaptée est mise en avant. Cela peut être pour plusieurs raisons : simplicité d'installation, prix ou disponibilité. *Lorsqu'elles existent, les alternatives sont mentionnées.* Ce guide part toutefois du principe que vous avez choisi l'option principale et ne s'attardera pas sur ces alternatives.

!!! info "Le marché de l'occasion japonais"
    Si le marché de seconde main japonais et ses options d'achat ne vous sont pas familiers, n'hésitez pas à consulter l'annexe [Le marché de l'occasion japonais](secondhand-market.md).

## Matériel obligatoire

<div class="equipment-card" markdown>

### ALLS HX2
* Où : JDirectItems Auction 
* Info : En fonction des périodes, il peut être assez difficile à trouver. C'est le système utilisé par maimai DX, et peu d'autres bornes l'utilisent.

*Alternative* : **ALLS MX2**

* Où : JDirectItems Auction 
* Info : Celui-ci se trouve plus facilement. Il nécessitera toutefois un downgrade pour être rendu compatible avec maimai DX. L'opération n'est pas documentée publiquement.

!!! info "Espace de stockage"
    En fonction du jeu que faisait tourner nativement votre ALLS, il est possible que celui-ci ne contienne qu'un SSD de 64 Go.
    Si c'est le cas, ce ne sera pas suffisant pour installer le jeu. Vous devrez alors vous procurer un SSD d'au moins 128 Go, idéalement 256 Go. N'importe quel modèle SATA fera l'affaire.

</div>

<div class="equipment-card" markdown>

### Carte I/O Sega IO4
* Où : JDirectItems Auction 
* Info : Simple à trouver, elle est utilisée dans toutes les bornes Sega depuis plusieurs années. À ne pas confondre avec une IO3, elles se ressemblent beaucoup. Le meilleur moyen de reconnaître une IO4 est de vérifier qu'elle possède bien ses dip switches sur le dessus de la PCB. 

!!! info "Variantes d'IO4"
    Il existe plusieurs variantes d'IO4. Certaines, compatibles JVS, sont équipées d'un port USB-B et d'un USB-A pour le chaînage. D'autres avec un simple port micro-USB destinées à être connectées sur un port USB classique. Dans notre cas, la connexion avec le ALLS se fait en USB classique, via le port micro-USB. Le support JVS est donc inutile pour maimai DX. 

    Habituellement les IO4 sans support JVS sont un peu moins chères à la revente, mais en théorie toutes les variantes sont compatibles pour cette conversion.

</div>

<div class="equipment-card" markdown>

### Lecteur Aime (Gen. 3)
* Où : JDirectItems Auction
* Info : Il faut impérativement un lecteur de génération 3. Il vient souvent avec le VFD intégré. On peut les reconnaître au logo Aime, différent de celui de la génération précédente. Ils ne sont pas très rares et on en trouve souvent provenant de la borne Star Horse 4.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } Dalle tactile HDX
* Où : [Sur le discord HanDevice](https://discord.gg/xABCFMWmTK)
* Info : Il s'agit d'une dalle tactile créée par un particulier pour fournir un « game-pad » permettant de jouer à un simulateur de maimai DX dans le confort de son domicile. Officiellement, ils ne vendent pas de kit de conversion, mais il est possible de [contacter le fabricant via son discord](https://discord.com/channels/1336383976721616897/1393421596190048266/1393822351094841375) pour leur demander une offre portant uniquement sur la dalle tactile **et** la HanDevice IO (leur carte I/O dédiée) qui va avec. Cette carte I/O a l'avantage d'exposer un port série UART que nous pouvons exploiter pour la connecter directement au ALLS HX2 sans avoir besoin de transformer le signal.

*Alternative* : **2x**{: .quantity-emphasis } **Kit de conversion Yuancon - à base d'une dalle ADX**

* Où : [Sur le site de yuancon](https://yuancon.store/controller/UPDATEKIT)
* Info : Yuancon propose des kits de conversion incluant la dalle tactile et huit boutons, permettant de convertir un côté de la borne. Ils sont équivalents aux HDX à ceci près que leur carte I/O n'inclut pas de port série : elle communique uniquement en USB-CDC avec le PC, ce qui rend sa connexion à un ALLS HX2 difficile, puisque ce signal ne peut pas être adapté directement via un simple convertisseur RS-232. C'est toutefois possible [via un logiciel faisant office de proxy](https://gitea.farewell.dev/Yttris/maitouch_rs), qui tourne sur un Raspberry Pi installé entre le ALLS et l'ADX, mais cela introduit une complexité que nous ne détaillerons pas dans ce guide. (Si vous décidez de partir sur cette alternative, vous n'avez pas besoin des boutons supplémentaires du point suivant.)

</div>

<div class="equipment-card" markdown>

### **16x**{: .quantity-emphasis } Boutons HDX
* Où : [Sur le discord HanDevice](https://discord.gg/xABCFMWmTK)
* Info : Les boutons de jeu pour l'anneau. Les boutons de FiNALE sont techniquement compatibles, mais le ressenti est totalement différent (et bien meilleur) sur DX. Il vaut donc largement la peine de les mettre à jour. Il faut huit boutons par joueur, soit seize au total, mais il peut être utile d'en acheter quelques-uns en réserve. C'est une pièce d'usure.

*Alternative* : **16x**{: .quantity-emphasis } **Boutons "Rabbit"**

* Où : [Sur la boutique Taobao officielle](https://item.taobao.com/item.htm?id=660013732031&skuId=5395223410039&spm=a1z10.1-c.w4004-24097871292.3.37221e09DSieDY)
* Info : Assez similaires aux boutons officiels de maimai DX, ils représentent une excellente alternative.

!!! failure "N'achetez pas les contrefaçons !"
    Il existe des boutons génériques beaucoup moins chers, en apparence très similaires, que l'on trouve sur Taobao ou AliExpress. Ne succombez pas à la tentation d'économiser quelques euros, c'est le pire achat que vous puissiez faire. Contrairement aux boutons de HanDevice ou de Rabbit, ils sont de **très** mauvaise qualité, cumulent les problèmes et ont une durabilité minime. Préférez des boutons de qualité venant d'un vendeur fiable.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } Bouton OBSF-24TR

* Où : [SmallCab](https://www.smallcab.net/sanwa-obsf-24tr-p-2080.html) ou [Jammastar](https://jammastar.com/gb/353-sanwa-obsf-24tr)
* Info : Les boutons de tri "triangle" du Joueur 1 et du Joueur 2, situés au centre de la borne au-dessus du lecteur Aime. Typiquement **bleu pour le Joueur 1 et rouge pour le Joueur 2**.

*Alternative* : ... Littéralement n'importe quels autres boutons

* Où : AliExpress, Amazon, etc.
* Info : Ces boutons sont très peu utilisés dans le jeu, et bien qu'il s'agisse de véritables Sanwa OBSF-24TR sur la borne originale, il n'y a vraiment pas besoin d'un bouton de qualité vu le faible usage qui en est fait. N'importe quelle contrefaçon fera très bien l'affaire.

</div>

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } HUB USB 4 ports

--8<-- "includes/untested-fr.md"

* Où : Amazon, AliExpress, votre boutique favorite
* Info : Dans une véritable maimai DX, un des 4 ports USB de la carte mère du ALLS est dédié à un hub USB de 4 ports. Ce hub accueille les deux caméras des lecteurs de QR-Code et l'adaptateur RS-232/USB sur lequel sont connectés les contrôleurs de LEDs du joueur 1 et du joueur 2. Même si vous ne souhaitez pas utiliser les caméras de QR code, vous devez quand même brancher le hub, afin que l'adaptateur RS-232/USB des contrôleurs de LEDs soit reconnu nativement par le système d'exploitation du ALLS. N'importe quel hub USB fera l'affaire. (Voir [Étape 1 : Le Remplacement du PC Central (ALLS)](step-1-alls-and-psu.md) pour le détail.)

</div>

D'autres petits achats sont nécessaires pour la suite du guide, et sont repris dans [Petites fournitures](#petites-fournitures).

## Matériel optionnel pour la caméra et les lecteurs de QR-code

L'installation de la caméra des joueurs et des lecteurs de QR-code est optionnelle, mais si vous souhaitez la réaliser, vous aurez besoin du matériel suivant.

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } Caméra des joueurs

* Où : Amazon, AliExpress, votre boutique favorite
* Info : N'importe quelle webcam USB bon marché fera l'affaire, si tant est qu'elle supporte UVC (si votre caméra fonctionne dès son branchement initial sans avoir besoin de drivers spécifiques, alors elle est sans doute compatible). Sur une maimai DX originale, la caméra possède une résolution native de 1280x960 pixels, et cette résolution est peu exploitée en jeu. Inutile donc de dépenser une fortune.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } Caméra pour QR-Code

* Où : Amazon, AliExpress, votre boutique favorite ([exemple de caméra compatible](https://www.amazon.com.be/dp/B0DWLGCSJ6))
* Info : Le jeu est très exigeant sur la caméra USB requise pour les lecteurs de QR-Code. Celle-ci doit être UVC, supporter une résolution de 640x480 en 30 fps au format YUY2 et offrir un angle de vue de 50°. Une lumière externe est par ailleurs nécessaire pour éclairer la zone.  
(Une LED adaptée est proposée dans les [Petites fournitures](#petites-fournitures))

</div>

## Petites fournitures

Vous trouverez ces articles dans votre boutique préférée (Amazon, AliExpress, ...). Il s'agit de petits achats bon marché dont vous aurez besoin au fil des différentes étapes.

<div class="equipment-supplies" markdown>

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
* **2x**{: .quantity-emphasis } **Câble micro-USB** de charge
    - Pour alimenter les deux proxys des contrôleurs de LEDs. L'extrémité opposée au Pico est coupée pour raccorder le fil rouge sur le 5V et le fil noir sur la masse de l'alimentation installée à l'[étape 1](step-1-alls-and-psu.md).

### Électronique

* **2x**{: .quantity-emphasis } **Convertisseur TTL vers RS-232 avec DB-9 femelle** ([exemple](https://www.amazon.com.be/dp/B09L1BB6F8)) 
    - Pour faire le lien entre l'IO de la dalle tactile du joueur 1 et la connexion DB-9 du ALLS.
    - Pour faire le lien entre l'IO de la dalle tactile du joueur 2 et la connexion DB-9 du ALLS.
* **2x**{: .quantity-emphasis } **Raspberry Pi Pico** ([exemple](https://aliexpress.com/item/1005007393927221.html)) 
    - Pour fabriquer les proxy des contrôleurs de LEDs. Préférez une version avec les broches pré-soudés sur le Pico si vous souhaitez une installation sans soudure. **Attention, les broches doivent être soudées vers les bas, pas vers le haut.**
* **2x**{: .quantity-emphasis } **Pico-2CH-RS232** ([exemple](https://aliexpress.com/item/1005012732708840.html)) 
    - Pour fabriquer les proxy des contrôleurs de LEDs


### Fils de câblage

* **Fil de câblage souple (AWG 22-24)** 
    - Il y aura plusieurs câbles à sertir tout au long de ce guide, prévoyez d'en avoir de réserve.


### Connecteurs

* **1x**{: .quantity-emphasis } **Connecteur Molex Mini-Fit Jr. 2x7 broches femelle** ([exemple](https://www.amazon.com/dp/B078H8F2YQ)) 
    - Pour raccorder proprement le connecteur d'alimentation préalablement raccordé au RingEdge2.
* **30x**{: .quantity-emphasis } **Broche Molex Mini-Fit Jr. femelle à sertir** 
    - Pour aller avec le connecteur précédent.
* **1x**{: .quantity-emphasis } **Connecteur JST-RA 2x10 broches femelle** 
    - Pour le CN9 de l'IO4.
* **30x**{: .quantity-emphasis } **Broche JST-RA femelle à sertir** 
    - Pour peupler le CN9 et les câbles à rajouter sur le CN3 de l'IO4.
* **2x**{: .quantity-emphasis } **Connecteur JST-SM 8 broches, paire mâle + femelle** 
    - Extrémités de la nappe d'éclairage de l'enseigne lumineuse, côté joueur 1 et côté joueur 2, à raccorder aux connecteurs JST-SM d'origine.
* **2x**{: .quantity-emphasis } **Connecteur JST-SM 2 broches, paire mâle + femelle**
    - Idéal pour faire nos propres connecteurs pour nous faciliter la vie, mais si vous n'en avez pas de stock de simples JST-XH peuvent également convenir.

Pour le reste des connecteurs, plutôt que d'acheter chaque référence à l'unité, procurez-vous directement un kit d'assortiment par type de connecteur : on en trouve facilement sur Amazon ou AliExpress, regroupant plusieurs tailles de boîtiers, les deux genres (mâle/femelle) et un lot de broches à sertir. Voici ce dont vous aurez besoin dans chacun :

**Kit JST-XH**

* **20x**{: .quantity-emphasis } Connecteur 2 broches mâle
* **20x**{: .quantity-emphasis } Connecteur 2 broches femelle
* **2x**{: .quantity-emphasis } Connecteur 7 broches femelle
* **1x**{: .quantity-emphasis } Connecteur 7 broches mâle
* **1x**{: .quantity-emphasis } Connecteur 9 broches femelle
* **1x**{: .quantity-emphasis } Connecteur 9 broches mâle
* **50x**{: .quantity-emphasis } Broche mâle à sertir
* **50x**{: .quantity-emphasis } Broche femelle à sertir

**Kit JST-PH**

* **2x**{: .quantity-emphasis } Connecteur 4 broches femelle
* **1x**{: .quantity-emphasis } Connecteur 8 broches femelle
* **30x**{: .quantity-emphasis } Broche mâle à sertir
* **30x**{: .quantity-emphasis } Broche femelle à sertir

</div>

!!! abstract "En cours d'écriture"
    Cette liste est incomplète, elle sera enrichie en même temps que les points suivants.  
    Il reste à ajouter, une fois les détails connus :
    
    - **2x**{: .quantity-emphasis } Prises jack pour le casque et les câbles qui vont avec
    - **2x**{: .quantity-emphasis } Amplis son pour les casques
    - **2x**{: .quantity-emphasis } LED blanches pour les lecteurs de QR-code
    - **1x**{: .quantity-emphasis } LED rouge pour indiquer que la caméra filme
    - **1x**{: .quantity-emphasis } LED blanche chaude pour éclairer la caméra

---

!!! warning "Vérifiez votre matériel avant de commencer"
    Assurez-vous d'avoir reçu et testé tout le matériel que vous aurez commandé avant de vous lancer dans la conversion à proprement parler. Cela vous évitera bien des migraines : si un problème survient, vous pourrez d'emblée écarter l'hypothèse du matériel défectueux.

---

!!! tip "Voici la checklist simplifiée"
    Envie de cocher vos achats au fur et à mesure plutôt que de vous replonger dans le détail ? Voici la [checklist d'achat](equipment-checklist.md).

---

Maintenant que vous disposez du matériel, commençons par l'[Étape 1 : Le Remplacement du PC Central (ALLS)](step-1-alls-and-psu.md).

