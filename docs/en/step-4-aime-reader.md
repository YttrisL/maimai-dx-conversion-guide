---
title: "💳 4 - Aime card reader"
---

# 💳 Step 4: The Aime Reader and the VFD

**The FiNALE Aime readers are not compatible with DX**: you need to install a newer-generation reader. The VFD has no real use in our conversion, but the software still requires it. Good news: both are very simple to install.

## Technical explanation

??? note "Click here for the technical explanation"
    FiNALE uses two previous-generation Aime readers, chained to each other: the top one reads the left player's card, the bottom one the right player's.

    On DX, there is only **a single reader**. When a card is scanned, the profile appears on both screens: its owner confirms the login on their screen, then the second player can scan their own card. The technology used is completely different: **a FiNALE Aime reader cannot be reused.**

    !!! info "aic_pico"
        It is technically possible to use an [aic_pico]({{AIC_PICO_REPO}}), an open-source project that imitates a real Aime reader transparently for the game. It is much cheaper to produce, but would need a good deal of tinkering to be connected to the corresponding DB9 port on the ALLS.

    Last-generation Aime readers are not that rare anyway, and are often sold **as a combo with the VFD** that we also need. This generation is technically compatible with electronic payment, but even in Japan, that feature is almost never used: operators prefer to install their own, more flexible payment terminal.

## The connectors

Connecting to the ALLS is extremely simple:

* Aime reader: **COM1**
* VFD: **COM2**

Both COM ports are physical DB9 ports on the ALLS. However, your Aime + VFD combo probably did not come with a ready-to-use DB9 cable: **you will have to crimp your own cables**, from the Aime reader and VFD connectors to the DB9.

!!! lightbox
    ![Front face of an Aime reader from a Star Horse 4 cabinet](../resources/images/step-4-aime-reader/front-aime-reader-from-star-horse-4.jpg)
    ![Rear face of an Aime reader from a Star Horse 4 cabinet](../resources/images/step-4-aime-reader/back-aime-reader-from-star-horse-4.jpg)

### Preparing the DB9 cable

Take your female-female DB9 cable and **cut it in two** to expose the wires. Two options:

* **Cut a long cable in the middle**, long enough once cut to run cleanly from the ALLS to the center of the cabinet, where the combo will be installed.
* **Cut about twenty centimeters** from one connector, then reach the ALLS with a simple male-female DB9 cable of the right length.

*The second option is recommended*: no bulky cable length while crimping, an easier installation, and a combo that is easier to unplug for maintenance.

!!! lightbox
    ![Female DB9 cable cut open, sheath removed to expose the internal wires](../resources/images/step-4-aime-reader/cut-cable.jpg)

### Identifying the right wires

Wire colors vary from one DB9 cable to another: do not rely on the colors in the photos. **The safest way is to use a multimeter in continuity mode**:

* Put one multimeter probe into the hole of the female DB9 plug matching the pin you want (see the diagrams below).
    * If the probe is too wide, attach a male Dupont wire to it.
* With the other probe, touch the wires one by one until you hear the beep. **The wire that beeps matches your pin**: mark it.
* Once all the useful wires are identified (*3 for the Aime reader, 5 for the VFD*), cut the others.

### Aime reader cable

The Aime reader is the simpler of the two: **only 5 of its 8 pins are used**. All 5 wires are crimped with **female JST-PH** pins and inserted into an **8-pin JST-PH** connector:

1. **3 signal wires**: the ones you identified on the DB9 cable.
2. **2 "flying" power wires**: a **red** wire on the **5V** pin and a **black** wire on the **GND** pin right next to it. They are not connected to the DB9: leave their other end free for now, it will be joined with the VFD's on a single connector (see [Grouping the power wires](#grouping-the-power-wires)).

![Pin mapping between the Aime reader's JST-PH connector and the female DB9 port](../resources/images/step-4-aime-reader/aime-db9-jst-mapping-en.svg){ width="80%" }

!!! warning "Crimp both GNDs"
    Two of the pins to crimp are GND (common ground). In theory one would be enough, but **wire both**: one goes with the 5V to power the reader, the other is connected to the DB9 as the RS-232 standard requires.

### VFD cable

The VFD has a 7-pin connector, and **all of its pins must be crimped**.

The method is almost identical to the Aime reader's, with two differences:

* The VFD connector is a JST-**X**H (not JST-PH): crimp the wires with **female JST-XH** pins.
* **5 signal wires** instead of 3: you also need to connect the `CTS` and `RTS` signal wires to the serial port.

As for the Aime reader, add **2 flying power wires**, red on **5V** and black on **GND**, leaving their other end free.

![Pin mapping between the VFD's JST-XH connector and the female DB9 port](../resources/images/step-4-aime-reader/vfd-db9-jst-mapping-en.svg){ width="80%" }

### Grouping the power wires

The Aime reader and the VFD now each have a pair of flying 5V/GND wires. **Join them in a Y on a single 2-pin JST-SM connector**: both red wires (5V) together on one pin, both black wires (GND) together on the other. Placed next to your two DB9 cables, this connector makes the combo easier to install and to unplug for maintenance.

Congratulations, your cables for the ALLS are ready!

!!! lightbox
    ![The two finished female DB9 cables, with their JST connectors for the Aime reader and the VFD](../resources/images/step-4-aime-reader/finished-cables.jpg)

### Securing the cables

Plug both cables into their connectors, then **fasten them to the back of the combo** so they are under no strain. Even well crimped, these connectors remain fragile.

!!! lightbox
    ![The cables plugged in and then fixed at the back of the Aime reader + VFD combo to avoid any strain on the connectors](../resources/images/step-4-aime-reader/cables-secured-behind-combo.jpg)

## Installing it on the cabinet

Use [the 3D model designed by SpiralGlide](spiralglide-resources.md#aime-reader-mount), which attaches to the cabinet using the existing screws of the acrylic panel. Designed for the Star Horse 4 Aime reader, it fits **without any destructive modification**, using the holes already there for the Aime readers. It also includes a spot for the 1P SELECT and 2P SELECT buttons.

!!! lightbox
    ![The Aime reader mount printed and fitted into the front of the center tower, with the Aime reader in place. Photo by SpiralGlide](../resources/images/spiralglide-resources/maimai-aime-reader-installed.jpg)

## Final step

Once the combo is installed on the front of the cabinet, all that's left is to plug the two cables into the ALLS DB9 ports. As a reminder: **Aime on COM1**, **VFD on COM2**.

Then don't forget to **connect the 5V and GND** of both connectors to the power supply installed in [step 1](step-1-alls-and-psu.md).

**Check that everything works** before moving on.

## In summary
!!! tldr "The big picture"
    For the Aime reader and the VFD:

    * Make a female DB9 cable for the Aime reader.
    * Make a female DB9 cable for the VFD.
    * Secure the cables so they don't move.
    * Install the combo on the front of the cabinet.
    * Plug both connectors into the ALLS.
    * Connect the power supply.

---

Let's move on to [Step 5: Headphone Jacks and Sound System](step-5-audio-headphones.md).
