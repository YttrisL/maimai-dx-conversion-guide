---
title: "💡 6 - Lumières (Optionnel)"
---

# 💡 Étape 6 : Lumières (Optionnel)

À ce stade, le jeu devrait être totalement jouable, mais l'éclairage esthétique de la borne n'est pas encore fonctionnel.
Sur *DX*, il y a trois contrôleurs différents qui gèrent l'éclairage de la borne :

* L'IO4 gère l'éclairage du "Billboard", le sommet de la borne. Référez-vous à l'[Étape 3](step-3-io-board.md) (point 3) pour savoir quelles broches utiliser.
* Deux cartes de contrôle identiques :
  * Une gère les LEDs des huit boutons du P1, l'éclairage du côté gauche, l'éclairage de l'anneau central de gauche et l'éclairage du fond de gauche.
  * L'autre gère les LEDs des huit boutons du P2, l'éclairage du côté droit, l'éclairage de l'anneau central de droite et l'éclairage du fond de droite.

Les deux cartes de contrôle s'interfacent en norme série RS-232 à une unique PCB convertissant les deux signaux RS-232 en USB. Cette PCB est elle-même raccordée à la même multiprise USB (Hub) que les caméras lecteurs de QR-Code (voir [Étape 7](step-7-cameras.md)).
Les ports COM logiciels sur lesquels les contrôleurs de LEDs sont interfacés sont le **COM21** pour les LEDs du P1 et le **COM23** pour les LEDs du P2.

Dans le cas d'une borne convertie, toutefois, les choses sont un peu plus compliquées.

Il est théoriquement possible de réutiliser les contrôleurs de LEDs d'une borne *FiNALE*, toutefois ceci s'accompagne de plusieurs inconvénients.

- Le numéro de série de la PCB ne correspond pas à ce que *DX* s'attend à trouver, cela provoquera ainsi un avertissement ("warning") au démarrage de la borne. Cela dit, le contrôleur fonctionnera tout de même.
- En cas de "warning", le jeu n'envoie simplement pas les données permettant d'éclairer l'anneau central (à ne pas confondre avec les boutons) et le corps de la borne (les données FET).

Les contrôleurs de LEDs de *FiNALE* s'interfacent de la même manière que ceux de *DX*, en passant par une carte de traduction intermédiaire convertissant le RS-232 des deux cartes en une unique connexion USB.
Les références sont les suivantes :

- *FiNALE* - Contrôleur LED : `837-15070-02-91 IC BD LED DRV32CH RS232` (Identique pour les deux joueurs)
- *FiNALE* - Convertisseur Serial-USB intermédiaire : `837-15067-02 IC BD USB TO 4SERIAL 232 IF`

Dans [le manuel de maimai *PiNK*](../resources/pdfs/maimai-pink-manual-full.pdf), on peut retrouver le contrôleur de LED à la page 192, et le convertisseur Serial-USB à la page 191 aux alentours de la zone FG-2.

Pour contourner le problème des avertissements sans avoir besoin de changer le contrôleur des LEDs, nous pouvons utiliser une astuce de [Proxy](glossary.md#informatique-et-linux) : un petit ordinateur qui s'interpose entre deux appareils pour adapter leurs échanges à la volée, sans que ni l'un ni l'autre ne s'en aperçoive. À l'aide d'un Raspberry Pi 5 [et du logiciel `mailight_rs` (écrit en langage Rust)](https://gitea.farewell.dev/Yttris/mailight_rs), nous pouvons interfacer le contrôleur des LEDs avant la carte de traduction USB-Serial pour l'envoyer à notre proxy. Ce dernier s'occupera d'adapter le signal en modifiant les en-têtes pour fournir au jeu un signal lui faisant croire qu'il s'agit des bonnes PCB, il retournera ainsi un signal "GOOD" à la place du "warning". Le Raspberry Pi se placera alors entre les PCBs de contrôle des LEDs et le convertisseur serial USB, qui pourra lui être directement branché au ALLS sur le port dédié au Hub USB, ou au Hub USB lui-même si des lecteurs de QR-Code sont également installés.

---

Dernière étape (optionnelle) : les [Caméras](step-7-cameras.md).
