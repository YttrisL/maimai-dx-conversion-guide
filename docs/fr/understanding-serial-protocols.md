---
title: "Les protocoles série"
---

# 🎓 Petit cours : comprendre les protocoles "série"

Ce guide mentionne plusieurs protocoles de communication : **UART**, **RS-232**, **RS-485**, **JVS** et **USB-CDC**. Si vous découvrez ces technologies, cette annexe vous explique à quoi ils servent, ce qui les distingue, et comment deux appareils parviennent à "se comprendre".

## 1. La base commune : parler "en série"

Un port "série" envoie les données **un bit à la fois, sur un seul fil**, à la queue leu leu (un port "parallèle", lui, utilise plusieurs fils en même temps). Chaque octet est emballé dans une petite trame, comme une lettre dans une enveloppe :

![Trame UART : bit Start, 8 bits de donnée D0 à D7, bit Stop, encadrés par la ligne au repos](../resources/images/serial-protocols/uart-framing.svg)

* Le bit **Start** prévient le récepteur qu'une lettre arrive.
* Les **8 bits suivants** sont le contenu.
* Le bit **Stop** referme l'enveloppe.

*Il existe des variantes avec plus ou moins de bits, mais "8 bits de donnée + 1 bit Stop" est de loin la plus courante.*

Ce découpage s'appelle une trame **UART** (*Universal Asynchronous Receiver-Transmitter*). À l'origine, UART désigne la puce qui fabrique ces trames, mais le terme désigne aussi, par extension, le découpage lui-même. Il vit au niveau d'une puce électronique (un microcontrôleur, par exemple), avec de petites tensions "logiques", souvent appelées **TTL** (*Transistor-to-Transistor Logic*) : 0V pour un "0", 3,3V ou 5V pour un "1".

**RS-232 et RS-485**, présentés juste après, sont simplement **deux façons de traduire électriquement ce même découpage**, pour l'envoyer sur un câble plus long ou plus fiable. Comme une même lettre confiée à deux services postaux différents : ce qui est écrit dessus ne change pas.

**Le rôle de "l'horloge" :** pour lire correctement une suite de bits, il faut savoir à quel instant précis regarder la ligne, comme un métronome qui bat la mesure pour des musiciens. En électronique, ce signal de cadencement s'appelle une **horloge** (*clock*). Rien à voir avec une pendule : c'est un signal qui répète "maintenant, maintenant..." à intervalle fixe, pour dire à chaque appareil de lire le bit suivant.

C'est justement le sens du "A" de UART, pour *Asynchronous* : **il n'y a pas de fil dédié à l'horloge**. Chaque appareil doit trouver le bon rythme tout seul, grâce à sa propre horloge interne, réglée à l'avance sur le débit convenu.

**Comment la communication s'établit :** les deux appareils doivent donc s'accorder à l'avance sur cette vitesse : c'est le fameux **débit en bauds** (par exemple, "9600 bauds" = 9 600 bits par seconde). **Aucune négociation n'a lieu sur le fil** : si les deux bouts ne sont pas réglés sur la même vitesse, chacun lit le mauvais bit au mauvais moment. C'est une convention fixée d'avance, pas une poignée de main.

## 2. RS-232 : le point à point

RS-232 traduit ce découpage UART en **tensions plus élevées et inversées** : typiquement entre -15V et +15V, souvent ±5 à ±12V en pratique. Un "1" logique devient une tension négative, un "0" une tension positive. Cela permet d'utiliser des câbles plus longs qu'avec les faibles 3,3V/5V d'un UART brut. RS-232 ne relie que **deux appareils**, chacun avec son propre fil d'émission :

![RS-232 : liaison point à point entre deux appareils, TX croisé avec RX, GND relié à GND](../resources/images/serial-protocols/rs232-point-to-point.svg){ width="65%" }

