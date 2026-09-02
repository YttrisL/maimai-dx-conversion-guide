---
title: "Wiring diagrams"
---

# Wiring diagrams

The [official manuals](official-manuals.md) contain, on their very last pages, the complete wiring diagram of the cabinet (A3-format plates, one per manual of several dozen MB). To avoid having to download an entire manual and zoom into a PDF reader just to find a wire, here are those plates extracted in high resolution.

_(Click a plate to open it at full resolution in a new tab. Each plate is preceded by the list of boards/modules that appear on it, with their part number, so you can find a board with `Ctrl+F`. The coordinates in brackets, e.g. **[C-3]**{: .wiring-coord }, refer to the reference grid printed around the edge of each plate - columns A to G, rows 1 to 6 - and indicate where the part is on the diagram.)_

## maimai DX manual

Chapter *22 総合配線図* ("general wiring diagram"), pages 193 to 196 of the [maimai DX manual](../resources/pdfs/maimai-dx-manual-full.pdf).

### Plate 1/4 - Power, *ALLS* PC, amp and player screens

* `MMT-1050` **ASSY AC UNIT** **[A-1]**{: .wiring-coord } - mains input block (noise filter, fuse, IEC socket)
* `MMT-4200` **ASSY XFMR** **[C-1]**{: .wiring-coord } - power transformer
* `MMT-4300` / `601-13203-63` **ASSY ROUTER (ROUTER RTX830 BD MMT)** **[F-1]**{: .wiring-coord } - network router board
* `MMT-4100` **ASSY ELEC BD** **[A-2]**{: .wiring-coord } - main electronics board, which brings together:
    * `838-15228` **2.1CH 40W STEREO AMP BD** ×2 **[B-2/B-3]**{: .wiring-coord } - Player 1 and 2 audio amps
    * `839-1363-01` **HEADPHONE AMP BD SHC** ×2 **[B-5/B-6]**{: .wiring-coord } - Player 1 and 2 headphone amps
    * `400-5489-15024` **SW REGU VS150E-24** **[A-3]**{: .wiring-coord } - 24V switching power supply
    * `400-5464-01505` **SW REGU VS15C-5** **[A-4]**{: .wiring-coord } - 5V switching power supply
* `849-1004` **ASSY CASE ALLS HX2 W HDD** **[E-4]**{: .wiring-coord } - the *ALLS* PC case itself
* `MMT-1000` / `MMT-1500` **ASSY CABINET 1P / 2P** **[D-2/G-2]**{: .wiring-coord } - player screens (`200-6280` **LCD DSPL 43 LED**)
* `MMT-1200` / `MMT-1700` **ASSY SW BASE 1P / 2P** **[C-5/D-4]**{: .wiring-coord } - button bases

[![maimai DX wiring diagram, plate 1 of 4](../resources/images/wiring-diagrams/maimai-dx-wiring-diagram-1-of-4.jpg)](../resources/images/wiring-diagrams/maimai-dx-wiring-diagram-1-of-4.jpg)

---

### Plate 2/4 - Buttons, button LEDs, USB hub and I/O board

* `MMT-1200` / `MMT-1700` **ASSY SW BASE 1P / 2P** **[A-1]**{: .wiring-coord } - button bases
* `837-15070-04` **IC BD LED DRV32CH RS232** ×2 **[E-2/D-2]**{: .wiring-coord } - LED driver, one per side
* `837-20008` **4PORT USB HUB BD MINIB TO A** **[B-4]**{: .wiring-coord } - 4-port USB hub
* `837-15067-02` **IC BD USB TO 4SERIAL 232 IF** **[A-5]**{: .wiring-coord } - USB to 4-port serial adapter
* `837-15257-01` **I/O CONTROL BD 4 FOR USB** **[E-4]**{: .wiring-coord } - the **IO4** board (JVS), see [step 3](step-3-io-board.md)
* `MMT-1000` / `MMT-1500` / `MMT-1900` **ASSY CABINET 1P / 2P / SIDE COVER BASE 1P** **[G-3/G-6/G-1]**{: .wiring-coord }

