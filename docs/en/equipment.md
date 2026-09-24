---
title: "🛒 Shopping list"
---

# 🛒 Shopping list: the hardware you need

!!! tip "Don't need the detail?"
    The [purchase checklist](equipment-checklist.md) lists every item to buy, without the explanations.

## Preamble
For each part, **the most suitable option is highlighted**, whether for its ease of installation, price or availability. *Alternatives are mentioned where they exist*, but the guide assumes you chose the main option and does not cover them.

!!! info "The Japanese second-hand market"
    Unfamiliar with the Japanese second-hand market? See the appendix [The Japanese second-hand market](secondhand-market.md).

## Mandatory hardware

<div class="equipment-card" markdown>

### ALLS HX2
* Where: JDirectItems Auction
* Info: it is the PC used by DX, and few other cabinets use this specific model: **depending on the period, it can be hard to find**.

*Alternative*: **ALLS MX2**

* Where: JDirectItems Auction
* Info: easier to find, and its internal software is technically compatible with DX.

!!! info "Storage space"
    Depending on the game it originally ran, your ALLS may only contain a 64 or 128 GB SSD, **not enough to install the game**. A secondary drive (named "SUB STORAGE"), usually 500 GB, is mandatory. If your ALLS does not have one, you will need to get one.

</div>

<div class="equipment-card" markdown>

### Sega IO4 I/O board
* Where: JDirectItems Auction
* Info: easy to find, it has equipped every Sega cabinet for several years. **Be careful not to confuse it with an IO3**, which looks very similar: the safest check is the **dip switches on top of the PCB**, which only the IO4 has.

!!! info "IO4 variants"
    There are several IO4 variants:

    - **JVS-compatible**, with a USB-B port and a USB-A port for daisy-chaining;
    - **without JVS**, with a simple micro-USB port to plug into a regular USB port.

    On maimai DX, the IO4 connects to the ALLS over regular USB, through the micro-USB port: **JVS support is useless**. IO4s without JVS are usually a little cheaper, but in theory every variant works.

</div>

<div class="equipment-card" markdown>

### Aime reader (Gen. 3)
* Where: JDirectItems Auction
* Info: **you absolutely need a generation 3 reader**, often sold with the VFD built in. You can recognize it by its Aime logo, which differs from the previous generation's. It is not very rare: you often find ones taken from Star Horse 4 cabinets.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } HDX touchscreen
* Where: [On the HanDevice Discord]({{DISCORD_HANDEVICE}})
* Info: a touchscreen designed by an individual, originally as a "game-pad" for playing a DX simulator at home. HanDevice does not officially sell a conversion kit, but you can [contact the maker on their Discord]({{HANDEVICE_DISCORD_CONTACT_MESSAGE}}) to ask for an offer covering **the touchscreen and the HanDevice IO** (its dedicated I/O board). The upside of this board: it exposes a **UART serial port**, which lets you connect it to the ALLS HX2 without converting the signal.

*Alternative*: **2x**{: .quantity-emphasis } **Yuancon conversion kit - based on an ADX touchscreen**

* Where: [On the Yuancon website]({{YUANCON_CONVERSION_KIT_PAGE}})
* Info: each Yuancon kit includes a touchscreen and eight buttons, enough to convert one side of the cabinet. They are equivalent to the HDX, with one catch: **their I/O board has no serial port**. It only communicates over USB-CDC, a signal that a simple RS-232 converter cannot adapt for the ALLS HX2. It is possible through a software proxy, [maitouch_rs]({{MAITOUCH_RS_REPO}}) by [4ndr3w]({{GITHUB_4NDR3W}}) on GitHub, running on a Raspberry Pi placed between the ALLS and the ADX, but that complexity is not covered in this guide. *With this alternative, you do not need the buttons from the next item.*

</div>

<div class="equipment-card" markdown>

### **16x**{: .quantity-emphasis } HDX buttons
* Where: [On the HanDevice Discord]({{DISCORD_HANDEVICE}})
* Info: the gameplay buttons for the ring. The FiNALE ones are technically compatible, but the feel on DX is completely different, and much better: **the upgrade is well worth it**. You need eight per player, so sixteen in total. *This is a wear part*: a few spare buttons can come in handy.

*Alternative*: **16x**{: .quantity-emphasis } **"Rabbit" buttons**

