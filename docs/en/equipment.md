---
title: "🛒 Shopping list"
---

# 🛒 Shopping list: the hardware you need

!!! tip "Don't need the detail?"
    The [purchase checklist](equipment-checklist.md) lists every item to buy, without the explanations.

## Preamble
For each of the parts listed below, the most suitable option is highlighted. This can be for several reasons: ease of installation, price or availability. *Where they exist, alternatives are mentioned.* This guide, however, assumes you have chosen the main option and will not dwell on those alternatives.

!!! info "The Japanese second-hand market"
    If the Japanese second-hand market and its buying options are unfamiliar to you, feel free to consult the appendix [The Japanese second-hand market](secondhand-market.md).

## Mandatory hardware

<div class="equipment-card" markdown>

### ALLS HX2
* Where: JDirectItems Auction
* Info: depending on the period, it can be fairly hard to find. It is the system used by maimai DX, and few other cabinets use it.

*Alternative*: **ALLS MX2**

* Where: JDirectItems Auction
* Info: this one is easier to find. It will, however, need a downgrade to be made compatible with maimai DX. That operation is not publicly documented.

!!! info "Storage space"
    Depending on the game your ALLS was natively running, it may only contain a 64 GB SSD.
    If that is the case, it will not be enough to install the game. You will then need to obtain an SSD of at least 128 GB, ideally 256 GB. Any SATA model will do.

</div>

<div class="equipment-card" markdown>

### Sega IO4 I/O board
* Where: JDirectItems Auction
* Info: easy to find, it has been used in every Sega cabinet for several years. Do not confuse it with an IO3, they look very similar. The best way to recognize an IO4 is to check that it has its dip switches on the top of the PCB.

!!! info "IO4 variants"
    There are several IO4 variants. Some, JVS-compatible, have a USB-B port and a USB-A port for daisy-chaining. Others have a simple micro-USB port meant to be connected to a regular USB port. In our case, the connection to the ALLS is done over regular USB, via the micro-USB port. JVS support is therefore useless for maimai DX.

    IO4s without JVS support are usually a little cheaper on the resale market, but in theory all variants are compatible with this conversion.

</div>

<div class="equipment-card" markdown>

