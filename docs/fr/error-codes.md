---
title: "Codes d'erreurs"
---

# 🚨 Codes d'erreurs

Cette page rassemble les codes d'erreur documentés dans les [manuels officiels](official-manuals.md), avec leur cause et le remède préconisé par le constructeur.

Sources utilisées :

* [Service Manual *ALLS HX2*](../resources/pdfs/alls-hx2-service-manual-full.pdf), chapitre 4 (anglais) : les **erreurs système**, communes à tous les jeux tournant sur *ALLS HX2*. C'est la source principale.
* [Service Manual *maimai DX*](../resources/pdfs/maimai-dx-service-manual-full.pdf), chapitre 5 (japonais) : les **erreurs propres à *maimai DX***.
* [Instruction Manual *maimai DX*](../resources/pdfs/maimai-dx-instruction-manual-full.pdf) : aucun tableau de codes, seulement quelques mentions ponctuelles (voir la dernière section).

!!! info "À savoir avant de lire les tableaux"
    * Les textes anglais et japonais sont traduits ici. Les **intitulés anglais d'origine** sont conservés dans les tableaux du *ALLS HX2* pour pouvoir chercher un code dans le manuel.
    * Pour redémarrer après une erreur, le manuel *DX* demande de couper l'**interrupteur d'alimentation secondaire** de la borne, d'attendre un court instant, puis de le remettre. Il ne faut pas enchaîner rapidement les coupures et remises sous tension.

## 1. Erreurs système du *ALLS HX2*

### Keychip (clé de licence)

| Code | Intitulé | Cause | Remède indiqué |
|---|---|---|---|
| 0001 | Keychip Not Found | Pas de keychip, ou keychip mal branché. | Vérifier que le keychip est bien connecté. |
| 0002 | Keychip Not Available | Le keychip n'est pas pris en charge. | Vérifier la combinaison keychip et support d'installation (DVD, etc.). |
| 0004 | Game Program Not Acceptable | Le keychip n'est pas pris en charge. | Vérifier qu'aucun keychip d'un autre système n'est inséré. |
| 0008 | Keychip Access Failed | Impossible d'accéder au keychip. | Éteindre, réinsérer le keychip, puis redémarrer le *ALLS HX2*. |
| 0949 | Keychip Not Found | Pas de keychip, ou défaut de connexion. | Vérifier que le keychip est bien connecté. |

### Carte mère et plantage du jeu

| Code | Intitulé | Cause | Remède indiqué |
|---|---|---|---|
| 0010 | Unexpected Game Program Failure | Le programme du jeu a planté de façon inattendue. | Éteindre et redémarrer le *ALLS HX2*. |
| 0021 | Main board Malfunctioning | La carte mère ne se reconnaît pas elle-même. | Éteindre et redémarrer. |
| 0028 / 0029 / 0032 | Main board Malfunctioning | Échec d'accès à la carte mère. | Éteindre et redémarrer. |
| 0912 | Unexpected Game Program Failure | La carte graphique n'a pas pu continuer le rendu. | Éteindre et redémarrer. |

### Installation du jeu (DVD, USB, serveur LAN)

| Code | Intitulé | Cause | Remède indiqué |
|---|---|---|---|
| 0022 | Game Program Not Found on Storage Device | Aucun programme de jeu sur le stockage. | Réinstaller le jeu depuis le support d'installation. |
| 0041 | Game Program Not Found on Install Media | Aucun programme de jeu sur le support d'installation. | Vérifier que le jeu placé sur le support et le keychip correspondent. |
| 0042 | Game Program Not Found on Install Media | Une partie du programme du jeu est manquante. | Vérifier la façon dont le jeu a été installé. |
| 0049 / 0052 | Install Media Access Failed | Échec d'accès au support d'installation. | Vérifier que le DVD n'est pas rayé, abîmé ou sale, et que le lecteur DVD est bien branché. |
| 0055 | Game Program Verify Error | Le jeu installé ne fonctionne pas correctement. | Réinstaller le jeu depuis le support d'installation. |
| 0064 | Game Program Not Found on Server | Aucun programme de jeu sur le serveur d'installation LAN. | Vérifier que le jeu placé sur le serveur et le keychip correspondent. |
| 0066 | Game Program Verify Error | Le jeu installé ne fonctionne pas correctement. | Réinstaller le jeu depuis le support d'installation. |
| 0088 | System Program Verify Error | Le programme système installé ne fonctionne pas correctement. | Réinstaller depuis le support d'installation. |
| 0917 | USB Flash Drive Remain Error | La clé USB d'installation est restée branchée. | Retirer la clé USB. |
| 0919 | DVD Drive Remain Error | Le lecteur DVD d'installation est resté branché. | Retirer le lecteur DVD. |