[![maimai DX wiring diagram, plate 2 of 4](../resources/images/wiring-diagrams/maimai-dx-wiring-diagram-2-of-4.jpg)](../resources/images/wiring-diagrams/maimai-dx-wiring-diagram-2-of-4.jpg)

---

### Plate 3/4 - Buttons, touch ring sensor, billboard

* `MMT-2000` **ASSY BUTTON SWITCH** ×8 **[B-1→B-4]**{: .wiring-coord } - buttons, each with:
    * `838-15235-01` **LED BD RGB 3X1BLOCK 5050** **[B-1→B-4]**{: .wiring-coord } - button RGB LED
    * `370-5359` **PHOTO INTERRUPTER OJ-555S-A5** **[C-1→C-4]**{: .wiring-coord } - optical button-press sensor
* `837-20015` **HEADPHONE JACK BD** (`MMT-1070`) **[E-3]**{: .wiring-coord } - headphone jack board
* `509-6483` **TOUCH SENSOR UNIT TPK** **[B-6]**{: .wiring-coord } - touch ring sensor board
* `MMT-1800-01` **ASSY BILLBOARD** **[F-5]**{: .wiring-coord } - billboard at the top of the cabinet
    * `390-5768` **LED TAPE RGB** **[F-4/G-4]**{: .wiring-coord } - billboard RGB LED strips
    * `MMT-1080` speakers `130-5310` **[F-5/G-5]**{: .wiring-coord }
* `390-7244` **LED TAPE WHITE M3528W-A** **[E-2]**{: .wiring-coord } - white LED strips of the ring
* `130-5280-01` **WOOFER 4OHM 80W** **[E-6]**{: .wiring-coord }

[![maimai DX wiring diagram, plate 3 of 4](../resources/images/wiring-diagrams/maimai-dx-wiring-diagram-3-of-4.jpg)](../resources/images/wiring-diagrams/maimai-dx-wiring-diagram-3-of-4.jpg)

---

### Plate 4/4 - Cameras, Aime reader, coin mech and entry panel

* `MMT-1350` / `MMT-1370` **ASSY PLAYER CAMERA / PLAYER CAMERA UNIT** **[D-1]**{: .wiring-coord } - player cameras
    * `601-13249` **CAMERA KBCR-S03MU-HPB2033-C300** **[D-1]**{: .wiring-coord }, see [step 7](step-7-cameras.md)
* `MMT-1440` **ASSY AIME AND VFD** **[B-3]**{: .wiring-coord } - Aime reader module (AIME RW UNIT) and display
    * `200-6275` **VFD GP1232A02A FUTABA** **[A-4]**{: .wiring-coord }, see [step 4](step-4-aime-reader.md)
* `MMT-1470` **ASSY CODE READER** **[B-5]**{: .wiring-coord } - QR code reader
    * `601-13216-01` **USB CAMERA MS-M33NU2AMSH43-S2** **[A-5/A-6]**{: .wiring-coord }
* `MMT-1400` **ASSY CENTER TOWER** **[B-4]**{: .wiring-coord } - center tower
* `MMT-1450` **ASSY ENTRY PANEL** **[D-3]**{: .wiring-coord } - player select buttons
    * `509-5970` **SW PB OBSF-24TR** **[D-3]**{: .wiring-coord } - Sanwa part
* `MMT-1420` **ASSY SELECTOR DOOR** **[G-5]**{: .wiring-coord } - selector/coin mech
    * `220-5846-91-01` **[G-5]**{: .wiring-coord } - coin acceptor mechanism
    * `220-5798-01` **MAG CNTR 4P MZ674** **[F-6]**{: .wiring-coord } - coin counter
* `MMT-1460` **SW UNIT** **[G-5]**{: .wiring-coord } - test/service buttons
    * `838-14548-10` **SW & VOL BD** **[G-5]**{: .wiring-coord }
