---
title: "🧠 5 - Compatibilité via Proxy"
---

# 🧠 Étape 5 : Compatibilité avec le système d'origine via le Proxy

C'est l'étape la plus complexe et la plus importante de ce guide. Comme expliqué plus tôt, nous souhaitons une fidélité logicielle totale. Toutefois, comme l'interface de communication des dalles tactiles ADX diffère des dalles officielles d'une borne *DX*, nous ne pouvons pas simplement les connecter via un port USB. Nous devons les adapter.

**Le problème matériel :** Le logiciel du jeu exige que les dalles tactiles communiquent via un port "série". Précisément, via la norme RS-232, en 9600 bauds. Cependant, les dalles tactiles ADX envoient leurs données via USB, dans un format et avec des timings totalement différents.
Même si on utilise des adaptateurs USB, brancher les ADX directement sur le PC fera planter le jeu, car celui-ci ne comprend pas les informations encodées de cette façon.

## La Solution : Le Raspberry Pi comme traducteur

Pour tromper le jeu, nous allons placer un mini-ordinateur (un **Raspberry Pi 5**) entre les dalles ADX et le PC *ALLS*. Ce Raspberry Pi va exécuter un petit programme qui agira comme un **traducteur intelligent et un régulateur de vitesse**.

* **Il met en attente** les commandes lentes envoyées par le PC et les donne aux écrans en un seul bloc compréhensible.
* **Il absorbe** le torrent de données très rapides envoyées par les ADX via USB.
* **Il fait le tri** et n'envoie au PC **que la position du doigt la plus récente**, à une vitesse que la norme série peut supporter, évitant ainsi tout plantage.

## Mise en place du Proxy (Pour utilisateurs familiers avec Linux)

1. Branchez les câbles USB de vos ADX sur les ports du Raspberry Pi (le Pi 5 a suffisamment de ports, pas besoin de Hub USB).
2. Reliez le Raspberry Pi aux ports du ALLS via les adaptateurs "USB-to-Serial" (puces FTDI) pour simuler la connexion lente attendue par le jeu.
3. **Sous Linux (sur le Raspberry Pi) :** Vous devez configurer le système pour que les ports USB gardent toujours le même nom (création de règles *udev* et de *symlinks*). Ainsi, même si vous redémarrez, le câble du joueur 1 s'appellera toujours "P1-TOUCH".
4. Installez sur le Raspberry Pi un programme capable de faire ce travail de traduction (mise en tampon des commandes lentes, filtrage des positions du doigt), et compilez-le si nécessaire.
5. Testez la liaison en lançant manuellement le programme. Si l'ADX répond, le pont fonctionne !
6. Créez un service `systemd` dans Linux. Cela permettra à ce programme de traduction de se lancer automatiquement et de manière invisible en arrière-plan à chaque fois que vous allumez la borne.

---

Passons à l'[Étape 6 : Prises casques et Système Son](step-6-audio-headphones.md).