### Aime reader (Gen. 3)
* Where: JDirectItems Auction
* Info: you absolutely need a generation 3 reader. It often comes with the VFD built in. You can recognize them by the Aime logo, which is different from the previous generation's. They are not very rare and you often find them coming from the Star Horse 4 cabinet.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } HDX touchscreen
* Where: [On the HanDevice Discord]({{DISCORD_HANDEVICE}})
* Info: this is a touchscreen created by an individual to provide a "game-pad" for playing a maimai DX simulator from the comfort of home. Officially, they do not sell a conversion kit, but you can [contact the maker via their Discord](https://discord.com/channels/1336383976721616897/1393421596190048266/1393822351094841375) to ask for an offer covering only the touchscreen **and** the HanDevice IO (their dedicated I/O board) that goes with it. This I/O board has the advantage of exposing a UART serial port that we can use to connect it directly to the ALLS HX2 without needing to convert the signal.

*Alternative*: **2x**{: .quantity-emphasis } **Yuancon conversion kit - based on an ADX touchscreen**

* Where: [On the Yuancon website](https://yuancon.store/controller/UPDATEKIT)
* Info: Yuancon offers conversion kits including the touchscreen and eight buttons, letting you convert one side of the cabinet. They are equivalent to the HDX except that their I/O board does not include a serial port: it only communicates over USB-CDC with the PC, which makes connecting it to an ALLS HX2 difficult, since that signal cannot be adapted directly with a simple RS-232 converter. It is nonetheless possible [via a piece of software acting as a proxy](https://gitea.farewell.dev/Yttris/maitouch_rs), running on a Raspberry Pi installed between the ALLS and the ADX, but that introduces a complexity we will not cover in this guide. (If you decide to go with this alternative, you do not need the extra buttons from the next item.)

</div>

<div class="equipment-card" markdown>

### **16x**{: .quantity-emphasis } HDX buttons
* Where: [On the HanDevice Discord]({{DISCORD_HANDEVICE}})
* Info: the gameplay buttons for the ring. The FiNALE buttons are technically compatible, but the feel is completely different (and much better) on DX. It is therefore well worth upgrading them. You need eight buttons per player, so sixteen in total, but it can be useful to buy a few spares. This is a wear part.

*Alternative*: **16x**{: .quantity-emphasis } **"Rabbit" buttons**

* Where: [On the official Taobao shop](https://item.taobao.com/item.htm?id=660013732031&skuId=5395223410039&spm=a1z10.1-c.w4004-24097871292.3.37221e09DSieDY)
* Info: fairly similar to the official maimai DX buttons, they are an excellent alternative.

!!! failure "Don't buy the counterfeits!"
    There are generic buttons, much cheaper, that look very similar, sold on Taobao or AliExpress. Do not give in to the temptation of saving a few euros; it is the worst purchase you can make. Unlike the HanDevice or Rabbit buttons, they are of **very** poor quality, pile up problems and have minimal durability. Go for quality buttons from a reliable seller.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } OBSF-24TR button

* Where: [SmallCab](https://www.smallcab.net/sanwa-obsf-24tr-p-2080.html) or [Jammastar](https://jammastar.com/gb/353-sanwa-obsf-24tr)
* Info: the "triangle" sort buttons for Player 1 and Player 2, located in the center of the cabinet above the Aime reader. Typically **blue for Player 1 and red for Player 2**.

*Alternative*: ... literally any other buttons

* Where: AliExpress, Amazon, etc.
* Info: these buttons are barely used in the game, and although they are genuine Sanwa OBSF-24TR on the original cabinet, there is really no need for a quality button given how little use they get. Any counterfeit will do just fine.

</div>

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } 4-port USB hub

--8<-- "includes/untested-en.md"

* Where: Amazon, AliExpress, your favorite shop
* Info: in a real maimai DX, one of the 4 USB ports on the ALLS motherboard is dedicated to a 4-port USB hub. This hub hosts the two QR-code reader cameras and the RS-232/USB adapter that the Player 1 and Player 2 LED controllers are connected to. Even if you do not want to use the QR-code cameras, you still have to plug in the hub, so that the LED controllers' RS-232/USB adapter is recognized natively by the ALLS operating system. Any USB hub will do. (See [Step 1: Replacing the Central PC (ALLS)](step-1-alls-and-psu.md) for the details.)

</div>

Other small purchases are needed for the rest of the guide, and are covered under [Small supplies](#small-supplies).

## Optional hardware for the camera and QR-code readers

Installing the player camera and the QR-code readers is optional, but if you want to do it, you will need the following hardware.

<div class="equipment-card" markdown>

### **1x**{: .quantity-emphasis } Player camera

* Where: Amazon, AliExpress, your favorite shop
* Info: any cheap USB webcam will do, as long as it supports UVC (if your camera works as soon as you plug it in without needing specific drivers, then it is probably compatible). On an original maimai DX, the camera has a native resolution of 1280x960 pixels, and that resolution is barely used in-game. No need, then, to spend a fortune.

</div>

<div class="equipment-card" markdown>

### **2x**{: .quantity-emphasis } QR-code camera

* Where: Amazon, AliExpress, your favorite shop ([example of a compatible camera](https://www.amazon.com.be/dp/B0DWLGCSJ6))
* Info: the game is very demanding about the USB camera required for the QR-code readers. It must be UVC, support a resolution of 640x480 at 30 fps in YUY2 format and offer a 50 degree field of view. An external light is also needed to illuminate the area.
(A suitable LED is listed under [Small supplies](#small-supplies))

</div>

## Small supplies

You will find these items in your favorite shop (Amazon, AliExpress, ...). These are small, cheap purchases you will need over the course of the various steps.

<div class="equipment-supplies" markdown>

### Cables

* **1x**{: .quantity-emphasis } **HDMI to DVI-D cable (3 m)**
    - Connection from the ALLS to the Player 1 screen.
* **1x**{: .quantity-emphasis } **DVI-D to DVI-D cable (2 m)**
    - Connection from the ALLS to the Player 2 screen. Your FiNALE may already have one natively.
* **1x**{: .quantity-emphasis } **DB-9 Female-Female cable**
    - As short as possible; the cable will be cut to make two connectors, for the Aime reader and the VFD.
* **4x**{: .quantity-emphasis } **DB-9 Male-Female cable (3 m)**
    - Used as an extension to connect the Aime reader to the ALLS.
    - Used as an extension to connect the VFD to the ALLS.
    - Used as an extension to connect the Player 1 touchscreen to the ALLS.
    - Used as an extension to connect the Player 2 touchscreen to the ALLS.
* **1x**{: .quantity-emphasis } **IEC C-13 cable (2 m)**
    - Plugged into the ALLS and cut off at the plug to be wired directly to the cabinet's power supply.
* **2x**{: .quantity-emphasis } charging **micro-USB cable**
    - To power the two LED controller proxies. The end opposite the Pico is cut off to wire the red lead to 5V and the black lead to the ground of the power supply installed in [step 1](step-1-alls-and-psu.md).

### Electronics

* **2x**{: .quantity-emphasis } **TTL to RS-232 converter with female DB-9** ([example](https://www.amazon.com.be/dp/B09L1BB6F8))
    - To bridge the Player 1 touchscreen I/O and the DB-9 connection on the ALLS.
    - To bridge the Player 2 touchscreen I/O and the DB-9 connection on the ALLS.
* **2x**{: .quantity-emphasis } **Raspberry Pi Pico** ([example](https://aliexpress.com/item/1005007393927221.html))
    - To build the LED controller proxies. Prefer a version with the pins pre-soldered onto the Pico if you want a solder-free installation. **Careful: the pins must be soldered facing down, not up.**
* **2x**{: .quantity-emphasis } **Pico-2CH-RS232** ([example](https://aliexpress.com/item/1005012732708840.html))
    - To build the LED controller proxies

### Hookup wire

* **Flexible hookup wire (AWG 22-24)**
    - There will be several cables to crimp throughout this guide; plan on having spares.

### Connectors

* **1x**{: .quantity-emphasis } **Molex Mini-Fit Jr. 2x7-pin female connector** ([example](https://www.amazon.com/dp/B078H8F2YQ))
    - To cleanly connect the power connector previously wired to the RingEdge 2.
* **30x**{: .quantity-emphasis } **Molex Mini-Fit Jr. female crimp pin**
    - To go with the previous connector.
* **1x**{: .quantity-emphasis } **JST-RA 2x10-pin female connector**
    - For the IO4's CN9.
* **30x**{: .quantity-emphasis } **JST-RA female crimp pin**
    - To populate CN9 and the cables to be added on the IO4's CN3.
* **2x**{: .quantity-emphasis } **JST-SM 8-pin female connector**
    - The ends of the billboard lighting harness, Player 1 side and Player 2 side, to connect to the original JST-SM connectors.
* **2x**{: .quantity-emphasis } **JST-SM 2-pin connector, male + female pair**
    - Ideal for making our own connectors to make life easier, but if you do not have any in stock, plain JST-XH will also do.

For the rest of the connectors, rather than buying each part number individually, get an assortment kit per connector type directly: they are easy to find on Amazon or AliExpress, bundling several housing sizes, both genders (male/female) and a batch of crimp pins. Here is what you will need in each:

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
    This list is incomplete; it will be expanded alongside the steps that follow.
    Still to be added, once the details are known:

    - **2x**{: .quantity-emphasis } Jack sockets for the headphones and the cables that go with them
    - **2x**{: .quantity-emphasis } Sound amplifiers for the headphones
    - **2x**{: .quantity-emphasis } White LEDs for the QR-code readers
    - **1x**{: .quantity-emphasis } Red LED to indicate that the camera is recording
    - **1x**{: .quantity-emphasis } Warm white LED to light the camera

---

!!! warning "Check your hardware before you start"
    Make sure you have received and tested all the hardware you ordered before diving into the conversion proper. It will save you a lot of headaches: if a problem comes up, you can immediately rule out faulty hardware.

---

!!! tip "Here is the simplified checklist"
    Want to tick off your purchases as you go rather than diving back into the detail? Here is the [purchase checklist](equipment-checklist.md).

---

Now that you have the hardware, let's start with [Step 1: Replacing the Central PC (ALLS)](step-1-alls-and-psu.md).