Le **TX** (émission) d'un côté se branche sur le **RX** (réception) de l'autre : c'est ce croisement que réalise un [adaptateur Null Modem](glossary.md#communication-et-protocoles). RS-232 ne se limite d'ailleurs pas aux tensions : la norme définit aussi le connecteur (le fameux port "DB9") et quelques fils de contrôle supplémentaires, ce qui rend justement ce genre de câble croisé possible.

Dans ce guide, **RS-232 est le protocole utilisé par le jeu** pour :

* piloter les [contrôleurs de LEDs](step-6-lighting.md) ;
* dialoguer avec les dalles tactiles *d'origine* ;
* récupérer les informations du lecteur Aime et dire au VFD quoi afficher.

C'est un standard très répandu dans le milieu de l'arcade.

**Le connecteur DB9 :** ce petit connecteur trapézoïdal à 9 broches sur deux rangées, que RS-232 a rendu quasi universel, est souvent confondu à tort avec un port VGA "inversé". On le retrouve sur le RingEdge 2 comme sur le ALLS. Sur les 9 broches, **seules trois nous intéressent vraiment** :

* **TX** : émission ;
* **RX** : réception ;
* **GND** : la masse, la référence commune de tension.

Les autres broches (DTR, DSR, RTS, CTS, DCD, RI) transportent des signaux de contrôle optionnels (contrôle de flux, détection de porteuse...), rarement utilisés en arcade. *Le VFD fait exception : il utilise aussi `RTS` et `CTS` (voir l'[étape 4](step-4-aime-reader.md)).*

![Connecteur DB9 mâle, vue de face, avec les broches 2 (RX), 3 (TX) et 5 (GND) mises en évidence](../resources/images/serial-protocols/db9-connector.svg){ width="65%" }

Un connecteur **femelle** porte les mêmes numéros de broches, mais en creux plutôt qu'en pointes, et en miroir horizontal. C'est pourquoi un câble croisé (Null Modem) doit explicitement **inverser les broches 2 et 3** d'un bout à l'autre. Brancher deux appareils "en direct" (broche 2 sur broche 2, broche 3 sur broche 3) relierait deux TX ensemble et deux RX ensemble, ce qui ne fonctionne pas : **le TX d'un appareil doit toujours aller sur le RX de l'autre**, et inversement.

## 3. RS-485 : le bus à plusieurs

RS-485 traduit lui aussi le découpage UART, mais avec une autre astuce. Au lieu d'un fil "haut/bas" mesuré par rapport à la masse, il utilise une **paire différentielle** : deux fils, A et B, dont on compare la tension *entre eux*, à des niveaux proches du TTL de départ.

Deux avantages :

* **une bien meilleure résistance aux parasites** sur de longs câbles ;
* surtout, **plusieurs appareils peuvent partager la même paire de fils** :

![RS-485 : bus partagé sur une paire différentielle A/B, avec l'hôte (maître) et deux nœuds (esclaves) raccordés aux mêmes fils](../resources/images/serial-protocols/rs485-bus.svg){ width="80%" }

En revanche, RS-485 ne dit rien de **qui a le droit de parler, et quand** : sans règle, les appareils parleraient en même temps et leurs signaux se mélangeraient. C'est le protocole du dessus qui fixe cette règle. Cette capacité à chaîner plusieurs appareils sur deux fils en fait le support idéal du JVS (voir point suivant).

## 4. JVS : un protocole construit par-dessus RS-485

Attention à ne pas confondre les niveaux : **RS-485 ne définit que l'aspect électrique** (comment les bits voyagent sur le fil). **JVS est une couche au-dessus**, qui définit un langage commun (adressage, commandes) pour que le jeu et la carte I/O se comprennent.

**Le lien avec l'UART du point 1 :** JVS ne réinvente pas la façon d'envoyer les bits. Il utilise **exactement les mêmes trames UART** (Start / 8 bits de données / Stop), simplement transportées en RS-485. Ce que JVS ajoute, c'est une convention sur le *contenu* de ces octets. Un paquet JVS contient toujours, dans l'ordre :

1. un octet de synchronisation ;
2. un octet d'adresse, qui désigne le destinataire ;
3. une longueur ;
4. les données de la commande ;
5. une somme de contrôle, pour détecter les erreurs.

Le jeu et la carte I/O échangent donc de simples octets UART, comme n'importe quel appareil série : c'est en interprétant leur contenu selon les règles JVS que les deux bouts se comprennent.

![Pile de couches JVS : JVS (protocole, contenu des octets) transporté en trames UART (framing, forme des octets), elles-mêmes transportées électriquement en RS-485](../resources/images/serial-protocols/jvs-layers.svg){ width="80%" }

**Comment la communication s'établit :**

1. Au démarrage, le jeu (l'hôte) envoie une **commande de réinitialisation** à tous les appareils du bus en même temps.
2. Il demande ensuite, toujours à tous : "qui n'a pas encore d'adresse ? Réponds-moi". Un fil supplémentaire, câblé en chaîne d'un appareil au suivant, n'autorise qu'un seul appareil à la fois à répondre. L'hôte attribue ainsi **une adresse à chaque appareil, un par un** : c'est l'auto-adressage JVS.
3. Une fois les adresses distribuées, l'hôte **interroge chaque carte à tour de rôle** ("du nouveau ?").

C'est un dialogue **maître/esclaves** : seul l'hôte prend l'initiative. Dans un système d'arcade, c'est typiquement la carte I/O qui parle JVS. Malgré son câble USB, elle communique en réalité toujours via une liaison série RS-485 sous le capot.

## 5. USB-CDC : le déguisement

L'USB est une tout autre famille de protocole : **par paquets, bien plus rapide, et négocié**. À la connexion, l'appareil se présente à l'ordinateur et décrit lui-même ses capacités : c'est "l'énumération USB".

La classe **CDC** (*Communication Device Class*) est un cas particulier : l'appareil dit à l'ordinateur *"traite-moi comme un port RS-232"*. L'ordinateur crée alors un **port COM virtuel**, mais le transport réel reste de l'USB par paquets :

![USB-CDC : la dalle tactile ADX envoie des paquets USB se présentant comme un port série, l'ordinateur les expose comme un port COM virtuel](../resources/images/serial-protocols/usb-cdc.svg){ width="80%" }

C'est pratique pour la compatibilité : un programme qui ne sait parler qu'en RS-232 fonctionne sans modification.

Mais attention : **le débit affiché n'est qu'une façade**. Le port COM virtuel annonce par exemple "9600 bauds", mais le matériel USB derrière continue d'envoyer ses données à pleine vitesse. Le déguisement ne crée donc pas lui-même de goulot d'étranglement : celui-ci apparaît quand ces données rapides doivent être renvoyées vers un appareil *réellement* limité à 9600 bauds, comme le jeu, plus loin dans la chaîne. C'est l'un des problèmes rencontrés avec les dalles tactiles ADX, une alternative mentionnée dans la [Liste de courses](equipment.md).

## Résumé express

| Protocole | Couche | Topologie | Établissement de la liaison |
|---|---|---|---|
| UART | Framing + logique (TTL, 3,3V ou 5V) | Point à point (avant tout support électrique) | Débit en bauds fixé à l'avance des deux côtés : la base commune à tout ce qui suit |
| RS-232 | Électrique + connecteur (traduit l'UART) | Point à point (2 appareils) | Comme l'UART, simplement porté en tensions plus élevées |
| RS-485 | Électrique (traduit l'UART) | Bus (plusieurs appareils) | Comme l'UART ; ne gère ni adresses ni tour de parole, c'est le rôle du protocole du dessus (ex. JVS) |
| JVS | Protocole (au-dessus de l'UART, transporté en RS-485) | Chaîne maître/esclaves | L'hôte réinitialise le bus, puis distribue les adresses une par une au démarrage |
| USB-CDC | Protocole (au-dessus de l'USB) | Point à point | Négocié à la connexion (USB), puis déguisé en port série |

---
