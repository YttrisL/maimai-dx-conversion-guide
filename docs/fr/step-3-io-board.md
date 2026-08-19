---
title: "🔌 3 - Carte I/O et boutons"
---

# 🔌 Étape 3 : La Carte I/O et les Boutons

Pour faire tourner *DX*, il est nécessaire de remplacer l'ancienne carte I/O par le nouveau modèle **IO4**. Heureusement, le câblage reste globalement le même, à quelques exceptions près.

*(Note : Le détail complet du câblage de la carte IO4 se trouve à la page 194 du [manuel](resources/pdfs/maimai-dx-manual-full.pdf), en bas à droite)*

## 1. Le Bloqueur de Pièces (Coin Locker)

La broche (pin) correspondant au bloqueur de pièces a été déplacée au passage à l'IO4. Sur une borne *FiNALE*, il était câblé sur la broche 51.

1. Sur le gros faisceau de câbles anciennement raccordé à l'IO3, repérez la broche **51**.
2. Déplacez ce fil vers la broche **53**.

## 2. L'ajout des boutons "Select"

Sur *DX*, de nouveaux boutons physiques sont apparus pour permettre aux joueurs de trier les chansons. Vous devez les câbler manuellement :

1. Vous devez installer vos boutons sur le panneau central de votre borne, idéalement via la confection d'un boîtier personnalisé pour éviter une modification destructrice de la coque.
2. Connectez une broche de chaque bouton sur le neutre du faisceau de câbles (broches de 9 à 16).
3. Connectez l'autre broche du bouton sur la broche de la nappe correspondante :
   * "1P SELECT BUTTON" : Broche **27**
   * "2P SELECT BUTTON" : Broche **26**

## 3. Le contrôle des LEDs du Billboard (Toit de la borne)

Sur *DX*, l'IO4 est responsable de la gestion des lumières du sommet de la borne. Ce point sera également abordé à l'[Étape 7](step-7-lighting.md), mais voici déjà le schéma (pinout) des LEDs à raccorder :

* "BILLBOARD LED L RED" : Connecteur **CN3** - Broche **51** (Le gros faisceau de câbles)
* "BILLBOARD LED R RED" : Connecteur **CN3** - Broche **52** (Le gros faisceau de câbles)
* "BILLBOARD LED L GREEN" : Connecteur **CN9** - Broche **5**
* "BILLBOARD LED R GREEN" : Connecteur **CN9** - Broche **6**
* "BILLBOARD LED L BLUE" : Connecteur **CN9** - Broche **9**
* "BILLBOARD LED R BLUE" : Connecteur **CN9** - Broche **10**

Si vous ne souhaitez pas installer les LEDs du dessus de la borne, vous pouvez ignorer cette étape.

## 4. Branchement USB de la carte IO4

La nouvelle carte IO4 communique avec le PC *ALLS* via un simple câble USB. Cependant, **le choix du port USB sur l'ordinateur est défini dans le [manuel](resources/pdfs/maimai-dx-manual-full.pdf)** *(Voir page 128 du manuel)*. Si vous regardez le PC *ALLS* posé à plat (à l'horizontale), vous devez brancher le câble de l'IO4 sur le port USB situé **en bas à gauche**.

---

Passons à l'[Étape 4 : Le Lecteur de Cartes Aime](step-4-aime-reader.md).
