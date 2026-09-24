---
title: "🛒 Liste de courses"
---

# 🛒 Liste de courses : Le matériel nécessaire

!!! tip "Pas besoin du détail ?"
    La [checklist d'achats](equipment-checklist.md) reprend tous les articles à acheter, sans les explications.

## Préambule
Pour chaque pièce, **l'option la plus adaptée est mise en avant**, que ce soit pour sa simplicité d'installation, son prix ou sa disponibilité. *Les alternatives sont mentionnées lorsqu'elles existent*, mais le guide part du principe que vous avez choisi l'option principale et ne les détaille pas.

!!! info "Le marché de l'occasion japonais"
    Le marché de seconde main japonais ne vous est pas familier ? Consultez l'annexe [Le marché de l'occasion japonais](secondhand-market.md).

## Matériel obligatoire

<div class="equipment-card" markdown>

### ALLS HX2
* Où : JDirectItems Auction 
* Info : C'est le PC utilisé par DX, et peu d'autres bornes utilisent ce modèle spécifique : **selon les périodes, il peut être difficile à trouver**.

*Alternative* : **ALLS MX2**

* Où : JDirectItems Auction 
* Info : Plus facile à trouver, et son logiciel interne est techniquement compatible avec DX.

!!! info "Espace de stockage"
    Selon le jeu qu'il faisait tourner à l'origine, votre ALLS ne contient peut-être qu'un SSD de 64 ou 128 Go, **insuffisant pour installer le jeu**. Il faut obligatoirement un disque secondaire (nommé "SUB STORAGE"), généralement de 500 Go. Si votre ALLS n'en a pas, vous devrez vous en procurer un.

</div>

<div class="equipment-card" markdown>

### Carte I/O Sega IO4
* Où : JDirectItems Auction 
* Info : Facile à trouver, elle équipe toutes les bornes Sega depuis plusieurs années. **Attention à ne pas la confondre avec une IO3**, très ressemblante : le plus sûr est de vérifier la présence de **dip switches sur le dessus de la PCB**, que seule l'IO4 possède.

!!! info "Variantes d'IO4"
    Il existe plusieurs variantes d'IO4 :

    - **compatibles JVS**, avec un port USB-B et un port USB-A pour le chaînage ;
    - **sans JVS**, avec un simple port micro-USB à brancher sur un port USB classique.

    Sur maimai DX, l'IO4 se branche au ALLS en USB classique, via le port micro-USB : **le support JVS est inutile**. Les IO4 sans JVS sont généralement un peu moins chères, mais en théorie toutes les variantes conviennent.

</div>

<div class="equipment-card" markdown>

### Lecteur Aime (Gen. 3)
* Où : JDirectItems Auction
* Info : **Il faut impérativement un lecteur de génération 3**, souvent vendu avec le VFD intégré. On le reconnaît à son logo Aime, différent de celui de la génération précédente. Il n'est pas très rare : on en trouve souvent issus de bornes Star Horse 4.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } Dalle tactile HDX
* Où : [Sur le discord HanDevice]({{DISCORD_HANDEVICE}})
* Info : Une dalle tactile conçue par un particulier, à l'origine comme « game-pad » pour jouer à un simulateur de DX chez soi. HanDevice ne vend pas officiellement de kit de conversion, mais vous pouvez [contacter le fabricant sur son discord]({{HANDEVICE_DISCORD_CONTACT_MESSAGE}}) pour demander une offre portant sur **la dalle tactile et la HanDevice IO** (sa carte I/O dédiée). Avantage de cette carte : elle expose un **port série UART**, qui permet de la relier au ALLS HX2 sans transformer le signal.

*Alternative* : **2x**{: .quantity-emphasis } **Kit de conversion Yuancon - à base d'une dalle ADX**

