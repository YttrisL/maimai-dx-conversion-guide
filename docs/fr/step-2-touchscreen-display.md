---
title: "📺 2 - Écrans et dalles tactiles"
---

# 📺 Étape 2 : L'Affichage et les Dalles Tactiles HDX

Commençons par installer l'affichage et les dalles tactiles.

## Les connexions vidéo

Le jeu est programmé pour envoyer la vidéo d'une manière bien précise aux deux écrans. L'ordre doit être respecté. *(Référence : [Manuel](../resources/pdfs/maimai-dx-manual-full.pdf) officiel de la borne DX, page 128)*

* **Joueur 1 (P1) :** Doit être branché sur le port **DisplayPort** (Attention : le [manuel](../resources/pdfs/maimai-dx-manual-full.pdf) officiel comporte une erreur et indique HDMI à tort).
* **Joueur 2 (P2) :** Doit être branché sur le port **DVI**.

*(Le port HDMI restant sur la carte graphique peut être utilisé pour brancher du matériel de capture vidéo, toutefois celui-ci ne propose que la sortie du joueur 1)*.

Il existe toutefois une légère différence native entre les écrans d'une *FiNALE* et d'une *DX*. Dans les deux cas, il s'agit d'écrans 1920x1080 cadencés à 60 Hz, mais les écrans de *FiNALE* mesurent 42" de diagonale, alors que les écrans de *DX* mesurent 43". La différence est pratiquement imperceptible en jeu.

## Les dalles tactiles HDX

Retirez les anciennes dalles tactiles de la borne *FiNALE* (maintenues par 8 vis) et installez les nouvelles dalles HDX.
Il faut ensuite raccorder les dalles aux bonnes "adresses" (Ports COM) sur le ALLS, sinon le jeu confondra les deux joueurs : *([Manuel](../resources/pdfs/maimai-dx-manual-full.pdf), page 128)*

* **Joueur 1 :** Doit être branché au Port **COM3**.
* **Joueur 2 :** Doit être branché au Port **COM4**.

Contrairement à d'autres kits de conversion, la carte I/O HanDevice fournie avec les dalles HDX expose directement un port série UART. Vous pouvez donc la raccorder directement au ALLS, sans transformation de signal ni Raspberry Pi intermédiaire - voir la [Liste de courses](equipment.md) pour le détail de cette carte I/O.

---

Passons à l'[Étape 3 : La Carte I/O et les Boutons](step-3-io-board.md).
