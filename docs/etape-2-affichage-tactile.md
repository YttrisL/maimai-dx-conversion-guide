# 📺 Étape 2 : L'Affichage et les Dalles Tactiles ADX

Toute la complexité réside au niveau de la connexion des dalles tactiles ADX, mais dans un premier temps, commençons par les installer.

## Les connexions vidéo

Le jeu est programmé pour envoyer la vidéo d'une manière bien précise aux deux écrans. L'ordre doit être respecté. *(Référence : [Manuel](pdfs/maimai-dx-manual-full.pdf) officiel de la borne DX, page 128)*

* **Joueur 1 (P1) :** Doit être branché sur le port **DisplayPort** (Attention : le [manuel](pdfs/maimai-dx-manual-full.pdf) officiel comporte une erreur et indique HDMI à tort).
* **Joueur 2 (P2) :** Doit être branché sur le port **DVI**.

*(Le port HDMI restant sur la carte graphique peut être utilisé pour brancher du matériel de capture vidéo, toutefois celui-ci ne propose que la sortie du joueur 1)*.

Il existe toutefois une légère différence native entre les écrans d'une *Finale* et d'une *DX*. Dans les deux cas, il s'agit d'écrans 1920x1080 cadencés à 60hz, mais les écrans de *Finale* mesurent 42" de diagonale, alors que les écrans de *DX* mesurent 43". La différence est pratiquement imperceptible en jeu.

## Les dalles tactiles ADX

Retirez les anciennes dalles tactiles de la borne *Finale* (maintenue par 8 vis) et installez les nouvelles dalles ADX.
Il faut ensuite raccorder les dalles aux bonnes "adresses" (Ports COM) sur le ALLS, sinon le jeu confondra les deux joueurs : *([Manuel](pdfs/maimai-dx-manual-full.pdf), page 128)*

* **Joueur 1 :** Doit être branché au Port **COM3**.
* **Joueur 2 :** Doit être branché au Port **COM4**.

En l'état, la connexion fournie par les dalles ADX se fait via USB-CDC, ce qui ne correspond pas aux raccordements souhaités sur le ALLS. Laissez les câbles USB des deux ADX débranchés pour le moment. Nous les connecterons au Raspberry Pi à l'[Étape 5](etape-5-proxy-compatibilite.md) pour assurer la compatibilité totale avec le système d'origine.

---

Passons à l'[Étape 3 : La Carte I/O et les Boutons](etape-3-carte-io.md).