* Where: [On the official Taobao shop]({{TAOBAO_OFFICIAL_SHOP_LISTING}})
* Info: fairly close to the official maimai DX buttons, they are an excellent alternative.

!!! failure "Don't buy the counterfeits!"
    Taobao and AliExpress sell much cheaper generic buttons that look very similar. **Do not give in to the temptation of saving a few euros**: it is the worst purchase you can make. Unlike HanDevice or Rabbit buttons, they are of **very** poor quality, pile up problems and wear out fast. Go for quality buttons from a reliable seller.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } OBSF-24TR button

* Where: [SmallCab]({{SMALLCAB_SANWA_OBSF_24TR}}) or [Jammastar]({{JAMMASTAR_SANWA_OBSF_24TR}})
* Info: the "triangle" sort buttons for players 1 and 2, in the center of the cabinet, above the Aime reader. Typically **blue for player 1 and red for player 2**.

*Alternative*: ... literally any other buttons

* Where: AliExpress, Amazon, etc.
* Info: the original cabinet uses genuine Sanwa OBSF-24TR, but these buttons are barely used in game: **no need to invest in quality**. Any counterfeit will do just fine.

</div>

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } 4-port USB hub

* Where: Amazon, AliExpress, your favorite shop
* Info: on a real maimai DX, one of the 4 USB ports on the ALLS motherboard is reserved for a 4-port USB hub. This hub hosts the two QR-code reader cameras and the RS-232/USB adapter for the player 1 and 2 LED controllers. **Any USB hub will do.**

</div>

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } 5V/12V switching power supply

* Where: Amazon, AliExpress, electronic component distributors
* Info: unlike the RingEdge 2, the ALLS does not power external peripherals. This power supply takes over that role: among other things, it powers the IO4, the Aime reader, the VFD and the LED controller proxies. You need a **dual-output 5V and 12V** model, in a metal enclosure with screw terminals, such as the Mean Well RD-35A or RD-50A. **Do not reuse the cabinet's original power supplies** instead.

</div>

Other small purchases are needed for the rest of the guide: they are grouped under [Small supplies](#small-supplies).

## Optional hardware for the camera and QR-code readers

The player camera and the QR-code readers are **optional**. If you want to install them, here is the hardware you need.

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } Player camera

* Where: Amazon, AliExpress, your favorite shop
* Info: **any cheap USB webcam will do**, as long as it is UVC. *If it works as soon as it is plugged in, with no specific driver, it is probably compatible.* The original camera films at 1280x960, a resolution barely used in game: no need to spend a fortune.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } QR-code camera

