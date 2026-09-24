---
title: "💳 4 - Lecteur Aime et VFD"
---

# 💳 Étape 4 : Le lecteur Aime et le VFD

**Les lecteurs Aime de FiNALE ne sont pas compatibles avec DX** : il faut installer un lecteur de nouvelle génération. Le VFD, lui, n'a aucune utilité réelle dans notre conversion, mais il reste nécessaire pour le logiciel. Bonne nouvelle : les deux sont très simples à installer.

## Explications techniques

??? note "Cliquez ici pour l'explication technique"
    FiNALE utilise deux lecteurs Aime d'ancienne génération, chaînés l'un à l'autre : celui du haut lit la carte du joueur de gauche, celui du bas celle du joueur de droite.

    Sur DX, il n'y a plus qu'**un seul lecteur**. Quand une carte est scannée, le profil apparaît sur les deux écrans : son propriétaire confirme la connexion sur son écran, puis le second joueur peut scanner sa propre carte. La technologie utilisée est complètement différente : **un lecteur Aime de FiNALE ne peut pas être réutilisé.**

    !!! info "aic_pico"
        Il est techniquement possible d'utiliser un [aic_pico]({{AIC_PICO_REPO}}), un projet open-source qui imite un véritable lecteur Aime de façon transparente pour le jeu. Il coûte beaucoup moins cher à produire, mais demanderait une bonne dose de bricolage pour être branché sur le port DB9 correspondant du ALLS.

    Les lecteurs Aime de dernière génération ne sont de toute façon pas si rares, et sont souvent vendus **en combo avec le VFD** dont nous avons également besoin. Cette génération est techniquement compatible avec le paiement électronique, mais même au Japon, cette fonction n'est presque jamais utilisée : les exploitants préfèrent installer leur propre terminal de paiement, plus flexible.

## La connectique

Le branchement au ALLS est extrêmement simple :

* Lecteur Aime : **COM1**
* VFD : **COM2**

Ces deux ports COM sont des ports DB9 physiques du ALLS. En revanche, votre combo Aime + VFD n'est probablement pas livré avec un câble DB9 prêt à brancher : **vous allez devoir sertir vos propres câbles**, du connecteur du lecteur Aime et du VFD jusqu'au DB9.

!!! lightbox
    ![Face avant d'un lecteur Aime issu d'une borne Star Horse 4](../resources/images/step-4-aime-reader/front-aime-reader-from-star-horse-4.jpg)
    ![Face arrière d'un lecteur Aime issu d'une borne Star Horse 4](../resources/images/step-4-aime-reader/back-aime-reader-from-star-horse-4.jpg)

### Préparer le câble DB9

Prenez votre câble DB9 femelle-femelle et **coupez-le en deux** pour en exposer les fils. Deux options :

* **Couper au milieu d'un câble long**, assez long une fois coupé pour aller proprement du ALLS jusqu'au centre de la borne, où sera installé le combo.
* **Couper à une vingtaine de centimètres** d'un connecteur, puis rejoindre le ALLS avec un simple câble DB9 mâle-femelle de longueur adaptée.

*La seconde option est recommandée* : pas de longueur de câble encombrante pendant le sertissage, une installation plus simple, et un combo plus facile à débrancher pour la maintenance.

!!! lightbox
    ![Câble DB9 femelle coupé, gaine retirée pour exposer les fils internes](../resources/images/step-4-aime-reader/cut-cable.jpg)

### Repérer les bons fils

Les couleurs des fils varient d'un câble DB9 à l'autre : ne vous fiez donc pas à celles des photos. **Le plus sûr est d'utiliser un multimètre en mode continuité** :

* Placez une pointe du multimètre dans le trou de la fiche DB9 femelle correspondant à la broche voulue (voir les schémas ci-dessous).
    * Si la pointe est trop large, raccordez-y un fil Dupont mâle.
* Avec l'autre pointe, touchez les fils un par un jusqu'au bip sonore. **Le fil qui sonne correspond à votre broche** : repérez-le.
* Une fois tous les fils utiles repérés (*3 pour le lecteur Aime, 5 pour le VFD*), coupez les autres.

### Câble du lecteur Aime

Le lecteur Aime est le plus simple des deux : **seules 5 de ses 8 broches sont utilisées**. Les 5 fils sont tous sertis avec des broches **JST-PH femelle** et insérés dans un connecteur **JST-PH 8 broches** :

