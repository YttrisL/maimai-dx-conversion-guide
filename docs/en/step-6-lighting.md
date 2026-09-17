---
title: "💡 6 - Lighting (optional)"
---

# 💡 Step 6: Lighting

The lighting is technically an *optional* step of the conversion, in the sense that it does not affect the playability of the cabinet. However, the operation is not that complex and the lighting adds a lot to the charm of maimai DX. It is therefore recommended not to skip this step.

## Technical explanation

??? note "Click here for the technical explanation"
    ### How the LEDs work on a maimai DX

    On a real *DX* cabinet, the lighting is driven by three different controllers:

    * The **IO4** manages the **billboard** lighting (labeled `BILLBOARD LED` / `ROOF LED` on the Sega diagrams). See [Step 3](step-3-io-board.md).
    * Two identical control boards (part no. `837-15070-04`):
        * P1 side: the eight buttons, the background lighting and the left-side lighting.
        * P2 side: the eight buttons, the background lighting and the right-side lighting.

    ![Lighting control chain: the P1 and P2 LED boards (part no. `837-15070-04`) join the RS-232 to USB adapter (part no. `837-15067-02`) over RS-232, itself plugged into the USB hub shared with the P1 and P2 QR-code cameras](../resources/images/step-6-lighting/led-controllers-chain-en.svg)

    The two control boards interface over RS-232 to a single RS-232 to USB adapter. That adapter is itself connected to the same USB hub as the QR-code readers (see [Step 7](step-7-cameras.md)).

    !!! info "Software configuration of the COM ports"
        The LED controllers are interfaced on the ALLS virtual COM ports as follows:

        * **COM21** for the P1 LEDs.
        * **COM23** for the P2 LEDs.

    ### How the LEDs work on a maimai FiNALE

    The way it works is a little simpler on FiNALE:

    * Unlike DX, no LED goes through FiNALE's IO3.
    * Two identical control boards manage the LEDs (part no. `837-15070-02-91`):
        * P1 side: the eight buttons, the background lighting, the woofer lighting and the billboard on the P1 side and in the center.
        * P2 side: the eight buttons, the background lighting, the woofer lighting and the billboard on the P2 side.

    ![Lighting control chain on FiNALE: the P1 and P2 LED boards (part no. `837-15070-02-91`) join the same RS-232 to USB adapter as on DX (part no. `837-15067-02`) over RS-232, plugged directly into a USB port of the RingEdge 2, with no USB hub](../resources/images/step-6-lighting/led-controllers-chain-finale-en.svg)

    As on DX, these two control boards interface over RS-232 to the same RS-232 to USB adapter. Luckily, **it is exactly the same one on FiNALE and on DX (part no. `837-15067-02`)**.

    On FiNALE, however, this adapter plugs directly into a USB port of the RingEdge 2, without going through a USB hub.

    ### What this implies for a conversion

    Three observations:

    * We will need a 4-port USB hub to reproduce the connection architecture on the ALLS. maimai DX is very demanding about which port the USB devices are connected to on the ALLS.
    * The billboard lighting is no longer connected to the LED controllers on DX, so they no longer receive the information to light it. This connector will have to be rewired to the IO4.
    * But above all, **the most important point**: the FiNALE and DX LED controllers **do not have the same part number**. If you try to plug a FiNALE LED controller into an ALLS running DX, **the game will throw a non-blocking error at startup** because the part number sent by the controller, `837-15070-02-91`, is not the one the game expects to receive, `837-15070-04`. Fun fact: in this state, the game will still send the information for the gameplay button lighting, but not for the background.

    Fortunately, there is a solution for these three problems.

## For the gameplay buttons and the background of both players

The problem is that for the LED controllers, **maimai DX expects to receive the identifier `837-15070-04`**, but the FiNALE ones will send it back `837-15070-02-91` and the game will error out. That is really the only problem: the FiNALE controller is otherwise 100% compatible with the instructions sent by DX.

We therefore need to find a way to modify the identifier sent by the two LED controllers so that they send back the value the game expects to receive. This is fairly simple to do in software, but we want perfect software fidelity. **We must therefore find a hardware solution.**