* `MMT-1900` / `MMT-1950` **ASSY SIDE COVER BASE 1P / 2P** **[A-1/G-2]**{: .wiring-coord }

[![maimai DX wiring diagram, plate 4 of 4](../resources/images/wiring-diagrams/maimai-dx-wiring-diagram-4-of-4.jpg)](../resources/images/wiring-diagrams/maimai-dx-wiring-diagram-4-of-4.jpg)

---

## maimai PiNK manual

Chapter *25 WIRING DIAGRAM*, pages 189 to 193 of the [maimai PiNK manual](../resources/pdfs/maimai-pink-manual-full.pdf).

### Plate 1/4 - Power, screen and coin selector

* `MAI-1050` **AC UNIT** **[B-1]**{: .wiring-coord } - mains input block
* **ASSY LCD** **[F-1]**{: .wiring-coord } - Player 1, screen (`200-6226-91` **ASSY LCD DSPL 42 TYPE LED Y**)
* coin acceptor mechanism
    * `MAI-1420` **ASSY SELECTOR DOOR** **[A-4]**{: .wiring-coord } - Japan version
        * `220-5846-01` **PFB-730 QL203 12VBK 100** **[B-3]**{: .wiring-coord }
    * `MAI-1420-01` **ASSY SELECTOR DOOR EXP** **[C-4]**{: .wiring-coord } - export version
        * `220-5842` **ELEC CC REJR SG-828** **[C-3]**{: .wiring-coord }
* **XFMR WIRING** **[B-5→G-6]**{: .wiring-coord } - multi-voltage transformers
    * `560-5515-V-91` **[B-6]**{: .wiring-coord } - 100V zone variant
    * `560-5599` **[C-5]**{: .wiring-coord } - 110V to 240V zone variant (repeated at several voltages on the plate)

[![maimai PiNK wiring diagram, plate 1 of 4](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-1-of-4.jpg)](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-1-of-4.jpg)

---

### Plate 2/4 - Aime reader, speakers, LEDs and power supplies

* `MAI-1400` **ASSY COIN CHUTE TOWER** **[B-2]**{: .wiring-coord } - center tower
    * `838-14971` **NFC RW BD TN32MSEC003S** **[D-1/D-2]**{: .wiring-coord } - the Aime card reader board, replaced in [step 4](step-4-aime-reader.md)
* `MAI-1420` **ASSY SELECTOR DOOR** **[D-2]**{: .wiring-coord }
    * `220-5798-01` **MAG CNTR 4P MZ674** **[C-2]**{: .wiring-coord } - coin counter
* `MAI-1460` **SW UNIT** (`838-14548-10` **SW & VOL BD**) **[D-3]**{: .wiring-coord } - test/service and volume buttons
* `MAI-0500` **ASSY SPEAKER** **[G-1]**{: .wiring-coord } - speakers
    * `838-15228` **2.1CH 40W STEREO AMP BD** ×2 **[F-2/F-3]**{: .wiring-coord }
    * `130-5296` enclosure **[G-1]**{: .wiring-coord }
    * `130-5280` woofer **[G-2]**{: .wiring-coord }
* `MAI-1090` **FAN UNIT DC12V** (`260-0139`) **[D-4]**{: .wiring-coord } - fan
* `MAI-4000` **ASSY SW RGLTR** **[C-4]**{: .wiring-coord } - switching power supplies (`400-5489-15024`/`15012`)
* `MAI-1080` **CENTER LED / ROOF LED (L) / ROOF LED (R)** ×3 **[F-3/F-4]**{: .wiring-coord }
    * `MAI-1070` **WOOFER LED** **[E-5]**{: .wiring-coord } - decorative LEDs (`838-15235-01` **LED BD RGB**)

[![maimai PiNK wiring diagram, plate 2 of 4](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-2-of-4.jpg)](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-2-of-4.jpg)

---