### Stockage (SSD principal et stockage secondaire)

| Code | Intitulé | Cause | Remède indiqué |
|---|---|---|---|
| 0081 | Invalid Storage Format | Le format du SSD principal est incorrect. | Contacter le support. |
| 0082 | Game Program Access Failed | Le SSD principal n'est pas reconnu. | Réinstaller le jeu depuis le support d'installation. |
| 0083 | Storage Device Not Acceptable | Le SSD principal n'a pas assez d'espace. | Lancer "UNINSTALL" dans "STORAGE INFORMATION" du mode test système, puis réinstaller (manuel 3-2, p. 8). |
| 0084 | Storage Device Malfunctioning | Le SSD principal est peut-être défaillant. | Éteindre et redémarrer. |
| 0085 | Invalid Storage Format | Le format du SSD principal est incorrect. | Contacter le support. |
| 0086 | Invalid Storage Format | Le format du stockage secondaire est incorrect. | Formater depuis "Storage information" du mode test système. |
| 0087 | Storage Device Malfunctioning | Le stockage secondaire est peut-être défaillant. | Éteindre et redémarrer la borne. |
| 0909 | Not Enough Storage Device | Le jeu n'a pas assez de stockage. | Contacter le support. |
| 0915 | Wrong Storage Device | Le stockage secondaire n'est pas connecté. | Contacter le support. |
| 0916 | Wrong Storage Device | Un stockage secondaire (HDD) inutile est connecté. | Contacter le support. |

### Compatibilité, mémoire et matériel

!!! tip "Astuce"
    Pour ces erreurs matérielles, il suffit **bien souvent** de retirer l'élément concerné (carte, barrette, câble...) puis de le **réinstaller dans son socle**. Par exemple, retirer la carte graphique et la remettre dans son slot peut résoudre le code 0905.

| Code | Intitulé | Cause | Remède indiqué |
|---|---|---|---|
| 0091 | Too High CPU Temperature | La température du CPU est élevée. | Nettoyer le *ALLS HX2* et son emplacement, vérifier que les sorties d'air ne sont pas obstruées (chapitre 5 du manuel). Le manuel recommande aussi un nettoyage annuel. |
| 0901 | Wrong Platform | Le jeu n'est pas pris en charge par le *ALLS HX2*. | Vérifier le manuel du jeu et la combinaison jeu / *ALLS HX2*. |
| 0902 | Wrong System Program | Démarrage avec un programme système non pris en charge, le programme système du *ALLS HX2* doit être mis à jour. | Vérifier la façon dont le jeu a été installé. |
| 0904 | Wrong Platform | Le programme système installé ne fonctionne pas correctement (texte tel qu'imprimé, il ne correspond pas à l'intitulé). | Réinstaller depuis le support d'installation. |
| 0905 | Graphic Function Not Found | Le jeu ne prend pas en charge la fonction graphique. | Contacter le support. |
| 0906 | Sound Function Not found | La fonction audio du *ALLS HX2* n'est pas reconnue. | Contacter le support. |
| 0907 | Not Enough System Memory | Le jeu n'a pas assez de mémoire. | Contacter le support. |
| 0918 | Not Enough System Memory Module | Le nombre de barrettes mémoire requis par le jeu est insuffisant. | Contacter le support. |
| 0920 | Wrong Coin Assignments | Le jeu ne prend pas en charge l'attribution des pièces actuelle. | Vérifier "COIN ASSIGNMENTS" dans le mode test système (3-6, p. 14). |

### Carte I/O

