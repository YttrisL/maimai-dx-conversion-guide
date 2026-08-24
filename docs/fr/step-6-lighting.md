---
title: "💡 6 - Lumières"
---

# 💡 Étape 6 : Lumières

L'éclairage est techniquement une étape *optionnelle* de la conversion, dans le sens ou elle n'impacte pas la jouabilité de la borne. Toutefois l'opération n'est pas si complexe et l'éclairage apporte beaucoup au charme de maimai DX. Il est donc recommandé de ne pas ignorer cette étape.

## Explications techniques

??? note "Cliquez ici pour le détail technique"
    ### Fonctionnement des LEDs sur une maimai DX

    Sur une véritable borne *DX*, l'éclairage est piloté par trois contrôleurs différents :

    * L'**IO4** gère l'éclairage de l'enseigne lumineuse, le dessus de la borne. Voir l'[Étape 3](step-3-io-board.md).
    * Deux cartes de contrôle identiques (réf. `837-15070-04`) :
        * Côté P1 : Les huit boutons, l'éclairage du fond, et l'éclairage du côté gauche.
        * Côté P2 : Les huit boutons, l'éclairage du fond, et l'éclairage du côté droit.

    ![Chaîne de contrôle de l'éclairage : les cartes LED P1 et P2 (réf. `837-15070-04`) rejoignent en RS-232 le convertisseur RS-232 vers USB (réf. `837-15067-02`), lui-même branché au hub USB partagé avec les caméras QR-Code de P1 et P2](../resources/images/step-6-lighting/led-controllers-chain.svg){ width="720" }

    Les deux cartes de contrôle s'interfacent en RS-232 à une unique PCB convertissant les deux signaux RS-232 en USB. Cette PCB est elle-même raccordée au même hub USB que les lecteurs de QR-Code (voir [Étape 7](step-7-cameras.md)).

    !!! info "Configuration logicielle des ports COM"
        Les contrôleurs de LEDs sont interfacés sur les ports COM virtuels du ALLS de la façon suivante :

        * **COM21** pour les LEDs du P1.
        * **COM23** pour les LEDs du P2.

    ### Fonctionnement des LEDs sur une maimai FiNALE

    Le fonctionnement est un peu plus simple sur FiNALE :

    * Contrairement à DX, aucune LED ne passe par l'IO3 de FiNALE.
    * Deux cartes de contrôle identiques gèrent les LEDs (réf. `837-15070-02-91`) :
        * Côté P1 : Les huit boutons, l'éclairage du fond, les lumières du woofer, et le dessus de la borne côté P1.
        * Côté P2 : Les huit boutons, l'éclairage du fond, les lumières du woofer, et le dessus de la borne côté P2.

    ![Chaîne de contrôle de l'éclairage sur FiNALE : les cartes LED P1 et P2 (réf. `837-15070-02-91`) rejoignent en RS-232 le même convertisseur RS-232 vers USB que sur DX (réf. `837-15067-02`), branché directement sur un port USB du RingEdge 2, sans hub USB](../resources/images/step-6-lighting/led-controllers-chain-finale.svg){ width="720" }

    Comme sur DX, ces deux cartes de contrôle s'interfacent en RS-232 à la même PCB convertissant les deux signaux RS-232 en USB. Par chance, **c'est exactement la même sur FiNALE et sur DX (réf. `837-15067-02`)**.

    Sur FiNALE par contre, ce convertisseur se branche directement sur un port USB du RingEdge 2, sans passer par un hub USB.

    ### Ce que ça implique pour une conversion

    Trois observations :

    * Nous aurons besoin d'un hub USB 4 ports pour reproduire l'architecture de branchement sur le ALLS. maimai DX est très exigeant sur le port sur lequel les appareils USB sont connectés sur le ALLS.
    * Sur DX, le woofer au bas de la borne n'est pas éclairé. Le jeu n'envoie donc pas l'information nécessaire pour piloter ces LEDs sur une borne maimai FiNALE. Il est toutefois possible de ruser, *voir plus bas*.
    * L'éclairage du dessus de la borne n'est plus connecté aux contrôleurs de LEDs sur DX, ceux-ci ne reçoivent donc plus l'information pour l'éclairer. Il faudra recâbler ce connecteur vers l'IO4.

    Mais surtout, le point le plus important : les contrôleurs de LEDs de FiNALE et de DX **n'ont pas la même référence**. Si vous tentez de brancher un contrôleur de LEDs FiNALE sur un ALLS faisant tourner DX, **le jeu se mettra en erreur non-bloquante au démarrage** car la référence envoyée par le contrôleur, `837-15070-02-91`, n'est pas celle que le jeu s'attend à recevoir, `837-15070-04`. Fait amusant : dans cet état, le jeu enverra tout de même les informations pour l'éclairage des boutons de jeu, mais pas pour le fond.

    Heureusement, il y a une solution pour ces trois problèmes.

## Pour les boutons de jeu et le fond des deux joueurs

## Pour le dessus de la borne

--8<-- "includes/untested-fr.md"

Puisque le contrôleur de LEDs de DX ne gère plus l'allumage du haut de la borne, le jeu ne lui envoie tout simplement pas l'information. Dans DX, c'est l'IO4 qui s'occupe de gérer ces LEDs.

Bonne nouvelle, la structure des LEDs n'a pas changé de FiNALE à DX, il s'agit toujours d'une simple bande de LEDs RGB non-adressables alimentée en 12v. Le connecteur est différent, mais dans notre cas ce n'est pas très important.

Sur maimai FiNALE, il y a trois connecteur pour le sommet de la borne :

* Un pour le côté gauche, côté joueur 1.
* Un pour le centre, celui-ci n'existe plus dans DX. Il peut être soit ignoré, soit connecté à un joueur ou l'autre.
* Un pour le côté droit, côté joueur 2.

Dans les trois cas, le connecteur a toujours la même structure. Dans cet ordre :

* Broche 1 : **12v** 
* Broche 2 : **R** 
* Broche 3 : **G** 
* Broche 4 : **B**

Une IO4 de DX dédie 3 broches pour les signaux R - G - B du côté gauche, et 3 broches aux signaux R - G - B du côté droit.

Vous devez créer un adaptateur en utilisant un connecteur JST-RA 20 broches qui viendra se connecter sur le CN9 de l'IO4, et deux broches qui viennent se rajouter sur les position 51 et 52 du gros connecteur CN3.

Consultez [le schéma de câblage (planche 2/4)](http://127.0.0.1:8000/fr/wiring-diagrams/#planche-24-boutons-leds-de-boutons-hub-usb-et-carte-io)**[E-2→E-3]**{: .wiring-coord } et **[F-5]**{: .wiring-coord } pour connaître l'ordre des broches à sertir.

--8<-- "includes/wip-fr.md"

## Pour les woofers des deux joueurs

--8<-- "includes/untested-fr.md"

Sur DX, les woofers au bas de la borne ne sont pas éclairés. Il n'y a donc aucun signal provenant du jeu destiné à en allumer les LEDs.

Il n'existe pas de réelle solution pour inférer ce signal. On pourrait penser en observant les signaux fournis par le contrôleur de LEDs d'un maimai DX que l'entrée nommée "1/2P SIDE COVER LED" pourrait être un signal de substitution, cette zone n'existant pas sur une maimai FiNALE. Toutefois, ce signal sert à alimenter une simple bande de LEDs blanches statiques, **et ne serait pas compatible**.

Les LEDs des woofers sont deux bandes de LEDs RGB non-adressables alimentées en 12v, **exactement comme l'éclairage du dessus de la borne**. Même le brochage du connecteur est identique. La meilleure option est donc de venir raccorder les deux connecteurs des woofers (J1 et J2) sur l'IO4 pour les éclairer de la même teinte que le sommet de la borne. Il s'agit d'une solution à la fois simple (*il suffit d'un simple connecteur en Y*) et élégante puisque cela permet de conserver cette spécificité de FiNALE sur la borne convertie. 

De plus, l'éclairage du dessus d'une FiNALE étant bien moins visible que la panneau lumineux d'une DX, cela permet de renforcer la couleur du thème du jeu sur une autre partie de la borne bien plus visible.

--8<-- "includes/wip-fr.md"

---

Dernière étape (optionnelle) : les [Caméras](step-7-cameras.md).
