---
title: "📖 Lexique"
---

# 📖 Petit Lexique pour les Débutants

Pour ne pas être perdu dans les termes techniques :

## Le PC et les cartes de la borne

* **ALLS (MX2 / HX2) :** C'est le nom de l'ordinateur standard utilisé par Sega pour faire tourner les jeux récents. Il remplace l'ancien PC de FiNALE (nommé Ringedge 2).
* **Carte I/O (IO board) :** C'est la carte électronique (un [PCB](#cablage-et-electronique)) qui fait le lien entre le PC et la borne. Elle capte l'appui sur les boutons. Dans le cas de *maimai FiNALE*, il s'agit d'une **Sega IO3**. Pour *DX*, elle doit être remplacée par une **Sega IO4**. La plupart des IO boards communiquent avec le système via le protocole [JVS](#communication-et-protocoles).
* **Aime / VFD :** Le lecteur de cartes sans contact (NFC) utilisé par les joueurs pour sauvegarder leur profil. Le *VFD* (Vacuum Fluorescent Display) est le petit écran à affichage rétro (souvent vert ou bleu) qui affiche le solde d'argent ou d'autres informations textuelles.

## Câblage et électronique

* **PCB :** Abréviation de *Printed Circuit Board*, autrement dit un "circuit imprimé". C'est le terme générique pour désigner une carte électronique, comme la carte I/O ou un contrôleur de LEDs.
* **Pinout (brochage) :** Le plan qui indique ce que fait chaque broche (chaque fil, chaque "pin") d'un connecteur. Un pinout vous dit par exemple que la broche n°51 d'un connecteur commande le bloqueur de pièces, et rien d'autre.
* **Connecteur Molex :** Un type de connecteur d'alimentation très courant en informatique, reconnaissable à son boîtier en plastique dur (souvent blanc ou noir) et ses broches épaisses. Sur le *Ringedge 2*, c'est par ce connecteur que transitaient les 12v/5v/3,3v vers le reste de la borne.
* **PSU :** Abréviation de *Power Supply Unit*, alimentation en français. C'est le composant qui transforme un courant d'entrée, le plus souvent du 100/220v AC, en tensions utilisables par le matériel électronique. Typiquement 12v, 5v, 3,3v.
* **Alimentation à découpage :** Un PSU qui transforme une tension électrique en une autre (par exemple du 24V en 5V) de façon compacte et efficace, en "découpant" le courant à très haute fréquence plutôt qu'en passant par un gros transformateur classique. C'est ce que désignent les références `SW REGU` sur les [schémas de câblage](wiring-diagrams.md).
* **FET :** Abréviation de *Field-Effect Transistor* (transistor à effet de champ). C'est un composant électronique qui agit comme un interrupteur commandé électriquement (on peut l'allumer/l'éteindre depuis un circuit de commande, sans intervention manuelle). Dans ce guide, "les données FET" désignent simplement les informations envoyées par le jeu pour piloter certains canaux d'éclairage additionnels (l'anneau central et le corps de la borne).
* **Photo-interrupteur :** Un petit capteur optique (une mini-fourche avec un émetteur et un récepteur de lumière) utilisé à l'intérieur des boutons pour détecter qu'ils sont enfoncés, sans contact mécanique qui s'use.

## Communication et protocoles

* **Ports COM (COM1, COM3...) :** Ce sont les "adresses" (ou canaux) virtuelles par lesquelles le PC communique avec certains périphériques spécifiques (comme les dalles tactiles ou le lecteur de carte *Aime*). Aujourd'hui, la plupart des connexions sur Port COM se font via des ports virtuels, toutefois un ALLS HX2 dispose de quatre connexions physiques pour y connecter le matériel de la borne.
* **Port série / RS-232 :** Une norme de communication filaire qui envoie les données un bit après l'autre sur un seul fil. Malgré son ancienneté, c'est encore aujourd'hui un standard industriel très répandu, notamment dans l'arcade, l'automatisme et l'instrumentation. C'est le protocole que le jeu *DX* utilise en interne pour parler à certains périphériques, comme les dalles tactiles ou les contrôleurs de LEDs.
* **Baud :** L'unité qui mesure la vitesse d'un port série. "9600 bauds" signifie environ 9 600 petits morceaux d'information par seconde, un débit nettement inférieur à celui de l'USB, mais parfaitement adapté aux usages pour lesquels ce type de liaison série reste employé.
* **USB-CDC :** Une classe de périphérique USB (*Communication Device Class*) qui permet à un appareil USB de se présenter à l'ordinateur comme un port série RS-232 classique. C'est pratique pour la compatibilité logicielle, mais le matériel réel derrière peut fonctionner à un débit très différent de celui qu'il annonce, ce qui peut créer des embouteillages de données si les deux bouts de la chaîne ne sont pas adaptés l'un à l'autre.
* **JVS :** Le protocole standard utilisé par la plupart des bornes d'arcade japonaises (Sega, Namco...) pour faire communiquer le système du jeu avec la carte I/O (boutons, capteurs, monnayeur). Contrairement à ce que son câble USB laisse penser, une carte JVS comme l'IO4 communique en réalité toujours via une liaison série (le protocole JVS lui-même repose sur du RS-485). JVS est le standard qui a succédé au JAMMA au passage des bornes basses-définitions aux générations suivantes.
* **Puce FTDI :** Le composant électronique présent dans la plupart des adaptateurs "USB-to-Serial" du commerce, qui convertit un port série RS-232 en USB (et inversement). C'est une référence tellement répandue que "FTDI" est souvent utilisé comme synonyme d'adaptateur USB-Série.
* **Adaptateur Null Modem :** Un petit adaptateur qui croise certains fils d'une connexion série (les fils d'émission et de réception). C'est en quelque sorte un "coupleur" : il permet à deux appareils "série" de se parler directement entre eux, sans passer par un vrai modem comme à l'origine de cette norme.
* **UVC (USB Video Class) :** Une norme qui permet à une webcam de fonctionner directement une fois branchée, sans installer de pilote particulier. Les lecteurs de QR-Code de *DX* exigent une webcam UVC filmant au format 640x480 précisément.

## Informatique et Linux

* **Proxy :** Dans ce guide, il ne s'agit pas d'un serveur web, mais d'un petit ordinateur (ou programme) placé entre deux appareils incompatibles pour "traduire" leurs échanges à la volée, sans que ni l'un ni l'autre ne s'en aperçoive. On parle parfois aussi de **MITM** pour désigner ce même rôle d'intermédiaire. C'est ce rôle que joue le Raspberry Pi à l'[Étape 5](step-5-proxy-compatibility.md) et à l'[Étape 7](step-7-lighting.md).
* **MITM (Man in the Middle) :** Littéralement "homme du milieu". Terme issu du monde de la sécurité informatique désignant un appareil ou un programme placé entre deux parties qui communiquent, capable de lire, modifier ou traduire leurs échanges. Le terme est souvent associé à une attaque malveillante, mais désigne ici un usage parfaitement légitime : un intermédiaire de confiance qui adapte la communication entre deux appareils pour les rendre compatibles.
* **Buffer (mémoire tampon) :** Une petite zone de stockage temporaire où l'on accumule des données avant de les traiter ou de les envoyer d'un seul coup, plutôt qu'au fil de l'eau. C'est une technique courante dans ce type de pont de communication, par exemple pour regrouper des commandes avant de les transmettre.
* **Règle udev / Symlink :** Sous Linux, un port USB peut changer de nom à chaque redémarrage (par exemple passer de `/dev/ttyUSB0` à `/dev/ttyUSB1`). Une règle *udev* permet de figer un nom stable et prévisible (un "raccourci", ou *symlink*) pour un appareil précis, par exemple pour être certain qu'un câble donné garde toujours le même nom.
* **Service systemd :** Sous Linux, un programme qui se lance automatiquement et en arrière-plan dès le démarrage de la machine, sans intervention manuelle. C'est ce qui permet à un programme de démarrer tout seul à chaque allumage de la borne, sans avoir à le lancer à la main.

---

Le vocabulaire est clair ? Passons à la [Liste de courses](equipment.md).
