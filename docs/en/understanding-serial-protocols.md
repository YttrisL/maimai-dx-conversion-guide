---
title: "Understanding serial protocols"
---

# 🎓 Short course: understanding "serial" protocols

This guide mentions several communication protocols: **UART**, **RS-232**, **RS-485**, **JVS** and **USB-CDC**. If you are new to these technologies, this appendix offers a short course to understand what they are for, what sets them apart, and how two devices manage to "understand each other".

## 1. The common foundation: talking "serially"

A "serial" port sends data one bit at a time, in single file, over a single wire (as opposed to a "parallel" port, which uses several wires at once). Each packet of information ("a byte") is wrapped in a small frame, a bit like a letter in an envelope:

![UART frame: Start bit, 8 data bits D0 to D7, Stop bit, framed by the idle line](../resources/images/serial-protocols/uart-framing-en.svg)

The *Start* bit warns the receiver that a letter is coming, the next 8 bits are the content, and the *Stop* bit closes the envelope (there are variants with more or fewer bits, but "8 data bits + 1 Stop bit" is by far the most common). This splitting has a name: it is a **UART** frame (*Universal Asynchronous Receiver-Transmitter*), from the name of the chip that produces it - UART therefore originally refers to an electronic component, but by extension it is also used to refer to this splitting itself. It lives at the level of an electronic chip (a microcontroller, for example), with small "logic" voltages (often called *TTL* for *Transistor-to-Transistor Logic* - 0V for a "0", 3.3V or 5V for a "1"). RS-232 and RS-485, presented right after, are just two different ways of *electrically* translating this same splitting into bits to send it over a longer or more reliable cable - like the same letter that can be handed to two different postal services, without changing what is written on it.

**The role of "the clock":** to read a sequence of bits correctly, you have to know at which precise instant to look at the line - a bit like a metronome keeping time for musicians. In electronics, this timing signal is called a **clock**: nothing to do with a wall clock that tells the time, it is simply a signal that repeats "now, now, now..." at a fixed interval, to tell each device "read the next bit". This is exactly what the "A" in UART means, for *Asynchronous*: there is **no** wire dedicated to this clock signal. Each device has to guess the right rhythm on its own, thanks to its own internal clock, set in advance to the agreed rate.

**How the communication is established:** the two devices must therefore agree, in advance, on this reading speed: it is the famous **baud rate** (e.g. "9600 baud" = 9,600 bits per second). No negotiation happens on the wire: if the two ends are not set to the same speed, each reads the wrong bit at the wrong time. It is a convention fixed in advance, not a handshake.

## 2. RS-232: point to point

RS-232 translates this same UART bit splitting into higher *and inverted* voltages (typically between -15V and +15V, often ±5 to ±12V in practice - a logic "1" becomes a negative voltage, a "0" a positive voltage), to support longer cables than the weak 3.3V/5V of a raw UART. It only links **two devices**, each with its own transmit wire:

![RS-232: point-to-point link between two devices, TX crossed with RX, GND connected to GND](../resources/images/serial-protocols/rs232-point-to-point-en.svg){ width="65%" }

