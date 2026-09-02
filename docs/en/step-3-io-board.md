---
title: "🔌 3 - I/O board & buttons"
---

# 🔌 Step 3: The I/O Board and the Buttons

--8<-- "includes/wip-en.md"

To run *DX*, you need to replace the old I/O board with the new **IO4** model. Fortunately, the wiring stays broadly the same, with a few exceptions.

*(Note: the full wiring detail for the IO4 board is on page 194 of the [manual](../resources/pdfs/maimai-dx-manual-full.pdf), bottom right)*

## 1. The Coin Locker

The pin corresponding to the coin blocker was moved in the transition to the IO4. On a *FiNALE* cabinet, it was wired to pin 51.

1. On the large wiring harness formerly connected to the IO3, locate pin **51**.
2. Move that wire to pin **53**.

## 2. Adding the "Select" buttons

On *DX*, new physical buttons appeared to let players sort songs. You have to wire them manually:

1. You need to install your buttons on the central panel of your cabinet, ideally by making a custom enclosure to avoid a destructive modification of the shell.
2. Connect one pin of each button to the neutral of the wiring harness (pins 9 to 16).
3. Connect the other pin of the button to the corresponding pin of the ribbon:
   * "1P SELECT BUTTON": pin **27**
   * "2P SELECT BUTTON": pin **26**

## 3. Controlling the billboard LEDs

On *DX*, the IO4 is responsible for managing the billboard lighting (labeled `BILLBOARD LED` / `ROOF LED` on the Sega diagrams). This point is also covered in [Step 6](step-6-lighting.md), but here is the pinout of the LEDs to connect already:

* "BILLBOARD LED L RED": connector **CN3** - pin **51** (the large wiring harness)
* "BILLBOARD LED R RED": connector **CN3** - pin **52** (the large wiring harness)
* "BILLBOARD LED L GREEN": connector **CN9** - pin **5**
* "BILLBOARD LED R GREEN": connector **CN9** - pin **6**
* "BILLBOARD LED L BLUE": connector **CN9** - pin **9**
* "BILLBOARD LED R BLUE": connector **CN9** - pin **10**

If you do not want to install the billboard LEDs, you can skip this step.

## 4. USB connection of the IO4 board

The new IO4 board communicates with the *ALLS* PC over a simple USB cable. However, **the choice of USB port on the computer is defined in the [manual](../resources/pdfs/maimai-dx-manual-full.pdf)** *(see page 128 of the manual)*. If you look at the *ALLS* PC lying flat (horizontal), you must plug the IO4 cable into the USB port located **at the bottom left**.

---

Let's move on to [Step 4: The Aime Card Reader](step-4-aime-reader.md).
