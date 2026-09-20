---
title: "📺 2 - Screens & touchscreens"
---

# 📺 Step 2: The Display and the HDX Touchscreens

--8<-- "includes/wip-en.md"

Let's start by installing the display and the touchscreens.

## The video connections

The game is programmed to send video to the two screens in a very specific way. The order must be respected. *(Reference: official [manual](../resources/pdfs/maimai-dx-instruction-manual-full.pdf) for the DX cabinet, page 128)*

* **Player 1 (P1):** can be connected to the **HDMI** or **DisplayPort** port (the [official manual](../resources/pdfs/maimai-dx-instruction-manual-full.pdf) recommends HDMI).
* **Player 2 (P2):** must be connected to the **DVI** port.

There is, however, a slight native difference between the screens of a *FiNALE* and a *DX*. In both cases they are 1920x1080 screens running at 60 Hz, but the *FiNALE* screens measure 42" diagonally, while the *DX* screens measure 43". The difference is practically imperceptible in-game.

## The HDX touchscreens

Remove the old touchscreens from the *FiNALE* cabinet (held by 8 screws) and install the new HDX touchscreens.
You then have to connect the touchscreens to the right "addresses" (COM ports) on the ALLS, otherwise the game will mix up the two players: *([manual](../resources/pdfs/maimai-dx-instruction-manual-full.pdf), page 128)*

* **Player 1:** must be connected to port **COM3**.
* **Player 2:** must be connected to port **COM4**.

Unlike other conversion kits, the HanDevice I/O board supplied with the HDX touchscreens exposes a UART serial port directly. You can therefore connect it straight to the ALLS, with no signal conversion or intermediate Raspberry Pi - see the [Shopping list](equipment.md) for the details of this I/O board.

---

Let's move on to [Step 3: The I/O Board and the Buttons](step-3-io-board.md).
