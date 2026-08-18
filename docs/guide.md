# Guide Complet : Projet "DxNALE"

## Convertir une borne maimai Finale en maimai DX

Bienvenue dans le guide détaillé de conversion matérielle d'une borne d'arcade **maimai Finale** vers le système **maimai DX**. Ce document est basé sur les notes de conversion de la communauté et a été enrichi pour être accessible même si vous n'êtes pas un ingénieur en électronique.

### Contexte : Pourquoi ce guide ?

Le matériel entre *maimai Finale* et *maimai DX* a radicalement changé. Le PC central est différent, et surtout, la dalle tactile ne fonctionne plus du tout de la même manière. Officiellement, ces bornes sont incompatibles.

**L'objectif final : Une fidélité logicielle parfaite**

Il est parfaitement possible de modifier les données du jeu afin de pouvoir rendre compatible n'importe quelle dalle tactile produite par la communauté, toutefois nous visons ici une fidélité logicielle totale. Aucune modification logicielle du jeu n'est tolérée. Le jeu doit "penser" qu'il tourne sur une borne originale Sega. Par conséquent, toute notre adaptation matérielle (via des mini-ordinateurs et des traducteurs) doit être invisible pour le jeu.

---

## 🛒 Liste de courses : Le matériel nécessaire

Avant de commencer, voici la liste des composants à acquérir pour réaliser cette conversion :

**Matériel Obligatoire :**

* Un PC ALLS HX2 (ou un MX2 modifié).
* Une carte I/O Sega IO4.
* Deux dalles tactiles ADX.
* Un lecteur Aime de 3ème génération (référence de la pièce : 610-0955).
* Un câble DisplayPort (ou DisplayPort vers DVI) et un câble DVI-D pour les écrans.
* Deux petits amplificateurs audio pour gérer les prises casques.

**Pour le Proxy ("Traduction" des données) :**

* Deux Raspberry Pi 5 avec leur bloc d'alimentation.
* Deux adaptateurs "USB-to-Serial" avec puces FTDI (prévoyez-en 6 si vous gérez le tactile **et** les LEDs via proxy).
* Deuxs adaptateurs "Null Modem" pour faire correspondre les fiches mâle-femelle des adaptateurs "USB-to-Serial. à la connectique du ALLS.

**Matériel Optionnel (Son, Caméras, Finitions) :**

* Une webcam classique et bon marché pour la caméra du joueur.
* Deux webcams au format strict UVC 640x480 pour les lecteurs de QR-Code.
* Un Hub USB (de préférence avec sa propre alimentation).

---

## ⚠️ Avertissements et Considérations

Avant de vous lancer, voici la réalité du projet :

* **C'est coûteux :** Comptez entre 3000€ et 4000€ en plus du prix de la borne de base pour les pièces (Écrans tactiles ADX, PC ALLS, Raspberry Pi, câblages, etc.).
* **C'est complexe et long :** Il faut savoir lire un schéma de câblage, dénuder/sertir des fils, et utiliser Linux. Prévoyez au moins une semaine complète de travail acharné.
* **C'est quasi-irréversible :** Revenir en arrière (vers *Finale*) sera extrêmement fastidieux.
* **Testez avant :** Assurez-vous que votre borne *Finale* fonctionne parfaitement avant de commencer. Cela vous évitera de chercher des pannes imaginaires plus tard.

---

## 📖 Petit Lexique pour les Débutants

Pour ne pas être perdu dans les termes techniques :

