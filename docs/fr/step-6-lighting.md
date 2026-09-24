---
title: "💡 6 - Lumières"
---

# 💡 Étape 6 : Lumières

L'éclairage est techniquement *optionnel* : il n'a aucun impact sur la jouabilité. Mais l'opération n'est pas si complexe et l'éclairage fait beaucoup pour le charme de DX. **Il est recommandé de ne pas faire l'impasse sur cette étape.**

## Explications techniques

??? note "Cliquez ici pour l'explication technique"
    ### Fonctionnement des LEDs sur une maimai DX

    Sur une véritable borne *DX*, l'éclairage est piloté par trois contrôleurs :

    * L'**IO4** gère l'**enseigne lumineuse** (désignée `BILLBOARD LED` / `ROOF LED` sur les schémas Sega). Voir l'[Étape 3](step-3-io-board.md).
    * Deux cartes de contrôle identiques (réf. `837-15070-04`) :
        * Côté P1 : les huit boutons, l'éclairage du fond et l'éclairage du côté gauche.
        * Côté P2 : les huit boutons, l'éclairage du fond et l'éclairage du côté droit.

    ![Chaîne de contrôle de l'éclairage : les cartes LED P1 et P2 (réf. `837-15070-04`) rejoignent en RS-232 l'adaptateur RS-232 vers USB (réf. `837-15067-02`), lui-même branché au hub USB partagé avec les caméras QR-Code de P1 et P2](../resources/images/step-6-lighting/led-controllers-chain.svg)

    Les deux cartes de contrôle sont reliées en RS-232 à un unique adaptateur RS-232 vers USB, lui-même branché sur le même hub USB que les lecteurs de QR-Code (voir [Étape 7](step-7-cameras.md)).

    !!! info "Configuration logicielle des ports COM"
        Les contrôleurs de LEDs apparaissent sur les ports COM virtuels suivants du ALLS :

        * **COM21** pour les LEDs du P1.
        * **COM23** pour les LEDs du P2.

    ### Fonctionnement des LEDs sur une maimai FiNALE

    Le fonctionnement est un peu plus simple sur FiNALE :

    * Contrairement à DX, aucune LED ne passe par l'IO3.
    * Deux cartes de contrôle identiques gèrent les LEDs (réf. `837-15070-02-91`) :
        * Côté P1 : les huit boutons, l'éclairage du fond, les woofers, et l'enseigne lumineuse côté P1 et au centre.
        * Côté P2 : les huit boutons, l'éclairage du fond, les woofers, et l'enseigne lumineuse côté P2.

    ![Chaîne de contrôle de l'éclairage sur FiNALE : les cartes LED P1 et P2 (réf. `837-15070-02-91`) rejoignent en RS-232 le même adaptateur RS-232 vers USB que sur DX (réf. `837-15067-02`), branché directement sur un port USB du RingEdge 2, sans hub USB](../resources/images/step-6-lighting/led-controllers-chain-finale.svg)

    Comme sur DX, ces deux cartes sont reliées en RS-232 à un adaptateur RS-232 vers USB. Par chance, **c'est exactement le même sur FiNALE et sur DX (réf. `837-15067-02`)**. Seule différence : sur FiNALE, il se branche directement sur un port USB du RingEdge 2, sans hub.

    ### Ce que ça implique pour une conversion

    * **Il faut un hub USB 4 ports** pour reproduire le branchement de *DX* sur le ALLS.
    * **L'enseigne lumineuse doit être recâblée vers l'IO4** : sur DX, les contrôleurs de LEDs ne reçoivent plus d'information pour l'éclairer.
    * Surtout, **les contrôleurs de LEDs de FiNALE et de DX n'ont pas la même référence**. Branché sur un ALLS avec DX, un contrôleur FiNALE provoque **une erreur non bloquante au démarrage** : il annonce `837-15070-02-91` alors que le jeu attend `837-15070-04`. Fait amusant : dans cet état, le jeu envoie tout de même l'éclairage des boutons, mais pas celui du fond.

    Heureusement, ces trois problèmes ont une solution.

## Pour les boutons de jeu et le fond des deux joueurs

Pour les contrôleurs de LEDs, **DX attend l'identifiant `837-15070-04`**, mais ceux de FiNALE renvoient `837-15070-02-91`, ce qui met le jeu en erreur. C'est le seul problème : pour le reste, le contrôleur de FiNALE est 100 % compatible avec les instructions envoyées par DX.

Il faut donc que les deux contrôleurs renvoient l'identifiant attendu. Un correctif logiciel serait simple, mais nous voulons laisser le logiciel du jeu intact : **la solution sera donc matérielle.**

**La solution :** un simple Raspberry Pi Pico, avec un firmware dédié, placé entre le contrôleur de LEDs et l'adaptateur RS-232 vers USB. Il **modifie uniquement le message contenant l'identifiant**, et transmet tous les autres à l'identique, dans les deux sens.

Le firmware existe déjà : il s'agit de [mailight_pico]({{MAILIGHT_PICO_REPO}}), un portage de *[mailight_rs]({{MAILIGHT_RS_REPO}})* par [4ndr3w]({{GITHUB_4NDR3W}}) sur GitHub. Il ne reste plus qu'à fabriquer le proxy.

### Fabriquer un proxy

!!! info "En double exemplaire"
    Il vous faut **deux proxys**, un par contrôleur de LEDs. Réalisez donc chaque opération en double.

**1. Installer le firmware.** Flashez mailight_pico sur le Raspberry Pi Pico. Si vous ne l'avez jamais fait, c'est extrêmement simple : [toutes les instructions sont sur la page du projet]({{MAILIGHT_PICO_FIRMWARE_INSTRUCTIONS}}).

**2. Assembler le Pico sur le `Pico-2CH-RS232`.** Attention au sens : les inscriptions sous le `Pico-2CH-RS232` indiquent où doit se trouver le port USB du Pico.

!!! lightbox
    ![Le module `Pico-2CH-RS232`, image tirée de la [page wiki officielle de Waveshare]({{WAVESHARE_PICO_2CH_RS232_WIKI}})](../resources/images/step-6-lighting/pico-2ch-rs232.png)

!!! warning "Attention au sens"
    Vérifiez que votre montage correspond bien à l'image. Si le port USB de votre Pico se retrouve par exemple entre les deux PCB plutôt qu'à l'extérieur, ses broches sont soudées dans le mauvais sens. **N'essayez pas de l'allumer**, vous endommageriez le `Pico-2CH-RS232`. Ressoudez les broches dans le bon sens, ou procurez-vous un Pico correctement assemblé.

**3. Préparer la connectique.** Le proxy s'insère entre le contrôleur de LEDs et l'adaptateur RS-232 vers USB. Le connecteur n'est pas le même selon le côté :

* Côté P1 : JST-XH **7** broches, mâle **et** femelle
* Côté P2 : JST-XH **9** broches, mâle **et** femelle

!!! lightbox
    ![Connecteur JST-XH côté P1](../resources/images/step-6-lighting/led-driver-connector-p1.png)
    ![Connecteur JST-XH côté P2](../resources/images/step-6-lighting/led-driver-connector-p2.png)

Pour vous simplifier la vie, reprenez les couleurs de la borne : **fil blanc sur la broche 4, fil rouge sur la broche 5**. Câblez les deux connecteurs de sorte que les couleurs soient alignées quand on enfiche le mâle dans le femelle.

Ces images proviennent du schéma de câblage, mais les connecteurs réels de la borne n'ont pas de fil `SHIELD` : la masse commune devra donc être raccordée ailleurs sur le `Pico-2CH-RS232`.

!!! lightbox
    ![Vue du dessus du module `Pico-2CH-RS232`](../resources/images/step-6-lighting/pico-2ch-rs232-photo.png)
    ![Le connecteur d'origine du contrôleur de LEDs dans la borne enfiché dans le connecteur confectionné à la main](../resources/images/step-6-lighting/led-controller-rs232-connector.jpg)

**4. Câbler les borniers.** Le connecteur **JST-XH femelle va sur le bornier Channel0** (côté adaptateur RS-232 vers USB), le connecteur **JST-XH mâle sur le bornier Channel1** (côté contrôleur de LEDs) :

* Channel0
    * TX0 : rouge
    * RX0 : blanc
    * GND : un fil noir, dont l'autre extrémité va sur le GND de l'alimentation installée à l'[étape 1](step-1-alls-and-psu.md).
* Channel1
    * TX1 : blanc
    * RX1 : rouge

**5. Alimenter le proxy.** Le plus simple est de brancher un câble micro-USB sur le Pico et d'en couper l'autre extrémité : **fil rouge sur le 5V, fil noir sur le GND** de l'alimentation installée à l'[étape 1](step-1-alls-and-psu.md).

Votre proxy est terminé !

!!! lightbox
    ![Le proxy terminé : le Raspberry Pi Pico assemblé sur le `Pico-2CH-RS232`, avec le connecteur JST-XH femelle (Channel0, côté adaptateur RS-232 vers USB) et le connecteur JST-XH mâle (Channel1, côté contrôleur de LEDs) câblés en fil rouge et blanc, et le câble micro-USB d'alimentation](../resources/images/step-6-lighting/pico-2ch-rs232-proxy-wired.jpg)

### Installer le proxy

Pour chaque contrôleur de LEDs :

* Débranchez le connecteur du contrôleur de LEDs et branchez-le sur le **connecteur mâle** du proxy.
* Branchez le **connecteur femelle** du proxy à sa place, sur l'adaptateur RS-232 vers USB.
* Alimentez le proxy.

Il ne reste plus qu'à brancher l'adaptateur RS-232 vers USB sur le ALLS via le hub USB. **Le jeu devrait reconnaître les contrôleurs de LEDs nativement**, sans aucune modification logicielle.

!!! warning "Branchez l'adaptateur correctement"
    Comme indiqué à l'[étape 1](step-1-alls-and-psu.md), **le hub USB doit être branché sur le port USB n°2** du ALLS, et l'adaptateur RS-232 vers USB sur ce hub. maimai DX est très exigeant sur les ports USB : en cas de mauvais branchement, les LEDs ne s'allumeront pas.

## Pour l'enseigne lumineuse et les woofers

??? note "Cliquez ici pour l'explication technique"
    Sur FiNALE, les woofers et l'enseigne lumineuse partagent le même circuit : allumer l'un allume forcément l'autre. Les woofers ne sont plus éclairés sur DX, mais ce n'est pas un problème puisque l'enseigne, elle, l'est toujours.

    En revanche, sur DX, **c'est l'IO4 qui gère ces LEDs** : le jeu n'envoie tout simplement plus cette information au contrôleur de LEDs. La raison de ce changement reste mystérieuse, mais il faut donc recâbler une partie des branchements.

    Par chance, le schéma de câblage de FiNALE référence un connecteur très pratique, qui permet de distribuer le signal côté joueur 1 et joueur 2 sans recâbler toute la borne :

    !!! lightbox
        ![Schéma de câblage FiNALE, connecteur AB côté P1 : le harnais MAI-60109 alimente les cartes CENTER LED, ROOF LED (L), ROOF LED (R) et WOOFER LED](../resources/images/step-6-lighting/lighting-topper-p1-side.png)
        ![Schéma de câblage FiNALE, connecteur BB côté P2 : le harnais MAI-60109 alimente les cartes WOOFER LED, ROOF LED (L) et ROOF LED (R), le connecteur SM5P n'étant pas utilisé](../resources/images/step-6-lighting/lighting-topper-p2-side.png)
        ![Connecteur JST-SM 8 broches qui connecte les woofers et l'enseigne lumineuse (en noir)](../resources/images/step-6-lighting/led-controller-rs232-disconnect.jpg)

    Le schéma du P1 comporte un élément `CENTER LED`, absent côté P2 : c'est l'éclairage du centre de l'enseigne. Sur DX, cette distinction n'existe pas : même si les signaux sont séparés, l'enseigne est toujours de la même couleur des deux côtés. Le plus simple est donc de **relier les broches `A2`, `A5` et `A8` du connecteur P1 aux broches `C3`, `C5` et `C8`**, pour que le centre prenne la même couleur que le côté joueur 1.

Deux méthodes sont possibles :

* **Avec la [PCB de conversion]({{IO4_CONVERSION_PCB}})**, si vous l'avez installée à l'[étape 3](step-3-io-board.md) : il suffit de brancher les LEDs sur les bons ports de la PCB.
* **Sans elle** : fabriquez votre propre nappe de câbles, compatible avec l'IO4, pour y raccorder les LEDs.

??? example "La méthode facile - La PCB de conversion"
    Branchez simplement le connecteur de sortie du contrôleur de LEDs sur la PCB de conversion, puis raccordez le 12V (**attention à la polarité**). C'est tout !

    !!! tip "Utilisez l'alimentation des LEDs"
        La borne dispose d'origine d'une alimentation 12V dédiée aux LEDs : utilisez-la pour alimenter la PCB. **Ne prenez pas le 12V de l'IO4**, et inversement, n'alimentez pas l'IO4 avec l'alimentation des LEDs. Les deux circuits doivent partager une masse commune, mais rester séparés.

    Il vous faudra une rallonge pour atteindre le câble existant : **2 mètres côté joueur 2, 3 mètres côté joueur 1**. Elle se sertit facilement : un connecteur `JST-XH 8 positions femelle` d'un côté, un `JST-SM 8 positions femelle` de l'autre.

    !!! lightbox
        ![PCB de conversion [maiConvert-IO4]({{IO4_CONVERSION_PCB}}) : repérage du connecteur J22 (`12V input`, attention à la polarité) et des connecteurs J23/J24 (`BILLBOARD LED L`/`R`) où raccorder la nappe de LEDs de l'enseigne lumineuse](../resources/images/step-6-lighting/led-inputs-and-12-on-convertion-pcb.jpg)
        ![Nappes de câbles en JST-SM 8 positions mâle, gérant les LEDs de l'enseigne lumineuse et des woofers, débranché du connecteur raccordé au contrôleur de LED sur une borne FiNALE](../resources/images/step-6-lighting/led-controller-rs232-disconnect.jpg)

    *Si vous comptez installer les caméras à l'étape suivante*, la PCB de conversion vous simplifiera aussi la vie : elle propose déjà des connecteurs prêts à l'emploi pour leurs LEDs.

??? example "La confection manuelle d'une nappe de câbles"
    La nappe se branche sur l'IO4 via un connecteur JST-RA 20 broches (CN9), et se termine par deux connecteurs JST-SM 8 broches, pour les côtés gauche et droit. Si vous avez suivi les suggestions de l'[étape 3](step-3-io-board.md), vous avez déjà un connecteur JST-SM 2 broches câblé sur le CN3 de l'IO4 pour les signaux `BILLBOARD LED L RED` et `BILLBOARD LED R RED`.

    !!! lightbox
        ![Repérage visuel des broches LED sur l'IO4 : le connecteur CN9 (JST-RA 20 broches) porte BILLBOARD LED L/R GREEN, CAMERA LED WARM/RED et BILLBOARD LED L/R BLUE, tandis que BILLBOARD LED L/R RED se trouve sur le connecteur CN3](../resources/images/step-6-lighting/io4-visual-reprensation-of-led-pins.png)
        ![Schéma de câblage officiel de l'IO4 centré sur les broches LED : connecteur CN9 (RA20P) pour BILLBOARD LED L/R GREEN, CAMERA LED WARM/RED et BILLBOARD LED L/R BLUE, et connecteur CN3 (RA60P) broches 51-52 pour BILLBOARD LED L/R RED](../resources/images/step-6-lighting/io4-wiring-schema-focused-on-leds.png)

    Réalisez la nappe d'après le schéma ci-dessous, avec une longueur suffisante pour une installation propre : **3 mètres côté joueur 1, 2 mètres côté joueur 2**. Pour le 12V, **n'utilisez pas la broche 12V du CN9** : raccordez-vous directement à l'alimentation 12V des LEDs de la borne, pour ne pas charger inutilement la carte I/O.

    ![Nappe de câbles pour l'éclairage de l'enseigne lumineuse : depuis l'IO4 (CN9 broches 5, 6, 9 et 10, et CN3 broches 51-52 déjà câblées à l'étape 3) et l'alimentation 12V interne, fabrication de deux connecteurs JST-SM 8 broches - côté P1 (3 mètres, avec pontage des broches 1-4 vers 5-8 pour alimenter aussi CENTER LED) et côté P2 (2 mètres, broches 5-8 non utilisées) - qui se branchent ensuite sur les connecteurs d'origine AB et BB](../resources/images/step-6-lighting/led-topper-harness.svg)

    Une fois la nappe terminée, branchez-la à l'IO4, raccordez le 12V, puis branchez les deux connecteurs JST-SM 8 broches d'origine sur votre nouveau câble. **Testez la continuité de tous vos câbles avant l'installation**, pour écarter toute broche mal sertie.

    !!! lightbox
        ![Nappes de câbles en JST-SM 8 positions mâle, gérant les LEDs de l'enseigne lumineuse et des woofers, débranché du connecteur raccordé au contrôleur de LED sur une borne FiNALE](../resources/images/step-6-lighting/led-controller-rs232-disconnect.jpg)

    !!! tip "Les LEDs des caméras"
        Si vous comptez installer les caméras optionnelles, sertissez dès maintenant quelques connecteurs supplémentaires :

        - JST-SM 2 broches sur les broches 7 et 8 du CN9, pour les signaux `CAMERA LED WARM` et `CAMERA LED RED` respectivement.
        - JST-SM 2 broches sur les broches 55 et 56 du CN3, pour les signaux `1P CODE READER LED` et `2P CODE READER LED` dans cet ordre.

## En résumé
!!! tldr "Les grandes lignes"
    Pour les LEDs des boutons et le fond de la borne :

    * Fabriquer deux proxys, chacun à base d'un Raspberry Pi Pico et d'un `Pico-2CH-RS232`.
    * Installer chaque proxy entre son contrôleur de LEDs et l'adaptateur RS-232 vers USB.
    * Brancher l'adaptateur sur le hub USB, et le hub sur le port USB n°2 du ALLS.

    Pour l'enseigne lumineuse et les woofers :

    * Soit : raccorder les connecteurs existants de la borne à la [PCB de conversion]({{IO4_CONVERSION_PCB}}).
    * Soit : confectionner et installer une nappe de câbles partant de l'IO4 et se branchant sur les connecteurs existants de la borne.

---

Dernière étape (optionnelle) : les [Caméras](step-7-cameras.md).