* Where: Amazon, AliExpress, your favorite shop ([example of a compatible camera]({{BUY_EXAMPLE_QR_CODE_CAMERA}}))
* Info: **the game is very strict about these cameras.** They must be UVC, film at 640x480 at 30 fps in YUY2 format, with a 50 degree field of view. External lighting is also needed (see [Lighting](#lighting)).

</div>

## Small supplies

These small, cheap purchases, needed over the course of the steps, can be found in your favorite shop (Amazon, AliExpress, ...).

<div class="equipment-supplies" markdown>

### Cables

* **1x**{: .quantity-emphasis } **HDMI to DVI-D cable (3 m)**
    - Connection from the ALLS to the Player 1 screen.
* **1x**{: .quantity-emphasis } **DVI-D to DVI-D cable (2 m)**
    - Connection from the ALLS to the Player 2 screen. Your FiNALE may already have one natively.
* **1x**{: .quantity-emphasis } **DB-9 Female-Female cable**
    - As short as possible: it will be cut in two to make the Aime reader and VFD connectors.
* **4x**{: .quantity-emphasis } **DB-9 Male-Female cable (3 m)**
    - Extensions to the ALLS for the Aime reader, the VFD and the player 1 and 2 touchscreens.
* **1x**{: .quantity-emphasis } **IEC C-13 cable (2 m)**
    - Plugged into the ALLS, then cut at the plug end to be wired directly to the cabinet's mains supply.
* **2x**{: .quantity-emphasis } charging **micro-USB cable**
    - To power the two LED controller proxies: the end opposite the Pico is cut off, red wire to 5V and black wire to GND on the power supply installed in [step 1](step-1-alls-and-psu.md).

### Electronics

* **2x**{: .quantity-emphasis } **TTL to RS-232 converter with female DB-9** ([example]({{BUY_EXAMPLE_TTL_RS232_CONVERTER}}))
    - To connect each touchscreen's I/O board (players 1 and 2) to its DB-9 port on the ALLS.
* **2x**{: .quantity-emphasis } **Raspberry Pi Pico** ([example]({{BUY_EXAMPLE_RASPBERRY_PI_PICO}}))
    - To build the LED controller proxies. To avoid any soldering, prefer a version with pre-soldered pins. **Careful: the pins must be soldered facing down, not up.**
* **2x**{: .quantity-emphasis } **Pico-2CH-RS232** ([example]({{BUY_EXAMPLE_PICO_2CH_RS232}}))
    - To build the LED controller proxies.

### Hookup wire

* **Flexible hookup wire (AWG 20)**
    - Several cables need crimping throughout the guide: plan a good supply, ideally in several colors.

### Lighting

*Only if you install the optional cameras.*

* **1x**{: .quantity-emphasis } **12V warm white LED strip**
    - Lighting for the player camera.
* **1x**{: .quantity-emphasis } **12V common-anode RGB LED strip**
    - Lighting for both QR-code readers: one common anode and one cathode per color. About 20 cm of strip is enough.
* **1x**{: .quantity-emphasis } **12V red LED with built-in resistor**
    - Tells players the camera is filming. **A bare LED would burn out** on 12V: pick a model rated for that voltage or, failing that, a separate 2.2 to 4.7 kOhm resistor.

### Connectors

* **1x**{: .quantity-emphasis } **Molex Mini-Fit Jr. 2x7-pin female connector** ([example]({{BUY_EXAMPLE_MOLEX_MINI_FIT_JR_CONNECTOR}}))
    - To cleanly connect the power connector that used to be plugged into the RingEdge 2.
* **30x**{: .quantity-emphasis } **Molex Mini-Fit Jr. female crimp pin**
    - To go with the previous connector.
* **1x**{: .quantity-emphasis } **JST-RA 2x10-pin female connector**
    - For the IO4's CN9.
* **30x**{: .quantity-emphasis } **JST-RA female crimp pin**
    - For CN9 and the cables to add on the IO4's CN3.
* **2x**{: .quantity-emphasis } **JST-SM 8-pin female connector**
    - The ends of the billboard lighting harness, Player 1 side and Player 2 side, to connect to the original JST-SM connectors.
* **2x**{: .quantity-emphasis } **JST-SM 2-pin connector, male + female pair**
    - Ideal for making your own connectors and simplifying your life. Failing that, plain JST-XH will also do.

For the other connectors, rather than buying each part number individually, **get an assortment kit per connector type**. They are easy to find on Amazon or AliExpress, with several housing sizes, both genders (male/female) and a batch of crimp pins. Here is what you need in each:

**JST-XH kit**

* **20x**{: .quantity-emphasis } 2-pin male connector
* **20x**{: .quantity-emphasis } 2-pin female connector
* **2x**{: .quantity-emphasis } 7-pin female connector
* **1x**{: .quantity-emphasis } 7-pin male connector
* **2x**{: .quantity-emphasis } 8-pin female connector
* **1x**{: .quantity-emphasis } 9-pin female connector
* **1x**{: .quantity-emphasis } 9-pin male connector
* **50x**{: .quantity-emphasis } male crimp pin
* **50x**{: .quantity-emphasis } female crimp pin

**JST-PH kit**

* **2x**{: .quantity-emphasis } 4-pin female connector
* **1x**{: .quantity-emphasis } 8-pin female connector
* **30x**{: .quantity-emphasis } male crimp pin
* **30x**{: .quantity-emphasis } female crimp pin

</div>

!!! abstract "Work in progress"
    This list is incomplete and will be expanded as the guide is written. Still to be added, once the details are known:

    - **2x**{: .quantity-emphasis } Jack sockets for the headphones and the cables that go with them
    - **2x**{: .quantity-emphasis } Sound amplifiers for the headphones

---

!!! warning "Check your hardware before you start"
    **Receive and test all the hardware you ordered before starting the conversion.** It will save you a lot of headaches: if a problem comes up, you can immediately rule out a faulty part.

---

!!! tip "Here is the simplified checklist"
    Want to tick off your purchases as you go, without diving back into the detail? Use the [purchase checklist](equipment-checklist.md).

---

Now that you have the hardware, let's start with [Step 1: Replacing the Central PC (ALLS)](step-1-alls-and-psu.md).