* **ALLS (MX2 / HX2) :** C'est le nom de l'ordinateur standard utilisé par Sega pour faire tourner les jeux récents. Il remplace l'ancien PC de Finale (nommé Ringedge 2).
* **Carte I/O (Input/Output) :** C'est la carte électronique qui fait le lien entre le PC et la borne. Elle capte l'appui sur les boutons. Dans le cas de *maimai Finale*, il s'agit d'une **Sega IO3**. Pour *DX*, elle doit être remplacée par une **Sega IO4**.
* **Ports COM (COM1, COM3...) :** Ce sont les "adresses" (ou canaux) virtuelles par lesquelles le PC communique avec certains périphériques spécifiques (comme les dalles tactiles ou le lecteur de carte *Aime*). Aujourd'hui, la plupart des connexions sur Port COM se font via des ports virtuel, toutefois un ALLS HX2 dispose de quatre connexion physiques pour y connecter le matériel de la borne.
* **Aime / VFD :** Le lecteur de cartes sans contact (NFC) utilisé par les joueurs pour sauvegarder leur profil. Le *VFD* (Vacuum Fluorescent Display) est le petit écran à affichage rétro (souvent vert ou bleu) qui affiche le solde d'argent ou d'autres informations textuelles.

---

## 🛠️ Étape 1 : Le Remplacement du PC Central (ALLS)

L'ancien PC *Ringedge 2* n'est pas assez puissant pour faire tourner *DX*. Vous avez besoin d'un PC **ALLS HX2**.
Alternativement, il est souvent plus simple (et moins cher) de trouver des PC **ALLS MX2**, et ceux-ci peuvent être modifiés (downgrade) pour correspondre exactement aux spécifications d'un HX2.

* **Stockage :** Le HX2 vient de base avec un SSD de 128 Go et un disque dur de 512 Go. Pour une installation sur serveur privé, ces disques suffisent.
* **Alimentation (Attention) :** L'alimentation interne du *Ringedge 2* fournissait directement les tensions nécessaires à différents composants de la borne *Finale*. Le connecteur molex en façade du *Ringedge 2* fournit au reste de la borne du 12v, du 5v et du 3,3v. Le nouveau PC *ALLS* ne possède pas ces connecteurs d'alimentation similaire. **La solution idéale** est d'ajouter une petite alimentation secondaire (arcade PSU) distincte de celle du PC *ALLS* pour alimenter les PCBs et les lumières. Une alimentation 12v/5v sera suffisante, aucun composant de la borne *Finale* n'exploite le 3,3v.

---

## 📺 Étape 2 : L'Affichage et les Dalles Tactiles ADX

Toute la complexité réside au niveau de la connexion des dalles tactiles ADX, mais dans un premier temps, commençons par les installer.

### Les connexions vidéo

Le jeu est programmé pour envoyer la vidéo d'une manière bien précise aux deux écrans. L'ordre doit être respecté. *(Référence : [Manuel](maimaiDX-Manual.pdf) officiel de la borne DX, page 128)*

* **Joueur 1 (P1) :** Doit être branché sur le port **DisplayPort** (Attention : le [manuel](maimaiDX-Manual.pdf) officiel comporte une erreur et indique HDMI à tort).
* **Joueur 2 (P2) :** Doit être branché sur le port **DVI**.

*(Le port HDMI restant sur la carte graphique peut être utilisé par pour brancher du matériel de capture vidéo, toutefois celui-ci ne propose que la sortie du joueur 1)*.

Il existe toutefois une légère différence native entre les écrans d'une *Finale* et d'une *DX*. Dans les deux cas, il s'agit d'écrans 1920x1080 cadensé à 60hz, mais les écrans de *Finale* mesurent 42" de diagnonale, alors que les écrans de *DX* mesurent 43". La différence est partiquement imperceptible en jeu.

### Les dalles tactiles ADX

Retirez les anciennes dalles tactiles de la borne *Finale* (maintenue par 8 vis) et installez les nouvelles dalles ADX.
Il faut ensuite raccorder les dalles aux bonnes "adresses" (Ports COM) sur le ALLS, sinon le jeu confondra les deux joueurs : *([Manuel](maimaiDX-Manual.pdf), page 128)*

* **Joueur 1 :** Doit être branché au Port **COM3**.
* **Joueur 2 :** Doit être branché au Port **COM4**.

En l'état, la connexion fournie par les dalles ADX se fait via USB-CDC, ce qui ne correspond pas aux raccordements souhaités sur le ALLS. Laissez les câbles USB des deux ADX débranchés pour le moment. Nous les connecterons au Raspberry Pi à l'étape 5 pour assurer la compatibilité totale avec le système d'origine.

---