### Plate 3/4 - I/O board (JVS), Serial-USB adapter, touch controller and *RingEdge 2* PC

* **ASSY LCD** **[G-1]**{: .wiring-coord } - Player 2, screen (`200-6226-91` **ASSY LCD DSPL 42 TYPE LED Y**)
* `837-14505` **I/O CONTROL BD FOR JVS** **[D-1]**{: .wiring-coord } - the IO3 board, replaced by the IO4 in [step 3](step-3-io-board.md)
* `837-15067-02` **IC BD USB TO 4SERIAL 232 IF** **[F-2]**{: .wiring-coord } - the RS-232 to USB adapter mentioned in [step 6](step-6-lighting.md)
* `838-15221` **SERIAL I/F BD TOUCHPANEL GUNZE** **[D-4]**{: .wiring-coord } - touchscreen controller board
* **ASSY CASE RGE2 W M2G S64G** **[E-3/E-4]**{: .wiring-coord } - *RingEdge 2* PC
    * `846-5003D` **[E-3]**{: .wiring-coord } (Japan version)
    * `846-5003D-02` **[E-4]**{: .wiring-coord } (export version)
* `MAI-4100` **ASSY ROUTER** (`601-12336-34` **ROUTER RT107E BD MAI**) **[F-6]**{: .wiring-coord }

[![maimai PiNK wiring diagram, plate 3 of 4](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-3-of-4.jpg)](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-3-of-4.jpg)

---

### Plate 4/4 - Buttons, LED controller and touch ring

* `MAI-1200` / `MAI-1201` **ASSY SW BASE** **[D-1/D-5]**{: .wiring-coord } - base and layout of the 8 buttons
    * `838-15235-01` **LED BD RGB** **[D-1→D-3]**{: .wiring-coord }
    * `370-5359` **PHOTO INTERRUPTER OJ-535S-A5** **[E-1→E-3]**{: .wiring-coord }
* `837-15070-02-91` **IC BD LED DRV32CH RS232** **[C-4]**{: .wiring-coord } - the LED controller mentioned in [step 6](step-6-lighting.md)
* `509-6384` **TOUCH SENSOR PANEL UNIT** **[E-5]**{: .wiring-coord } - touch ring sensor board

[![maimai PiNK wiring diagram, plate 4 of 4](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-4-of-4.jpg)](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-4-of-4.jpg)

---

### Optional camera kit - Player camera and control box

* `MAI-3100` **ASSY CAMERA SW RGLTR** **[C-1]**{: .wiring-coord } - camera PSU
    * `400-5489-05012` **SW REGU VS50E-12** **[C-3]**{: .wiring-coord }
* `MAI-3000` **ASSY CAMERA BOX** **[D-1]**{: .wiring-coord } - camera box, see [step 7](step-7-cameras.md)
    * `838-15222` **MOVIE CAMERA CTRL BD** **[D-3]**{: .wiring-coord }
    * `601-12827-01` **BD CAMERA KBCR-S01MG-HPB1022** **[F-2]**{: .wiring-coord }
* `MAI-3050` **ASSY LCD W/CUSHION** **[F-3]**{: .wiring-coord } - feedback screen
    * `200-6211` **LCD MODULE NL6448BC18-01 NLT** **[F-3]**{: .wiring-coord }
* **ASSY CASE RGE2 W M2G S64G** **[C-3/C-4]**{: .wiring-coord } - *RingEdge 2* PC
    * `846-5003D` **[C-3]**{: .wiring-coord } (Japan version)
    * `846-5003D-02` **[C-4]**{: .wiring-coord } (export version)
* `MAI-4100` **ASSY ROUTER** (`601-12336-34` **ROUTER RT107E BD MAI**) **[B-5]**{: .wiring-coord }

[![maimai PiNK wiring diagram, optional camera kit](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-camera-kit.jpg)](../resources/images/wiring-diagrams/maimai-pink-wiring-diagram-camera-kit.jpg)

---