1. **3 fils de signal** : ceux que vous avez repérés sur le câble DB9.
2. **2 fils d'alimentation "volants"** : un fil **rouge** sur la broche **5V** et un fil **noir** sur la broche **GND** juste à côté. Ils ne sont pas reliés au DB9 : laissez leur autre extrémité libre pour l'instant, elle sera réunie avec celle du VFD sur un seul connecteur (voir [Regrouper les fils d'alimentation](#regrouper-les-fils-dalimentation)).

![Correspondance des broches entre le connecteur JST-PH du lecteur Aime et le port DB9 femelle](../resources/images/step-4-aime-reader/aime-db9-jst-mapping.svg){ width="80%" }

!!! warning "Sertissez les deux GND"
    Deux des broches à sertir sont des GND (masse commune). Un seul suffirait en théorie, mais **câblez bien les deux** : l'un accompagne le 5V pour alimenter le lecteur, l'autre est relié au DB9 comme le veut la norme RS-232.

### Câble du VFD

Le VFD a un connecteur 7 broches, et **toutes doivent être serties**.

La méthode est presque identique à celle du lecteur Aime, à deux différences près :

* Le connecteur du VFD est un JST-**X**H (et non JST-PH) : sertissez les fils avec des broches **JST-XH femelle**.
* **5 fils de signal** au lieu de 3 : il faut aussi raccorder au port série les fils des signaux `CTS` et `RTS`.

Comme pour le lecteur Aime, ajoutez **2 fils d'alimentation volants**, rouge sur le **5V** et noir sur le **GND**, en laissant leur autre extrémité libre.

![Correspondance des broches entre le connecteur JST-XH du VFD et le port DB9 femelle](../resources/images/step-4-aime-reader/vfd-db9-jst-mapping.svg){ width="80%" }

### Regrouper les fils d'alimentation

Le lecteur Aime et le VFD ont maintenant chacun une paire de fils volants 5V/GND. **Réunissez-les en Y sur un seul connecteur JST-SM 2 broches** : les deux fils rouges (5V) ensemble sur une broche, les deux fils noirs (GND) ensemble sur l'autre. Placé à côté de vos deux câbles DB9, ce connecteur rend le combo plus simple à installer et à débrancher pour la maintenance.

Félicitations, vos câbles pour le ALLS sont prêts !

!!! lightbox
    ![Les deux câbles DB9 femelle finalisés, avec leurs connecteurs JST pour le lecteur Aime et le VFD](../resources/images/step-4-aime-reader/finished-cables.jpg)

### Sécuriser les câbles

Branchez les deux câbles sur les connecteurs correspondants, puis **fixez-les à l'arrière du combo** pour qu'ils ne subissent aucune tension. Même bien sertis, ces connecteurs restent fragiles.

!!! lightbox
    ![Les câbles branchés puis fixés à l'arrière du combo lecteur Aime + VFD pour éviter toute tension sur les connecteurs](../resources/images/step-4-aime-reader/cables-secured-behind-combo.jpg)

## Installation sur la borne

Utilisez [le modèle 3D conçu par SpiralGlide](spiralglide-resources.md#support-du-lecteur-aime), qui se fixe sur la borne grâce aux vis existantes de la vitre en acrylique. Conçu pour le lecteur Aime de Star Horse 4, il s'intègre **sans modification destructive**, en profitant des trous déjà prévus pour les lecteurs Aime. Il comprend aussi un emplacement pour les boutons 1P SELECT et 2P SELECT.

!!! lightbox
    ![Le support du lecteur Aime imprimé et monté dans la façade de la tour centrale, lecteur Aime en place. Photo par SpiralGlide](../resources/images/spiralglide-resources/maimai-aime-reader-installed.jpg)

## Dernière étape

Une fois le combo installé en façade, il ne reste qu'à brancher les deux câbles aux ports DB9 du ALLS. Pour rappel : **Aime sur COM1**, **VFD sur COM2**.

N'oubliez pas ensuite de **raccorder le 5V et le GND** des deux connecteurs à l'alimentation installée à l'[étape 1](step-1-alls-and-psu.md).

**Vérifiez que tout fonctionne** avant de passer à la suite.

## En résumé
!!! tldr "Les grandes lignes"
    Pour le lecteur Aime et le VFD :

    * Fabriquer un câble DB9 femelle pour le lecteur Aime.
    * Fabriquer un câble DB9 femelle pour le VFD.
    * Sécuriser les câbles pour qu'ils ne bougent pas.
    * Installer le combo en façade sur la borne.
    * Brancher les deux connecteurs sur le ALLS.
    * Raccorder l'alimentation.

---

Passons à l'[Étape 5 : Prises casques et Système Son](step-5-audio-headphones.md).