## 🔌 Étape 3 : La Carte I/O et les Boutons

Pour faire tourner *DX*, il est nécessaire de remplacer l'ancienne carte I/O par le nouveau modèle **IO4**. Heureusement, le câblage reste globalement le même, à quelques exceptions près.

*(Note : Le détail complet du câblage de la carte IO4 se trouve à la page 194 du [manuel](maimaiDX-Manual.pdf), en bas à droite)*

### 1. Le Bloqueur de Pièces (Coin Locker) :

La broche (pin) correspondant au bloqueur de pièces a été déplacée au passage à l'IO4. Sur une borne *Finale*, il était câblé sur la broche 51.

1. Sur le gros faisceau de câbles anciennement raccordé à l'IO3, repérez la broche **51**.
2. Déplacez ce fil vers la broche **53**.

### 2. L'ajout des boutons "Select" :

Sur *DX*, de nouveaux boutons physiques sont apparus pour permettre aux joueurs de trier les chansons. Vous devez les câbler manuellement :

1. Vous devez installer vos boutons sur le panneau central de votre borne, idéalement via la confection d'un boîtier personnalisé pour éviter une modification destructrice de la coque.
2. Connectez une broche de chaque bouton sur le neutre du faisceau de câbles (broches de 9 à 16).
3. Connectez l'autre broche du bouton sur la broche de la nappe correspondante :
   * "1P SELECT BUTTON" : Broche **27**
   * "2P SELECT BUTTON" : Broche **26**

### 3. Le contrôle des LEDs du Billboard (Toit de la borne) :

Sur *DX*, l'IO4 est responsable de la gestion des lumières du sommet de la borne. Ce point sera également abordé à l'étape 7, mais voici déjà le schéma (pinout) des LEDs à raccorder :

* "BILLBOARD LED L RED" : Connecteur **CN3** - Broche **51** (Le gros faisceau de câbles)
* "BILLBOARD LED R RED" : Connecteur **CN3** - Broche **52** (Le gros faisceau de câbles)
* "BILLBOARD LED L GREEN" : Connecteur **CN9** - Broche **5**
* "BILLBOARD LED R GREEN" : Connecteur **CN9** - Broche **6**
* "BILLBOARD LED L BLUE" : Connecteur **CN9** - Broche **9**
* "BILLBOARD LED R BLUE" : Connecteur **CN9** - Broche **10**

Si vous ne souhaitez pas installer les LEDs du dessus de la borne, vous pouvez ignorer cette étape.

### 4. Branchement USB de la carte IO4 :

La nouvelle carte IO4 communique avec le PC *ALLS* via un simple câble USB. Cependant, **le choix du port USB sur l'ordinateur est définit dans le [manuel](maimaiDX-Manual.pdf)** *(Voir page 128 du manuel)*. Si vous regardez le PC *ALLS* posé à plat (à l'horizontale), vous devez brancher le câble de l'IO4 sur le port USB situé **en bas à gauche**.

---

## 💳 Étape 4 : Le Lecteur de Cartes Aime

Les anciens lecteurs de cartes de la *Finale* sont obsolètes et ne fonctionneront pas avec *DX*.

1. Vous devez vous procurer un lecteur Aime moderne (Génération 3, numéro de pièce : **610-0955**).
2. Installez-le sur le panneau central de la borne, de préférence via une impression 3D pour réaliser une installation non-destructrice.
3. **Bonne nouvelle :** L'ordre des fils (pinout) sur le connecteur est presque identique à l'ancien modèle. Vous pouvez réutiliser les câbles de communication de l'ancien lecteur sans avoir à tout recâbler.
4. **Adresses et Branchement :**
   * Le lecteur Aime doit être branché au port **COM1**.
   * Le petit écran texte (VFD) doit être raccordé au port **COM2**.
   * Vous pouvez récupérer du courant 5V sur les anciens câbles pour alimenter ces deux éléments.

**Sur le PC *ALLS HX* :** Le port matériel correspondant au COM1 est la prise série située à gauche des ports USB et de la prise réseau. *([Manuel](maimaiDX-Manual.pdf), page 128)*.