| Code | Intitulé | Cause | Remède indiqué |
|---|---|---|---|
| 6401 | I/O board is not connected to main board | (1) La carte I/O n'est pas connectée. (2) Connexion peu fiable entre le *ALLS HX2* et la carte I/O. | (1) Connecter la carte I/O et vérifier son câble d'alimentation. (2) Rebrancher ou remplacer le câble USB entre la carte I/O et le *ALLS HX2*. |
| 6402 | I/O board does not fulfill the game spec | La carte I/O connectée n'est pas la bonne. | Utiliser une carte I/O adaptée au jeu. |

### Réseau et ALL.Net

| Code | Intitulé | Cause | Remède indiqué |
|---|---|---|---|
| 8001 | Network address error (DHCP) | Les réglages réseau n'ont pas pu être initialisés. | Vérifier la connexion réseau et redémarrer le *ALLS HX2* selon la procédure de démarrage. |
| 8002 | Network setting error (SYSTEM) | "NETWORK SETTING" du mode test système est incorrect. | Vérifier les réglages réseau (3-9, p. 24). |
| 8003 | Network address error (Dup.IP) | Les réglages réseau n'ont pas pu être initialisés. | Vérifier la connexion réseau et redémarrer. |
| 8004 | Network setting error (Dup.IP) | "NETWORK SETTING" du mode test système est incorrect. | Vérifier les réglages réseau (3-9, p. 24). |
| 8005 | Network type error (WAN) | Le type de ligne du routeur ALL.Net connecté est incorrect. | Vérifier le type de ligne du routeur ALL.Net. |
| 8006 | Network timeout error (DHCP) | Les réglages réseau n'ont pas pu être initialisés. | Vérifier la connexion réseau et redémarrer. |
| 8007 | Network timeout error (DNS-WAN) | Impossible d'établir la connexion avec ALL.Net. | Vérifier la connexion réseau du *ALLS HX2*, le réseau du lieu et la liaison routeur ALL.Net / câble réseau, puis redémarrer. Si l'erreur persiste, consulter les informations de maintenance. |
| 8008 | Network timeout error (DNS-LAN) | Impossible d'établir la connexion avec le routeur ALL.Net. | Vérifier la connexion réseau du *ALLS HX2* et la connexion ALL.Net du lieu, puis redémarrer. |
| 8009 | Network Game Disabled | La connexion ALL.Net du mode test jeu est sur OFF. | Vérifier le réglage de connexion ALL.Net dans le mode test jeu. |
| 8103 | ALL.Net System error (TIMEOUT) | Impossible d'établir la connexion avec ALL.Net. | Même procédure que 8007. |
| 8106 | ALL.Net System Caution | Impossible d'établir la connexion avec ALL.Net. | Même procédure que 8007. |
| 8111 | ALL.Net System error (REG) | L'enregistrement ALL.Net n'a pas pu être confirmé. | Vérifier que l'enregistrement ALL.Net (le contrat) est bien terminé. |
| 8113 | ALL.Net System error (MODE) | Les réglages ALL.Net n'ont pas pu être confirmés. | Contacter le support. |
| 8114 | ALL.Net System error (RTC) | Impossible d'établir la connexion avec ALL.Net. | Même procédure que 8007. |
| 8201 | ALL.Net System error (TIMEOUT) | Impossible d'établir la connexion avec ALL.Net. | Même procédure que 8007. |
| 8202 | ALL.Net System error (REG) | L'enregistrement ALL.Net n'a pas pu être confirmé. | Vérifier que l'enregistrement ALL.Net (le contrat) est bien terminé. |
| 8301 | Network error (GAME-LAN) | La connexion avec les appareils qui composent ce jeu n'a pas pu être confirmée. | Vérifier la connexion réseau et redémarrer. |
| 8302 | Maintenance time (GAME) | Le serveur est actuellement en maintenance. | Attendre la fin de la maintenance du serveur. |
| 8303 | Network error (GAME) | Impossible d'établir la connexion avec ALL.Net. | Même procédure que 8007. |
| 8304 | Network failed (GAME) | Panne réseau irrécupérable. | Même procédure que 8007. |