**The solution:** a simple Raspberry Pi Pico, programmed with a homemade firmware, that installs itself between the LED controller and its RS-232 to USB adapter to modify only the message where the controller sends its identifier. All other messages are passed through unchanged in both directions.

The software is already all set: it is [mailight_pico](https://gitea.farewell.dev/Yttris/mailight_pico), a port of *mailight_rs* by 4ndr3w on GitHub. All that is left is to build the proxy.

### Building a proxy

!!! info "Two of them"
    You will need two proxies, one for each LED controller. So do this operation twice.

Start by installing the mailight_pico firmware on the Raspberry Pi Pico. If you have never installed firmware on a Pico, it is extremely simple. [All the instructions are on the project page](https://gitea.farewell.dev/Yttris/mailight_pico#3-installing-the-firmware).

Next you need to assemble your Raspberry Pi Pico with the `Pico-2CH-RS232`. Watch the orientation; the markings on the underside of the `Pico-2CH-RS232` indicate the orientation the Pico's USB port is supposed to be in.

!!! lightbox
    ![The `Pico-2CH-RS232` module, image from the [official Waveshare wiki page](https://www.waveshare.com/wiki/Pico-2CH-RS232)](../resources/images/step-6-lighting/pico-2ch-rs232.png)

!!! warning "Watch the orientation"
    Make sure your assembly matches the image. If your Raspberry Pi Pico has, for example, its USB port between the two PCBs rather than on the outside as in the image, it means the pins of your Pico are soldered the wrong way round. **Do not try to power it on!** You would only manage to damage the `Pico-2CH-RS232`. You must either re-solder the pins the right way round yourself, or get a new, correctly assembled Pico.

Once your hardware is assembled, all that is left is to prepare the connectors so you can insert the Pico between the LED controller and its RS-232 to USB adapter. Depending on whether you are building a proxy for the P1 or P2 side LED controller, you will need a different connector:

* P1 side: JST-XH **7** pins - male **and** female
* P2 side: JST-XH **9** pins - male **and** female

!!! lightbox
    ![JST-XH connector, P1 side](../resources/images/step-6-lighting/led-driver-connector-p1.png)
    ![JST-XH connector, P2 side](../resources/images/step-6-lighting/led-driver-connector-p2.png)

For simplicity, be sure to use white and red wire and install them in the positions matching the cabinet installation. Crimp the white wire onto pin 4, the red wire onto pin 5.
Make your cable so that if you plug the male connector into the female connector, the wire colors are aligned. These images come from the wiring diagram, but as you will see, there is no `SHIELD` wire on the real connectors in the cabinet, which means we will have to connect our common ground somewhere else on the `Pico-2CH-RS232`.

!!! lightbox
    ![Top view of the `Pico-2CH-RS232` module](../resources/images/step-6-lighting/pico-2ch-rs232-photo.png)
    ![The cabinet's original LED controller connector plugged into the hand-made connector](../resources/images/step-6-lighting/led-controller-rs232-connector.jpg)

You must connect the cables with the **female JST-XH connector to the Channel0 screw terminal**, and the cables with the **male JST-XH connector to the Channel1 screw terminal**. That way, Channel0 should end up on the RS-232 to USB adapter side, and Channel1 on the LED controller side. Connect the wires as follows:

* Channel0 side
    * TX0: Red
    * RX0: White
    * GND: connect a black wire to this terminal and attach its stripped end to the GND terminal of the power supply installed in [step 1](step-1-alls-and-psu.md).
* Channel1 side
    * TX1: White
    * RX1: Red

Your proxy is now finished. To power it, the simplest way is to connect a micro-USB cable to the Pico's port, and cut off its other end so you can wire its red lead directly to the 5V terminal and its black lead to the GND terminal of the power supply installed in [step 1](step-1-alls-and-psu.md).

!!! lightbox
    ![The finished proxy: the Raspberry Pi Pico assembled onto the `Pico-2CH-RS232`, with the female JST-XH connector (Channel0, RS-232 to USB adapter side) and the male JST-XH connector (Channel1, LED controller side) wired in red and white, plus the micro-USB power cable](../resources/images/step-6-lighting/pico-2ch-rs232-proxy-wired.jpg)


### Installing the proxy

Now that you have your two proxies, all that is left is to install them. You can unplug the LED controller's connector and connect it to the male connector of your proxy; the female connector of the proxy then takes its place on the RS-232 to USB adapter.

Once the proxy is installed for both LED controllers, all that is left is to connect the RS-232 to USB adapter to the ALLS via the USB hub, and you are done. The game should recognize the LED controllers natively, with no software modification.

!!! warning "Plug the adapter in correctly"
    As mentioned in [step 1](step-1-alls-and-psu.md), the USB hub must absolutely be plugged into the USB port numbered 2, and the `RS-232 to USB adapter` that the LED controllers are connected to must be plugged into the USB hub. As said before, maimai DX is very demanding about which USB port devices are connected to; if plugged in wrong, the LEDs will not light up.

    Even if you do not plan to use the QR-code cameras, the USB hub is still mandatory.

## For the billboard and the woofers

??? note "Click here for the technical explanation"
    On a maimai FiNALE, the woofers and the billboard are on the same lighting circuit. The two elements are not electrically separated, one always necessarily lights the other. So although the woofers are no longer lit on maimai DX, this will not be a problem since the billboard still is. However, as explained earlier, on DX it is no longer the LED controller that manages the light for this section of the cabinet.

    Since the DX LED controller no longer manages the billboard lighting, the game simply does not send it that information. On DX, **it is the IO4 that handles these LEDs**. The reason for this change remains a mystery, but it means having to rewire part of the LED controllers' connections.

    Luckily, Sega's engineers did things well, and the FiNALE wiring diagram references a very handy connector that will let us broadcast our signal to the Player 1 and Player 2 sides without having to rewire the whole cabinet:

    !!! lightbox
        ![FiNALE wiring diagram, connector AB on the P1 side: the MAI-60109 harness powers the CENTER LED, ROOF LED (L), ROOF LED (R) and WOOFER LED boards](../resources/images/step-6-lighting/lighting-topper-p1-side.png)
        ![FiNALE wiring diagram, connector BB on the P2 side: the MAI-60109 harness powers the WOOFER LED, ROOF LED (L) and ROOF LED (R) boards, with the SM5P connector unused](../resources/images/step-6-lighting/lighting-topper-p2-side.png)
        ![8-pin JST-SM connector that connects the woofers and the billboard lighting (in black)](../resources/images/step-6-lighting/led-controller-rs232-disconnect.jpg)

    On the P1 diagram, there is a `CENTER LED` element that does not appear on the P2 one. It is the lighting for the center of the billboard. On DX, this distinction does not exist, and although the signals are separate, the billboard is always lit the same color on both sides. The simplest solution is therefore to connect pins `A2`, `A5` and `A8` of the P1 connector to pins `C3`, `C5` and `C8` so that the center is lit the same color as the Player 1 side.

There are two ways to go about this: we can either create our own wiring harness compatible with the IO4's structure and then connect the LEDs to the IO4 through it, or, if you chose the [conversion PCB]({{IO4_CONVERSION_PCB}}) in [step 3](step-3-io-board.md), simply connect the various LEDs to the right ports on the PCB.

??? example "The easy method - The conversion PCB"
    This is the simplest method: if you already installed it in [step 3](step-3-io-board.md), all you need to do is connect the connector coming out of the LED controller to the conversion PCB. Don't forget to connect the 12V - **watch the polarity** - and you're done.

    !!! tip "Use the LED power supply"
        The cabinet natively uses a dedicated 12V power supply for the LEDs; you can reuse it to power the board. **Do not use the 12V you use for the IO4.** Conversely, do not use the LED power supply to power the IO4 - these two circuits must share a common ground but stay separate.

    You will need an extension to connect the existing cable: 1 meter for the Player 2 side, and 2 meters for the Player 1 side. You can easily crimp this cable yourself; you need a `JST-XH 8-position female` pin on one end, and a `JST-SM 8-position female` one on the other.

    !!! lightbox
        ![Conversion PCB [maiConvert-IO4]({{IO4_CONVERSION_PCB}}): location of connector J22 (`12V input`, watch the polarity) and connectors J23/J24 (`BILLBOARD LED L`/`R`) where the billboard LED harness connects](../resources/images/step-6-lighting/led-inputs-and-12-on-convertion-pcb.jpg)
        ![Male 8-position JST-SM wiring harnesses that handle the billboard and woofer LEDs, unplugged from the connector wired to the LED controller on a FiNALE cabinet](../resources/images/step-6-lighting/led-controller-rs232-disconnect.jpg)

    Note that if you plan to install the cameras in the next step, the conversion PCB will also make life easier for their LEDs, since it already has a ready-made connector for installing them.

??? example "Hand-making a wiring harness"
    We are going to create our own wiring harness that integrates with the IO4 via a 20-pin JST-RA connector for CN9, and ends in two 8-pin JST-SM connectors for the left and right sides. If you followed the rewiring suggestions in [step 3](step-3-io-board.md), you should already have a 2-pin JST-SM connector wired to the IO4's CN3 connector for the `BILLBOARD LED L RED` and `BILLBOARD LED R RED` signals.

    !!! lightbox
        ![Visual identification of the LED pins on the IO4: the CN9 connector (20-pin JST-RA) carries BILLBOARD LED L/R GREEN, CAMERA LED WARM/RED and BILLBOARD LED L/R BLUE, while BILLBOARD LED L/R RED is on the CN3 connector](../resources/images/step-6-lighting/io4-visual-reprensation-of-led-pins.png)
        ![Official IO4 wiring diagram centered on the LED pins: CN9 connector (RA20P) for BILLBOARD LED L/R GREEN, CAMERA LED WARM/RED and BILLBOARD LED L/R BLUE, and CN3 connector (RA60P) pins 51-52 for BILLBOARD LED L/R RED](../resources/images/step-6-lighting/io4-wiring-schema-focused-on-leds.png)

    So let's make our own wiring harness based on the following diagram. Ideally, it should be long enough to be installed cleanly in the cabinet: 2 meters for the Player 1 side, 1 meter for the Player 2 side. For the 12V, do not use the 12V pin of CN9; instead, wire directly to the cabinet's internal 12V power supply. That way you avoid loading the I/O board unnecessarily.

    ![Wiring harness for the billboard lighting: from the IO4 (CN9 pins 5, 6, 9 and 10, and CN3 pins 51-52 already wired in step 3) and the internal 12V power supply, making two 8-pin JST-SM connectors - P1 side (2 meters, with a bridge from pins 1-4 to 5-8 to also power CENTER LED) and P2 side (1 meter, pins 5-8 unused) - which then plug into the original AB and BB connectors](../resources/images/step-6-lighting/led-topper-harness-en.svg)

    Once the harness is made, all that is left is to plug it into the IO4, wire the 12V to the internal power supply, and connect the two original 8-pin JST-SM connectors to your new cable. Make sure to test continuity on all your cables before installation to rule out any badly crimped pin.

    !!! lightbox
        ![Male 8-position JST-SM wiring harnesses that handle the billboard and woofer LEDs, unplugged from the connector wired to the LED controller on a FiNALE cabinet](../resources/images/step-6-lighting/led-controller-rs232-disconnect.jpg)

    !!! tip "The camera LEDs"
        If you want to connect the optional cameras on your cabinet, crimp a few extra connectors right now:

        - A 2-pin JST-SM connector onto pins 7 and 8 of CN9, for easy access to the CAMERA LED WARM and CAMERA LED RED signals respectively.
        - A 2-pin JST-SM connector onto pins 55 and 56 of CN3, for the 1P CODE READER LED and 2P CODE READER LED signals in that order.

## In summary
!!! tldr "The gist"
    For the button LEDs and the cabinet background:

    * Build two proxies, each from a Raspberry Pi Pico and a `Pico-2CH-RS232`.
    * Install the proxy between the LED controller and the RS-232 to USB adapter.
    * Plug the adapter into the USB hub on the appropriate port, and connect the hub to the dedicated port on the ALLS.

    For the billboard and the woofers:

    * Either: connect the cabinet's existing connectors to the [conversion PCB]({{IO4_CONVERSION_PCB}}).
    * Or: make and install a new wiring harness running from the IO4 and connecting to the cabinet's existing connectors.

---

Final step (optional): the [Cameras](step-7-cameras.md).