* Où : [Sur le site de yuancon]({{YUANCON_CONVERSION_KIT_PAGE}})
* Info : Chaque kit Yuancon comprend une dalle tactile et huit boutons, de quoi convertir un côté de la borne. Ils équivalent aux HDX, à un détail près : **leur carte I/O n'a pas de port série**. Elle communique uniquement en USB-CDC, un signal qu'un simple convertisseur RS-232 ne peut pas adapter pour le ALLS HX2. C'est possible via un proxy logiciel, [maitouch_rs]({{MAITOUCH_RS_REPO}}) par [4ndr3w]({{GITHUB_4NDR3W}}) sur GitHub, qui tourne sur un Raspberry Pi placé entre le ALLS et l'ADX, mais cette complexité n'est pas détaillée dans ce guide. *Avec cette alternative, les boutons du point suivant sont inutiles.*

</div>

<div class="equipment-card" markdown>

### **16x**{: .quantity-emphasis } Boutons HDX
* Où : [Sur le discord HanDevice]({{DISCORD_HANDEVICE}})
* Info : Les boutons de jeu de l'anneau. Ceux de FiNALE sont techniquement compatibles, mais le ressenti sur DX est totalement différent, et bien meilleur : **le remplacement vaut largement la peine**. Il en faut huit par joueur, soit seize au total. *C'est une pièce d'usure* : quelques boutons de réserve peuvent être utiles.

*Alternative* : **16x**{: .quantity-emphasis } **Boutons "Rabbit"**

* Où : [Sur la boutique Taobao officielle]({{TAOBAO_OFFICIAL_SHOP_LISTING}})
* Info : Assez proches des boutons officiels de maimai DX, c'est une excellente alternative.

!!! failure "N'achetez pas les contrefaçons !"
    On trouve sur Taobao ou AliExpress des boutons génériques bien moins chers, en apparence très similaires. **Ne cédez pas à la tentation d'économiser quelques euros** : c'est le pire achat possible. Contrairement aux boutons HanDevice ou Rabbit, ils sont de **très** mauvaise qualité, cumulent les problèmes et durent très peu. Préférez des boutons de qualité, achetés chez un vendeur fiable.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } Bouton OBSF-24TR

* Où : [SmallCab]({{SMALLCAB_SANWA_OBSF_24TR}}) ou [Jammastar]({{JAMMASTAR_SANWA_OBSF_24TR}})
* Info : Les boutons de tri "triangle" des joueurs 1 et 2, au centre de la borne, au-dessus du lecteur Aime. Typiquement **bleu pour le joueur 1 et rouge pour le joueur 2**.

*Alternative* : ... Littéralement n'importe quels autres boutons

* Où : AliExpress, Amazon, etc.
* Info : La borne d'origine utilise de véritables Sanwa OBSF-24TR, mais ces boutons servent très peu en jeu : **inutile d'investir dans la qualité**. N'importe quelle contrefaçon fera très bien l'affaire.

</div>

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } Hub USB 4 ports

* Où : Amazon, AliExpress, votre boutique favorite
* Info : Sur une véritable maimai DX, l'un des 4 ports USB de la carte mère du ALLS est réservé à un hub USB 4 ports. Ce hub accueille les deux caméras des lecteurs de QR-Code et l'adaptateur RS-232/USB des contrôleurs de LEDs des joueurs 1 et 2. **N'importe quel hub USB fera l'affaire.**

</div>

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } Alimentation à découpage 5V/12V

* Où : Amazon, AliExpress, distributeurs de composants électroniques
* Info : Contrairement au RingEdge 2, le ALLS n'alimente pas les périphériques externes. Cette alimentation prend le relais : elle alimente notamment l'IO4, le lecteur Aime, le VFD et les proxys des contrôleurs de LEDs. Il vous faut un modèle **à double sortie 5V et 12V**, en boîtier métallique avec bornier à vis, comme les Mean Well RD-35A ou RD-50A. **Ne réutilisez pas les alimentations d'origine de la borne** à la place.

</div>

D'autres petits achats sont nécessaires pour la suite du guide : ils sont regroupés dans les [Petites fournitures](#petites-fournitures).