## 2. Erreurs spécifiques à *maimai DX* (manuel de service *DX*, chapitre 5)

Le manuel indique aussi l'endroit où se situe la panne ("発生場所").

| Code | Message affiché | Lieu | Cause | Remède indiqué |
|---|---|---|---|---|
| 0951 | USB devices are insufficient | `Adaptateur 4x RS-232 vers USB` | Communication impossible avec `l'adaptateur 4x RS-232 vers USB`. | Redémarrer. Si cela ne suffit pas, vérifier la connexion de `l'adaptateur 4x RS-232 vers USB` (`837-15067-02`) et du hub USB (`837-20008`) (chapitre 22 du manuel d'instruction, schéma de câblage général). |
| 3100 | Connection of the code reader or the player camera cannot be confirmed | Lecteur de code ou caméra joueur | Connexion du lecteur de code ou de la caméra joueur introuvable. | Dans le mode test, utiliser le test des caméras pour repérer la caméra non reconnue, vérifier sa connexion ainsi que celle du hub USB (`837-20008`) (3-6, p. 44). |
| 3101 | Code reader recognition failed | Lecteur de code | Le code d'identification de la caméra du lecteur de code est illisible. | Nettoyer le code d'identification de la caméra (14-2 du manuel d'instruction). |
| 3102 | Player camera not recognized | Caméra joueur | La caméra joueur n'est pas reconnue. | Redémarrer. Sinon, vérifier que la caméra est bien branchée (chapitre 22). |
| 3201 | Reference machine duplicated in the same cabinet group | *ALLS HX2* | Deux machines "de référence" dans le même groupe de bornes. | Vérifier les réglages du jeu et redémarrer le *ALLS HX2* (3-7, p. 46). |
| 3300 | Cannot connect to touch sensor (1P) (timeout) | Dalle tactile 1P | Connexion à la dalle tactile 1P introuvable. | Vérifier la connexion de la dalle tactile 1P (3-5, p. 39 et 11-4 du manuel d'instruction). |
| 3301 | Touch sensor (1P) initialization failed | Dalle tactile 1P | Échec d'initialisation de la dalle tactile 1P. | Redémarrer. Sinon, remplacer la dalle tactile (11-4). |
| 3302 | Cannot connect to touch sensor (2P) (timeout) | Dalle tactile 2P | Connexion à la dalle tactile 2P introuvable. | Vérifier la connexion de la dalle tactile 2P (3-5, p. 39 et 11-4). |
| 3303 | Touch sensor (2P) initialization failed | Dalle tactile 2P | Échec d'initialisation de la dalle tactile 2P. | Redémarrer. Sinon, remplacer la dalle tactile (11-4). |
| 8405 | Multiple LAN install servers found (client) | *ALLS HX2* | Plusieurs serveurs d'installation LAN détectés. | Vérifier le réglage du serveur d'installation LAN (4-2, p. 67). |
| 8406 | Multiple LAN install servers found (server) | *ALLS HX2* | Plusieurs serveurs d'installation LAN détectés. | Vérifier le réglage du serveur d'installation LAN (4-2, p. 67). |

Les intitulés de cette section sont une traduction du japonais. Les codes 3300 à 3303 concernent les dalles tactiles, pas les écrans d'affichage.

## 3. Autres mentions de codes dans les manuels

| Code | Manuel | Contexte |
|---|---|---|
| Error 0917 | Instruction *DX*, pages 77 et 80 du PDF (installation du jeu) | Message "Error 0917 : clé USB branchée" affiché en fin d'installation tant que la clé USB n'est pas retirée. Voir le code 0917 plus haut. |
| Error 0091 | Instruction *DX*, page 151 du PDF (*ALLS HX2*) | Nettoyer le *ALLS HX2* une fois par an ou à l'apparition de ce code. |
| "Reste sur le logo *ALLS* sans passer à l'attract mode (une erreur s'affiche)" | Instruction *DX*, page 92 du PDF (dépannage) | Cause : mauvais réglage ou panne du *ALLS HX2*. Remède : consulter le chapitre des erreurs du manuel de service du *ALLS HX2*, et remplacer le *ALLS HX2* en cas de panne. |
