---
title: "🛠️ 1 - ALLS and PSU"
---

# 🛠️ Step 1: Replacing the Central PC (ALLS)

## Technical background

??? note "Click here for the technical explanation"
    The old *RingEdge 2* PC cannot be used to run *DX*. You need an **ALLS HX2** PC.  
    Beyond the newer, more powerful hardware, the operating system is radically different between a RingEdge 2 and an ALLS HX2. **The replacement is mandatory.**
    
    You can also use an **ALLS MX2**, whose specifications exceed the minimum required for *DX*. In principle, every second-generation ALLS (those whose model name ends in 2) is software-compatible, but some models lack the specifications to run the game properly. The ALLS X2, for example, is compatible but does not have the power required for a pleasant experience. These models can still be upgraded, but the job quickly gets complicated and it is often simpler to get a suitable model from the start.

    An ALLS is very similar to a modern gaming PC: its architecture does not fundamentally differ from that of a regular PC. Besides the usual components, you will notice a recessed USB port on top of the motherboard. It is meant to hold the "keychip", the USB key that identifies the cabinet's owner on the official Sega network and decrypts the game data. In addition, second-generation models include two expansion cards, which provide three RS-232 serial ports and a 2.5mm audio jack. These serial ports are used, together with the motherboard's COM port, to connect the Aime reader, the VFD and the touch panels of both screens. The jack, for its part, is dedicated to one of the two player headphone outputs.

    !!! tip "The ALLS power supply"
        The C13 connector on the ALLS power supply can be connected to 100V, 110V, 220V or 240V alike: the power supply switches voltage automatically. No external transformer is needed.

    !!! warning "Storage"
        An official *DX* ALLS HX2 contains two drives: a 120GB SSD and a 500GB hard drive (named "SUB STORAGE"). The game expects to find both storage spaces, and for *DX*, the SSD alone is not enough. If your ALLS has only one drive, you will need to get a second one and install it inside. (**Note:** see the [ALLS HX2 Service Manual](../resources/pdfs/alls-hx2-service-manual-full.pdf) to learn how to install the SUB STORAGE. Plugging in the drive is not enough: a software step, detailed in the manual, is also required.)

## Installing it in the cabinet

--8<-- "includes/wip-en.md"

## Connections

Here is the plate from the [official maimai DX manual](../resources/pdfs/maimai-dx-instruction-manual-full.pdf) (page 128) detailing the full set of connectors on an ALLS HX2. Let's go through each connection in detail.

!!! lightbox wide
    ![Rear view of an ALLS HX2 and detail of its connectors.](../resources/images/step-1-alls-and-psu/alls-hx2-rear-connectors-en.jpg)

Most of the devices to connect to the ALLS are covered in more detail in the following sections: if in doubt about a connection, finish the corresponding chapter, then come back to this page. According to the official *DX* manual, the order of the USB ports matters.

### Internal PSU

- **C13 connector**: Mains connection, accepts any input voltage from 100V to 240V.

### Keychip

- **USB port**: Reserved for the keychip. It can **not** be used as a regular USB port.

### Motherboard

- **COM1 - DB9 port**: Aime reader
- **LAN1 - RJ45 port**: Network port, to be connected to the service router. The second network port is unused.
- **2.5mm audio jacks**:
    - **C/W**: Player 1 headphones
    - **FRONT**: Player 1 speakers
    - **REAR**: Player 2 speakers
- **USB**:
    - **USB 1**: SEGA IO4
    - **USB 2**: USB hub, to which the two QR code cameras and the `4x RS-232 to USB` hub for the two LED controllers are connected.
    - **USB 3**: Player camera
    - **USB 4**: Installation port, for a USB stick containing the game data to install.

### Graphics card

- **HDMI**: Connected to the player 1 screen via an HDMI - DVI-D cable.
- **DVI**: Connected to the player 2 screen via a DVI-D cable.
- **DisplayPort**: Unused, mirrors the player 1 video signal.

### Expansion cards

- **COM2 - DB9 port**: VFD
- **COM3 - DB9 port**: Player 1 touch panel
- **COM4 - DB9 port**: Player 2 touch panel
- **SIDE**: Player 2 headphones

## Power supply

While most components are fairly straightforward to connect, one essential RingEdge 2 connector has no equivalent on the ALLS: the one that powers the external peripherals.

On the RingEdge 2, next to the keychip port, a female 2x7-pin Molex Mini-Fit Jr connector comes out of the PC. It connects several parts of the cabinet to the RingEdge 2's internal power supply, including the IO3. To avoid rewiring this whole area, the ideal solution is to build a small adapter from an identical Molex Mini-Fit Jr connector. To do so, get a "Mean Well" type power supply able to provide 5V and 12V. The original connector also provides 3.3V, but no hardware in this area uses it.

!!! warning "Do not reuse the cabinet's power supplies"
    Among other things, this cable harness will power the IO4. While reusing the 5V supply would have little consequence, reusing the LEDs' 12V supply would be a mistake. To avoid backfeed current, the IO4 and the LEDs must each have their own power supply, as the IO4 is not designed to handle that much current.

!!! warning "Tie the grounds together"
    Don't forget to connect the ground of your new power supply to the ground of the cabinet's other power supplies. Do not leave the power supply floating: this can cause all sorts of unexpected problems. Simply connect the GND of your new power supply to the GND of one already in place.

![Female Molex Mini-Fit Jr 2x7 connector, front view from the contact side: pins 1 to 7 are GND, 8 to 10 are +12V, 11 to 13 are +5V and 14 is +3.3V](../resources/images/step-1-alls-and-psu/molex-minifit-jr-2x7-en.svg)

To wire the female connector, follow the diagram above. It is a front view of the female connector, the one you need to wire. The diagram shows the contact side: do not confuse it with the wire side.

- Pin 14: **3.3V** (optional, unused)
- Pins 13-11: **5V**
- Pins 10-8: **12V**
- Pins 7-1: **GND**

Connect these wires to the matching terminals of your Mean Well power supply, then install it in the cabinet. Screw it down firmly with wood screws: it must not be able to move. All that's left is to plug your homemade connector into the original cable.

## Summary
!!! tldr "The big picture"
    For the ALLS and the power supply:

    * Remove the RingEdge2
    * Install the ALLS HX2 in its place
    * Connect the various peripherals to the ALLS (see the following steps)
    * Build an adapter cable for the external power connector
    * Install the external power supply and the adapter cable in the cabinet, then plug in the existing connector

---

Let's move on to [Step 2: HDX Display and Touchscreens](step-2-touchscreen-display.md).