The "TX" (transmit) of one side connects to the "RX" (receive) of the other - this crossing is what a [Null Modem adapter](glossary.md#communication-and-protocols) does. RS-232 is not limited to these voltages either: it also standardises the connector (the famous "DB9" port) and a few additional control wires, which is precisely what makes this kind of crossover cable possible.

In this guide, RS-232 is the protocol the game uses to drive the [LED controllers](step-6-lighting.md) and to talk to the *original* touchscreens, as well as to retrieve the information from the Aime reader and tell the VFD what to display. It is a very widely used standard in the arcade world.

**The DB9 connector:** this is the small trapezoidal 9-pin connector on two rows that RS-232 made almost universal. It is often wrongly confused with a "reversed" VGA port. It is the one found on the RingEdge 2 and on the ALLS. Of the 9 pins, only three really matter to us here: **TX** (transmit), **RX** (receive) and **GND** (the ground, the common voltage reference) - as on the point-to-point diagram seen above. The other pins (DTR, DSR, RTS, CTS, DCD, RI) are for optional control signals (flow negotiation, carrier detection...), rarely used in the arcade field.

![Male DB9 connector, front view, with pins 2 (RX), 3 (TX) and 5 (GND) highlighted](../resources/images/serial-protocols/db9-connector-en.svg){ width="65%" }

A "female" connector has the same pin numbers, but recessed rather than in points, and mirrored horizontally. This is why a crossover cable (Null Modem) must explicitly swap pins 2 and 3 from one end to the other: connecting two devices "straight through" (pin 2 to pin 2, pin 3 to pin 3) would connect two TX together and two RX together, which does not work. The Transmit (Tx) of one device must be linked to the Receive (Rx) of the other, and vice versa.

## 3. RS-485: the multi-device bus

RS-485 also translates this same UART bit splitting, but with a different trick from RS-232: instead of a "high/low" wire (meaning "electrically charged or not") compared to ground, it uses a **differential pair**, at voltages close to the starting TTL (two wires, A and B, whose voltage difference between them is compared rather than against ground). This makes it much more resistant to noise over long cables, and above all, it lets you connect **several devices to the same pair of wires**:

![RS-485: shared bus on an A/B differential pair, with the host (master) and two nodes (slaves) connected to the same wires](../resources/images/serial-protocols/rs485-bus-en.svg){ width="80%" }

But RS-485 says nothing about *who* has the right to speak at what time: with no rule, the devices would trample each other and the signals would mix. It is this ability to chain several devices on the same two wires, combined with the protocol that will handle this rule, that makes it the ideal medium for JVS (see next point).

## 4. JVS: a protocol built on top of RS-485

Be careful not to confuse the levels: RS-485 only defines the *electrical* aspect (how the bits travel on the wire). **JVS** is another layer on top, which defines a common language (addressing, commands) so that the game and the I/O board understand each other.

**The link with the UART from point 1:** JVS does not reinvent the way bits are sent. It uses exactly the same UART frames (Start / 8 data bits / Stop) seen above, simply transported electrically over RS-485 - the *nature* of the packets does not change. What JVS adds is a standardised convention on the *content* of these UART bytes: a JVS packet always starts with a synchronisation byte, then an address byte (which designates the recipient), a length, the command data, and a checksum to detect errors. The game and the I/O board therefore exchange simple UART bytes, like any other serial device - it is by interpreting their content according to the JVS rules that the two ends know what it is about:

![JVS layer stack: JVS (protocol, content of the bytes) transported over UART frames (framing, shape of the bytes), themselves transported electrically over RS-485](../resources/images/serial-protocols/jvs-layers-en.svg){ width="80%" }

**How the communication is established:** at startup, the game (the host) begins with a reset command sent to all the devices on the bus at once. It then asks, again to all at once, "whoever does not yet have an address, answer me"; thanks to an additional wire chained from one device to the next, only one device at a time is allowed to answer, which lets the host assign them an address one by one (JVS auto-addressing). Once the addresses are handed out, the host queries each board in turn ("does this board have anything new?"): it is a **master/slaves** dialogue, where only the host takes the initiative. It is typically the I/O board that speaks JVS in an arcade system; despite its USB cable, it actually always communicates over an RS-485 serial link under the hood.

## 5. USB-CDC: the disguise

USB is a whole other family of protocol: packet-based, much faster, and **negotiated** - on connection, the device presents itself to the computer and describes its own capabilities ("USB enumeration"). The **CDC** class (*Communication Device Class*) is a special case where the device tells the computer: *"treat me like an RS-232 port"*. The computer then creates a virtual COM port, but the real transport stays packet-based USB:

![USB-CDC: the ADX touchscreen sends USB packets presenting themselves as a serial port, the computer exposes them as a virtual COM port](../resources/images/serial-protocols/usb-cdc-en.svg){ width="80%" }

It is convenient for software compatibility: a program that only knows how to talk to RS-232 works without modification. But be careful, the disguise does not *create* a bottleneck: it is rather the opposite that is a problem. The "9600 baud" rate displayed by the virtual COM port is just a facade, the USB hardware behind it keeps going at full speed - it is when this fast data then has to be sent on to a device that is *actually* limited to 9600 baud (like the game, further down the chain) that the bottleneck appears. It is one of the problems encountered with the ADX touchscreens, an alternative mentioned in the [Shopping list](equipment.md).

## Quick summary

| Protocol | Layer | Topology | Establishing the link |
|---|---|---|---|
| UART | Framing + logic (TTL, 3.3V or 5V) | Point to point (before any electrical medium) | Baud rate fixed in advance on both sides - the common foundation for everything that follows |
| RS-232 | Electrical + connector (translates UART) | Point to point (2 devices) | Same as UART, simply carried at higher voltages |
| RS-485 | Electrical (translates UART) | Bus (several devices) | Same as UART; handles neither addresses nor turn-taking, that comes from the layer above (e.g. JVS) |
| JVS | Protocol (above UART, transported over RS-485) | Master/slaves chain | The host resets the bus then hands out the addresses one by one at startup |
| USB-CDC | Protocol (above USB) | Point to point | Negotiated on connection (USB), then disguised as a serial port |

---