## Matériel optionnel pour la caméra et les lecteurs de QR-code

La caméra des joueurs et les lecteurs de QR-code sont **optionnels**. Si vous souhaitez les installer, voici le matériel nécessaire.

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } Caméra des joueurs

* Où : Amazon, AliExpress, votre boutique favorite
* Info : **N'importe quelle webcam USB bon marché fera l'affaire**, pourvu qu'elle soit UVC. *Si elle fonctionne dès le branchement, sans pilote particulier, elle est sans doute compatible.* La caméra d'origine filme en 1280x960, une résolution peu exploitée en jeu : inutile de dépenser une fortune.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } Caméra pour QR-Code

* Où : Amazon, AliExpress, votre boutique favorite ([exemple de caméra compatible]({{BUY_EXAMPLE_QR_CODE_CAMERA}}))
* Info : **Le jeu est très exigeant sur ces caméras.** Elles doivent être UVC, filmer en 640x480 à 30 fps au format YUY2, avec un angle de vue de 50°. Un éclairage externe est aussi nécessaire (voir [Éclairage](#eclairage)).

</div>

## Petites fournitures

Ces petits achats bon marché, nécessaires au fil des étapes, se trouvent dans votre boutique préférée (Amazon, AliExpress, ...).

<div class="equipment-supplies" markdown>

### Câbles

* **1x**{: .quantity-emphasis } **Câble HDMI vers DVI-D (3 m)** 
    - Branchement du ALLS vers l'écran du joueur 1.
* **1x**{: .quantity-emphasis } **Câble DVI-D vers DVI-D (2 m)** 
    - Branchement du ALLS vers l'écran du joueur 2. Votre FiNALE en a peut-être déjà nativement un.
* **1x**{: .quantity-emphasis } **Câble DB-9 Femelle-Femelle** 
    - Le plus court possible : il sera coupé en deux pour fabriquer les connecteurs du lecteur Aime et du VFD.
* **4x**{: .quantity-emphasis } **Câble DB-9 Mâle-Femelle (3 m)** 
    - Rallonges vers le ALLS pour le lecteur Aime, le VFD et les dalles tactiles des joueurs 1 et 2.
* **1x**{: .quantity-emphasis } **Câble IEC C-13 (2 m)** 
    - Branché au ALLS, puis coupé côté prise pour être raccordé directement à l'alimentation électrique de la borne.
* **2x**{: .quantity-emphasis } **Câble micro-USB** de charge
    - Pour alimenter les deux proxys des contrôleurs de LEDs : l'extrémité opposée au Pico est coupée, fil rouge sur le 5V et fil noir sur le GND de l'alimentation installée à l'[étape 1](step-1-alls-and-psu.md).

### Électronique

* **2x**{: .quantity-emphasis } **Convertisseur TTL vers RS-232 avec DB-9 femelle** ([exemple]({{BUY_EXAMPLE_TTL_RS232_CONVERTER}})) 
    - Pour relier la carte I/O de chaque dalle tactile (joueurs 1 et 2) à son port DB-9 du ALLS.
* **2x**{: .quantity-emphasis } **Raspberry Pi Pico** ([exemple]({{BUY_EXAMPLE_RASPBERRY_PI_PICO}})) 
    - Pour fabriquer les proxys des contrôleurs de LEDs. Pour éviter toute soudure, préférez une version aux broches pré-soudées. **Attention : les broches doivent être soudées vers le bas, pas vers le haut.**
* **2x**{: .quantity-emphasis } **Pico-2CH-RS232** ([exemple]({{BUY_EXAMPLE_PICO_2CH_RS232}})) 
    - Pour fabriquer les proxys des contrôleurs de LEDs.


### Fils de câblage

* **Fil de câblage souple (AWG 20)** 
    - Plusieurs câbles sont à sertir tout au long du guide : prévoyez-en une bonne réserve, idéalement de plusieurs couleurs.

### Éclairage

*Uniquement si vous installez les caméras optionnelles.*

* **1x**{: .quantity-emphasis } **Bande de LEDs blanc chaud 12V**
    - Éclairage de la caméra des joueurs.
* **1x**{: .quantity-emphasis } **Bande de LEDs RGB 12V à anode commune**
    - Éclairage des deux lecteurs de QR-code : une anode commune et une cathode par couleur. Environ 20 cm de bande suffisent.
* **1x**{: .quantity-emphasis } **LED rouge 12V avec résistance intégrée**
    - Indique aux joueurs que la caméra filme. **Une LED nue grillerait** sur le 12V : prenez un modèle prévu pour cette tension ou, à défaut, une résistance à part de 2,2 à 4,7 kOhm.

### Connecteurs

* **1x**{: .quantity-emphasis } **Connecteur Molex Mini-Fit Jr. 2x7 broches femelle** ([exemple]({{BUY_EXAMPLE_MOLEX_MINI_FIT_JR_CONNECTOR}})) 
    - Pour raccorder proprement le connecteur d'alimentation qui était branché sur le RingEdge 2.
* **30x**{: .quantity-emphasis } **Broche Molex Mini-Fit Jr. femelle à sertir** 
    - Pour aller avec le connecteur précédent.
* **1x**{: .quantity-emphasis } **Connecteur JST-RA 2x10 broches femelle** 
    - Pour le CN9 de l'IO4.
* **30x**{: .quantity-emphasis } **Broche JST-RA femelle à sertir** 
    - Pour le CN9 et les câbles à ajouter sur le CN3 de l'IO4.
* **2x**{: .quantity-emphasis } **Connecteur JST-SM 8 broches femelle** 
    - Extrémités de la nappe d'éclairage de l'enseigne lumineuse, côté joueur 1 et côté joueur 2, à raccorder aux connecteurs JST-SM d'origine.
* **2x**{: .quantity-emphasis } **Connecteur JST-SM 2 broches, paire mâle + femelle**
    - Idéal pour fabriquer vos propres connecteurs et vous simplifier la vie. À défaut, de simples JST-XH conviennent aussi.

Pour les autres connecteurs, plutôt que d'acheter chaque référence à l'unité, **procurez-vous un kit d'assortiment par type de connecteur**. On en trouve facilement sur Amazon ou AliExpress, avec plusieurs tailles de boîtiers, les deux genres (mâle/femelle) et un lot de broches à sertir. Voici ce qu'il vous faut dans chacun :

**Kit JST-XH**

* **20x**{: .quantity-emphasis } Connecteur 2 broches mâle
* **20x**{: .quantity-emphasis } Connecteur 2 broches femelle
* **2x**{: .quantity-emphasis } Connecteur 7 broches femelle
* **1x**{: .quantity-emphasis } Connecteur 7 broches mâle
* **2x**{: .quantity-emphasis } Connecteur 8 broches femelle
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
    Cette liste est incomplète et sera enrichie au fil de l'écriture du guide. Restent à ajouter, une fois les détails connus :
    
    - **2x**{: .quantity-emphasis } Prises jack pour le casque et les câbles qui vont avec
    - **2x**{: .quantity-emphasis } Amplis son pour les casques

---

!!! warning "Vérifiez votre matériel avant de commencer"
    **Recevez et testez tout le matériel commandé avant de commencer la conversion.** Vous vous éviterez bien des migraines : en cas de problème, vous pourrez d'emblée écarter l'hypothèse d'une pièce défectueuse.

---

!!! tip "Voici la checklist simplifiée"
    Envie de cocher vos achats au fur et à mesure, sans vous replonger dans le détail ? Utilisez la [checklist d'achat](equipment-checklist.md).

---

Maintenant que vous disposez du matériel, commençons par l'[Étape 1 : Le Remplacement du PC Central (ALLS)](step-1-alls-and-psu.md).