---

## 🧠 Étape 5 : Compatibilité avec le système d'origine via le Proxy

C'est l'étape la plus complexe et la plus importante de ce guide. Comme expliqué plus tôt, nous souhaitons une fidélité logicielle totale. Toutefois, comme l'interface de communication des dalles tactiles ADX diffère des dalles officielles d'une borne *DX*, nous ne pouvons pas simplement les connecter via un port USB. Nous devons les adapter.

**Le problème matériel :** Le logiciel du jeu exige que les dalles tactiles communiquent via un ports "série". Précisément, via la norme RS-232, en 9600 bauds. Cependant, les dalles tactiles ADX envoient leurs données via USB, dans un format et avec des timings totalement différent.
Même si on utilise des adaptateurs USB, brancher les ADX directement sur le PC fera planter le jeu, car celui-ci ne comprend pas les informations encodée de cette façon. *(Pour plus de détails techniques, consultez le fichier `comprendre-maitouch_RS.md`)*.

### La Solution : Le Raspberry Pi et le programme `maitouch_rs`

Pour tromper le jeu, nous allons placer un mini-ordinateur (un **Raspberry Pi 5**) entre les dalles ADX et le PC *ALLS*. Ce Raspberry Pi va exécuter [un petit programme nommé `maitouch_rs` (écrit en langage Rust)](https://gitea.farewell.dev/Yttris/maitouch_rs), qui agira comme un **traducteur intelligent et un régulateur de vitesse**.

* **Il met en attente** les commandes lentes envoyées par le PC et les donne aux écrans en un seul bloc compréhensible.
* **Il absorbe** le torrent de données très rapides envoyées par les ADX via USB.
* **Il fait le tri** et n'envoie au PC **que la position du doigt la plus récente**, à une vitesse que la norme série peut supporter, évitant ainsi tout plantage.

### Mise en place du Proxy (Pour utilisateurs familiers avec Linux) :

1. Branchez les câbles USB de vos ADX sur les ports du Raspberry Pi (le Pi 5 a suffisamment de ports, pas besoin de Hub USB).
2. Reliez le Raspberry Pi aux ports du ALLS via les adaptateurs "USB-to-Serial" (puces FTDI) pour simuler la connexion lente attendue par le jeu.
3. **Sous Linux (sur le Raspberry Pi) :** Vous devez configurer le système pour que les ports USB gardent toujours le même nom (création de règles *udev* et de *symlinks*). Ainsi, même si vous redémarrez, le câble du joueur 1 s'appellera toujours "P1-TOUCH".
4. Téléchargez le code source de `maitouch_rs` créé par 4ndr3w, et compilez-le.
5. Testez la liaison en lançant manuellement la commande : `./maitouch ALLS ADX`. Si l'ADX répond, le pont fonctionne !
6. Créez un service `systemd` dans Linux. Cela permettra à ce programme de traduction de se lancer automatiquement et de manière invisible en arrière-plan à chaque fois que vous allumez la borne.

---

## 🎧 Étape 6 : Prises casques et Système Son

La borne *DX* propose des prises casques pour les joueurs, ce qui n'existait pas sur *Finale*.

L'ordinateur *ALLS HX* possède 4 sorties audio classiques (type Jack). Trois sont situées sur la carte mère principale, et une sur une carte d'extension *([Manuel](maimaiDX-Manual.pdf), page 128)*.
**Attention :** L'ordinateur ne sort qu'un son "pré-amplifié" (très faible). Dans une vraie borne *DX*, ce son passe par un gros amplificateur dédié. Vous pouvez réutiliser l'amplificateur de la *Finale* pour les haut-parleurs principaux, mais il ne gérera pas les nouvelles prises casques.

Voici à quoi correspondent les ports audio de l'ordinateur : *(Voir [manuel](maimaiDX-Manual.pdf), page 193)*

* **FRONT :** Sortie pour les haut-parleurs du Joueur 1
* **REAR :** Sortie pour les haut-parleurs du Joueur 2
* **C/W :** Sortie pour la prise casque du Joueur 1
* **SIDE :** Sortie pour la prise casque du Joueur 2

### Comment installer les prises casques :

Puisque le signal pour les casques (sorties C/W et SIDE) est trop faible, vous devez acheter un ou deux petits amplificateurs audio bon marché. **Inutile d'acheter des amplis avec des molettes de volume :** le volume des casques se règle numériquement directement dans les menus du jeu *DX*.

Pour l'installation physique des prises (qui sont de simples connecteurs Jack 3.5mm femelles), vous avez deux options :

1. **La méthode fidèle :** Percer la coque en plastique sous les boutons (comme sur une vraie *DX*) pour y encastrer les prises.
2. **La méthode non-destructrice :** Installer les deux prises casque au centre de la borne, entre les deux joueurs, via un boîtier réalisé manuellement.

**Astuce :** En salle d'arcade, les prises jack s'abîment très vite à force de brancher/débrancher les écouteurs. Prévoyez un système où la prise fixée sur la coque est facilement remplaçable (par exemple, reliez-la à l'amplificateur interne avec un câble détachable, plutôt que de souder le connecteur directement sur l'ampli).

---

## 💡 Étape 7 : Lumières (Optionnelle)

À ce stade, le jeu devrait être totalement jouable, mais l'éclairage esthétique de la borne n'est pas encore fonctionnel.
Sur *DX*, il y a trois contrôleurs différents qui gèrent l'éclairage de la borne :

* L'IO4 gère l'éclairage du "Billboard", le sommet de la borne. Référez-vous à l'étape 3 (point 3) pour savoir quelles broches utiliser.
* Deux cartes de contrôle identiques :
  * Une gère les LEDs des huit boutons du P1, l'éclairage du côté gauche, l'éclairage de l'anneau central de gauche et l'éclairage du fond de gauche.
  * L'autre gère les LEDs des huit boutons du P2, l'éclairage du côté droit, l'éclairage de l'anneau central de droite et l'éclairage du fond de droite.

Les deux cartes de contrôle s'interfacent en norme série RS-232 à une unique PCB convertissant les deux signaux RS-232 en USB. Cette PCB est elle-même raccordée au même multiprise USB (Hub) que les caméras lecteurs de QR-Code (Voir point suivant).
Les ports COM logiciels sur lesquels les contrôleurs de LEDs sont interfacés sont le **COM21** pour les LEDs du P1 et le **COM23** pour les LEDs du P2.

Dans le cas d'une borne convertie, toutefois, les choses sont un peu plus compliquées.

Il est théoriquement possible de réutiliser les contrôleurs de LEDs d'une borne *Finale*, toutefois ceci s'accompagne de plusieurs inconvénients.

- Le numéro de série de la PCB ne correspond pas à ce que *DX* s'attend à trouver, cela provoquera ainsi un avertissement ("warning") au démarrage de la borne. Cela dit, le contrôleur fonctionnera tout de même.
- En cas de "warning", le jeu n'envoie simplement pas les données permettant d'éclairer l'anneau central (à ne pas confondre avec les boutons) et le corps de la borne (Les données FET).

Les contrôleurs de LEDs de *Finale* s'interfacent de la même manière que ceux de *DX*, en passant par une carte de traduction intermédiaire convertissant le RS-232 des deux cartes en une unique connexion USB.
Les références sont les suivantes :

- *Finale* - Contrôleur LED : `837-15070-02-91 IC BD LED DRV32CH RS232` (Identique pour les deux joueurs)
- *Finale* - Convertisseur Serial-USB intermédiaire : `837-15067-02 IC BD USB TO 4SERIAL 232 IF`

Dans [le manuel de maimai *PiNK*](maimaiPiNK-Manual.pdf), on peut retrouver le contrôleur de LED à la page 192, et le convertisseur Serial-USB à la page 191 aux alentours de la zone FG-2.

Pour contourner le problème des avertissements sans avoir besoin de changer le contrôleur des LEDs, nous pouvons utiliser la même astuce de Proxy que nous avons utilisée à l'étape 5. À l'aide d'un second Raspberry Pi 5 [et du logiciel `maitouch_rs` (écrit en langage Rust)](https://gitea.farewell.dev/Yttris/mailight_rs), nous pouvons interfacer le contrôleur des LEDs avant la carte de traduction USB-Serial pour l'envoyer à notre proxy. Ce dernier s'occupera d'adapter le signal en modifiant les en-têtes pour fournir au jeu un signal lui faisant croire qu'il s'agit des bonnes PCB, il retournera ainsi un signal "GOOD" à la place du "warning". Le Raspberry Pi se placera alors entre les PCBs de contrôle des LEDs et le convertisseur serial USB, qui pourra lui être directement branché au ALLS sur le port dédié au Hub USB, ou au Hub USB lui-même si des lecteurs de QR-Code sont également installés.
Il est également possible de réutiliser le même Raspberry Pi 5 que celui des ADX pour effectuer le proxy des LEDs, toutefois à des fins de netteté et d'organisation, il est suggéré d'en dédier un pour chaque proxy.

---

## 📷 Étape 8 : Caméras (Optionnelle)

Si vous souhaitez finaliser votre borne pour qu'elle soit parfaite, vous pouvez ajouter les caméras. Cependant, le jeu est tout à fait fonctionnel sans elles.

### 1. Caméra des joueurs (Photos in-game)

Prenez une webcam très basique et bon marché. Imprimez un support en 3D pour la fixer au sommet de la borne, sur la vitre en acrylique.

* **Branchement :** Sur l'ordinateur *ALLS* posé à plat, cette webcam doit se brancher sur le port USB situé **en bas à droite** *([Manuel](maimaiDX-Manual.pdf), page 128)*.
  Deux LEDs dédiées sont également à câbler sur l'IO4. Sur le connecteur CN9, en position 7 "CAMERA LED WARM" et en position 8 "CAMERA LED RED". *(Voir [manuel](maimaiDX-Manual.pdf), page 194)*.
* La plupart des réseaux privés ne gèrent pas la caméra, son usage se résumera donc à l'affichage en jeu.

### 2. Caméras des lecteurs de QR-Code

Dans *DX*, les joueurs peuvent scanner des cartes avec des QR codes.

* Pour que cela fonctionne, vous devez obligatoirement utiliser des webcams capables de filmer en **format UVC 640x480**.
* **L'éclairage :** Le jeu exige d'éclairer ces cartes avec des LEDs blanches (alimentées en 12V). Ces LEDs sont contrôlées par l'IO4, via les broches 55 et 56. *(Voir [manuel](maimaiDX-Manual.pdf), page 194)*.
  *Astuce : Ne braquez pas les LEDs directement sur la lentille de la caméra. Éclairez plutôt la paroi en plastique pour que la lumière rebondisse de façon diffuse sur la carte.*
* **Branchement :** Sur une véritable borne *DX*, ces caméras sont reliées au même multiprise USB (Hub) que les lumières de la borne. Vous pouvez faire la même chose en utilisant un simple Hub USB branché sur le PC. Sur l'ordinateur *ALLS* posé à plat, le Hub doit être branché sur le port USB situé en **haut à droite** *([Manuel](maimaiDX-Manual.pdf), page 128)*.

**Faut-il vraiment installer les caméras QR Code ?**
C'est tout à fait optionnel. À moins que vous n'ayez accès à une autre borne très spécifique (le *Sega CardMaker*) pour imprimer vos cartes, elles ne vous serviront à rien. De plus, la plupart des réseaux privés offrent virtuellement un "DX Pass" à tous les joueurs, débloquant les fonctionnalités sans avoir besoin de scanner de cartes.

*Sachez qu'il est souvent possible lors de l'enregistrement de votre borne sur un réseau privé de demander à l'administrateur de désactiver complètement la recherche de ces caméras si vous ne souhaitez pas les installer.*

---

**Félicitations !** Si vous avez suivi toutes ces étapes, vous avez accompli une prouesse technique. Vous possédez désormais une borne *maimai DxNALE* fonctionnelle, sublimée et prête pour le jeu en ligne !
