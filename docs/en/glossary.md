---
title: "Glossary"
---

# 📖 A Short Glossary for Beginners

So you don't get lost in the technical terms:

## The PC and cabinet boards

* **ALLS (MX2 / HX2):** the name of the standard computer Sega uses to run its recent games. It replaces FiNALE's old PC (called the RingEdge 2). It comes [in several variants (UX, HX, UX2, HX2, etc.)]({{ARCADE_DOCS_ALLS_VARIANTS}}), each with its own hardware specifications. The model that goes with maimai DX is the ALLS HX2.
* **I/O board:** the electronic board (a [PCB](#wiring-and-electronics)) that bridges the PC and the cabinet. It picks up button presses. On *maimai FiNALE*, it is a **Sega IO3**. For *DX*, it must be replaced with a **Sega IO4**. Most I/O boards communicate with the system using the [JVS](#communication-and-protocols) protocol.
* **Aime / VFD:** the contactless (NFC) card reader players use to save their profile. The *VFD* (Vacuum Fluorescent Display) is the small retro-style display (often green or blue) that shows the credit balance or other text information.
* **Dip switches:** a row of tiny miniature switches mounted directly on an electronic board (like the IO4), which let you configure certain hardware settings without software, simply by flipping them to "ON" or "OFF" by hand. It is also a good visual way to recognize an IO4: it has them on the top of its PCB, unlike the IO3, which looks very similar.

## Wiring and electronics

* **PCB:** short for *Printed Circuit Board*. It is the generic term for an electronic board, like the I/O board or an LED controller.
* **Pinout:** the map that tells you what each pin (each wire, each "pin") of a connector does. A pinout tells you, for example, that pin 51 of a connector controls the coin blocker, and nothing else.
* **Molex connector:** a type of power connector very common in computing, recognizable by its hard plastic housing (often white or black) and its thick pins. On the *RingEdge 2*, this is the connector through which 12V/5V/3.3V went to the rest of the cabinet.
* **PSU:** short for *Power Supply Unit*. It is the component that transforms an input current, most often 100/220V AC, into voltages usable by electronic hardware. Typically 12V, 5V, 3.3V.
* **Switching power supply:** a PSU that converts one voltage into another (for example 24V into 5V) compactly and efficiently, by "chopping" the current at very high frequency rather than going through a big traditional transformer. This is what the `SW REGU` references on the [wiring diagrams](wiring-diagrams.md) refer to. Enclosed models with screw terminals from the **Mean Well** brand are so common that the name is often used for this kind of power supply, like the one installed in [Step 1](step-1-alls-and-psu.md).
* **FET:** short for *Field-Effect Transistor*. It is an electronic component that acts as an electrically controlled switch (it can be turned on/off from a control circuit, with no manual intervention). In this guide, "the FET data" simply refers to the information sent by the game to drive certain additional lighting channels (the central ring and the body of the cabinet).
* **Photo-interrupter:** a small optical sensor (a mini fork with a light emitter and receiver) used inside the buttons to detect that they are pressed, with no mechanical contact that wears out.

## Communication and protocols

* **COM ports (COM1, COM3...):** these are the virtual "addresses" (or channels) the PC uses to communicate with certain specific peripherals (like the touchscreens or the *Aime* card reader). Today, most COM-port connections are done over virtual ports; however, an ALLS HX2 has four physical connections for plugging in the cabinet's hardware.
* **Serial port / RS-232:** a wired communication standard that sends data one bit after another over a single wire. Despite its age, it is still a very widespread industrial standard today, particularly in arcade, automation and instrumentation. It is the protocol the *DX* game uses internally to talk to certain peripherals, such as the touchscreens or the LED controllers.
* **Baud:** the unit that measures the speed of a serial port. "9600 baud" means about 9,600 small pieces of information per second, a rate much lower than USB's, but perfectly suited to the uses this kind of serial link is still employed for.
* **USB-CDC:** a USB device class (*Communication Device Class*) that lets a USB device present itself to the computer as a regular RS-232 serial port. It is convenient for software compatibility, but the real hardware behind it may run at a very different rate from the one it announces, which can create data traffic jams if the two ends of the chain are not matched to each other.
* **JVS:** the standard protocol used by most Japanese arcade cabinets (Sega, Namco...) to make the game system communicate with the I/O board (buttons, sensors, coin mech). Contrary to what its USB cable suggests, a JVS board like the IO4 actually always communicates over a serial link (the JVS protocol itself is based on RS-485). JVS is the standard that succeeded JAMMA when cabinets moved from low-definition to later generations.
* **FTDI chip:** the electronic component found in most off-the-shelf "USB-to-Serial" adapters, which converts an RS-232 serial port to USB (and vice versa). It is such a widespread part that "FTDI" is often used as a synonym for a USB-to-Serial adapter.
* **Null Modem adapter:** a small adapter that crosses certain wires of a serial connection (the transmit and receive wires). It is a kind of "coupler": it lets two "serial" devices talk directly to each other, without going through a real modem as this standard originally intended.
* **UVC (USB Video Class):** a standard that lets a webcam work directly once plugged in, with no particular driver to install. The *DX* QR-code readers require a UVC webcam recording in exactly 640x480.

## Computing and Linux

* **Proxy:** in this guide, it is not a web server, but a small computer (or program) placed between two incompatible devices to "translate" their exchanges on the fly, without either of them noticing. This role is also sometimes called a **MITM**. It is the role the Raspberry Pi plays in [Step 6](step-6-lighting.md).
* **MITM (Man in the Middle):** literally "man in the middle". A term from the world of computer security for a device or program placed between two communicating parties, able to read, modify or translate their exchanges. The term is often associated with a malicious attack, but here it refers to a perfectly legitimate use: a trusted intermediary that adapts the communication between two devices to make them compatible.
* **Buffer:** a small temporary storage area where data is accumulated before being processed or sent all at once, rather than piecemeal. It is a common technique in this kind of communication bridge, for example to group commands together before transmitting them.
* **udev rule / Symlink:** on Linux, a USB port can change name on every reboot (for example going from `/dev/ttyUSB0` to `/dev/ttyUSB1`). A *udev* rule lets you pin a stable, predictable name (a "shortcut", or *symlink*) for a specific device, for example to be sure that a given cable always keeps the same name.
* **systemd service:** on Linux, a program that starts automatically and in the background as soon as the machine boots, with no manual intervention. This is what lets a program start on its own every time the cabinet is powered on, without having to launch it by hand.

## Playing outside a cabinet

* **Pad:** a custom controller, usually compact, that reproduces the buttons and the touch ring of *maimai DX* so you can play a simulator that reproduces the feel of maimai DX at home, without an arcade cabinet. It is a different approach from this guide's, which aims to run real cabinet hardware.

## Japanese arcade culture

* **Game center:** the Japanese term for an arcade, that is, an establishment where video game cabinets are installed, including *maimai DX*. Unlike most Western countries where arcades have declined sharply, game centers remain a popular outing in Japan and a pillar of video game culture, with large chains such as Round1, Taito Station or GiGO (formerly Club Sega, renamed after GENDA's acquisition of Sega's arcade division in 2020).

---
