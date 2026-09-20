---
title: "🛠️ 1 - ALLS et PSU"
---

# 🛠️ Étape 1 : Le Remplacement du PC Central (ALLS)

--8<-- "includes/wip-fr.md"

L'ancien PC *RingEdge 2* n'est pas assez puissant pour faire tourner *DX*. Vous avez besoin d'un PC **ALLS HX2**.
Alternativement, il est souvent plus simple (et moins cher) de trouver des PC **ALLS MX2**, et ceux-ci peuvent être modifiés (downgrade) pour correspondre exactement aux spécifications d'un HX2.

* **Stockage :** Le HX2 vient de base avec un SSD de 128 Go et un disque dur de 512 Go. Pour une installation sur serveur privé, ces disques suffisent.

Voici la planche du manuel officiel *SEGA* qui détaille l'ensemble de la connectique à l'arrière d'un ALLS HX2, utile pour repérer chaque prise avant de reprendre le câblage d'origine du *RingEdge 2* :

[![Vue arrière d'un ALLS HX2 et détail de sa connectique : 4 connecteurs D-SUB9P/stéréo mini-jack [SIDE] en haut, 2 connecteurs HDMI/DVI, 3 connecteurs stéréo mini-jack [C/W] [FRONT] [REAR], 5 connecteurs LAN/USB [IO]/[USB HUB]/[P CAMERA]/[INSTALL], 1 connecteur D-SUB9P [COM1] et le connecteur secteur en bas](../resources/images/step-1-alls-and-psu/alls-hx2-rear-connectors-fr.jpg)](../resources/images/step-1-alls-and-psu/alls-hx2-rear-connectors-fr.jpg)
_(Planche extraite du [manuel officiel maimai DX](../resources/pdfs/maimai-dx-instruction-manual-full.pdf), page 128.)_

!!! warning "Alimentation"
    L'alimentation interne du *RingEdge 2* fournissait directement les tensions nécessaires à différents composants de la borne *FiNALE*. Le connecteur molex en façade du *RingEdge 2* fournit au reste de la borne du 12v, du 5v et du 3,3v. Le nouveau PC *ALLS* ne possède pas ces connecteurs d'alimentation similaires. **La solution idéale** est d'ajouter une petite alimentation secondaire (arcade PSU) distincte de celle du PC *ALLS* pour alimenter les PCBs et les lumières. Une alimentation 12v/5v sera suffisante, aucun composant de la borne *FiNALE* n'exploite le 3,3v.

---

Passons à l'[Étape 2 : Affichage et dalles tactiles HDX](step-2-touchscreen-display.md).
