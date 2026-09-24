---
title: "📷 7 - Cameras (optional)"
---

# 📷 Step 7: Cameras (Optional)

At this point, only one feature still separates your conversion from a real *DX*: **the cameras**. The game uses them very little, and they are widely considered optional. But if you want to get as close as possible to a real *DX*, they are fortunately quite simple to install.

## Technical explanation

??? note "Click here for the technical explanation"
    A real *DX* has **three cameras**: one pointed at the players, and two that serve as QR-code readers for the *DX Pass*.

    - **The player camera**: a simple USB UVC camera, at 1280x960 with a 95° HFOV. [[reference]]({{SHIKINO_PLAYER_CAMERA_REFERENCE}})
    - **The QR-code reader cameras**: two USB UVC cameras, at 640x480 with a 50° FOV.

    !!! info "DX Pass"
        DX Passes are physical cards that players get printed on the "Sega CardMaker" cabinet. That cabinet is rare outside Japan, and even rarer in working printing order. Moreover, DX Passes are nowadays automatically linked to the player's account: the physical card is no longer needed. **The QR-code readers are therefore largely optional**, even useless.

        Some in-game events only trigger by scanning specific cards, but most private servers unlock them by default.

    **For the player camera, any USB UVC camera will do**, even a cheap webcam. The game only uses it to show a photo of the players at the end of each song, an option most players turn off to save time.

    **For the QR-code readers, the game is much stricter**: you absolutely need USB UVC cameras able to film at 640x480, with a precise FOV, otherwise the QR-codes are not recognized.

    In both cases, the game provides **dedicated lighting for each camera**, driven by the IO4. Connecting it is not essential, but without proper lighting, the QR-code readers are likely to work very poorly. For the player camera, lighting becomes necessary if your cabinet is in a dark room. The game also drives a red LED, which warns players that the camera is filming.

    The cameras connect to the ALLS over USB: the player camera directly to the motherboard, the two QR-code reader cameras to the USB hub that already hosts the LED controllers' RS-232 to USB adapter (see [step 6](step-6-lighting.md)).

## Player camera (in-game photos)

Every camera model is different, so a universal mount is hard to offer. The best option is to **design a 3D-printable mount** to install at the top of the cabinet, using the existing screws of the acrylic panel.

* **Installation on the cabinet:** 3D printing.
* **Connection to the ALLS:** USB, on port **#3**.
* **Connection to the IO4:**
    - **CAMERA LED WARM: CN9 - Pin 7**: cathode of the white LED ring that lights the filmed area.
    - **CAMERA LED RED: CN9 - Pin 8**: cathode of the red LED that tells players the camera is filming.

If you made your own wiring harness and followed the suggestion in [step 6](step-6-lighting.md), you already have a connector ready for the IO4. With the conversion PCB, two dedicated connectors are available for these LEDs.

!!! lightbox
    ![ALLS diagram: USB port #3 used for the player camera, highlighted by the red arrow](../resources/images/step-7-cameras/alls-hx2-rear-connectors-emphasis-on-usb-no3.jpg)
    ![Conversion PCB [maiConvert-IO4]({{IO4_CONVERSION_PCB}}): location of connectors J29 (`CAMERA LED RED`) and J30 (`CAMERA LED WARM`)](../resources/images/step-7-cameras/camera-led-on-convertion-pcb.jpg)

## QR-code reader cameras

Ideally, get **two small 30mm x 25mm modules**: they fit [the 3D model designed by SpiralGlide](spiralglide-resources.md#qr-code-reader-mount-dx-pass-reader), which attaches using the existing screws of the acrylic panel.

* **Installation on the cabinet:** [3D printing](spiralglide-resources.md#qr-code-reader-mount-dx-pass-reader).
* **Connection to the ALLS:** USB, through the USB hub plugged into port **#2**. Any port on the hub will do.
* **Connection to the IO4:**
    - **1P CODE READER LED: CN3 - Pin 55**: common cathode (R, G and B) of the LED strip lighting the player 1 reader.
    - **2P CODE READER LED: CN3 - Pin 56**: common cathode (R, G and B) of the LED strip lighting the player 2 reader.

If you followed the suggestion in [step 6](step-6-lighting.md), you already have a connector ready for these two signals. They are also available on the conversion PCB.

**For the game to identify the cameras, each one must film a specific QR-code**: *SDEZ01* on the player 1 side, *SDEZ02* on the player 2 side. SpiralGlide's 3D model has a slot of the right size for these codes. Print [this PDF](../resources/images/step-7-cameras/codes-for-qr-code-readers.pdf) on A4, with a properly calibrated printer, to get QR-codes of the right size, then stick them in place.

If you chose the cameras from the [shopping list](equipment.md), their lens is adjustable: you can tweak the focus.

!!! tip "The QR-code reader LEDs"
    *DX* originally uses an RGB LED strip, but its three colors share a single cathode driven by the IO4: they always light up together, at (almost) the same intensity. **A warm white LED strip will give the same result.**

    **Do not point the LEDs directly at the camera lens.** Light the plastic wall instead, so the light diffuses onto the card. Front lighting creates a glare that blinds the camera and prevents the QR-code from being read.

!!! tip "Installing the camera modules"
    **The game is very strict about the cameras' orientation**: if the angle is off, it will not read the cards' QR-codes. Also beware: a default QR-code that reads fine does not guarantee the cards will, so run some tests. To adjust a module's height and tilt, you can for example add nuts on its screws. It is not ideal, but it works.

    Test the detection in the game's Test menu. Unfortunately, nothing beats trial and error for this step.

!!! lightbox
    ![ALLS diagram: USB port #2 used for the QR-code reader cameras' hub, highlighted by the red arrow](../resources/images/step-7-cameras/alls-hx2-rear-connectors-emphasis-on-usb-no2.jpg)
    ![Conversion PCB [maiConvert-IO4]({{IO4_CONVERSION_PCB}}): location of connectors J25 (`1P CODE READER LED`) and J26 (`2P CODE READER LED`)](../resources/images/step-7-cameras/code-reader-led-on-convertion-pcb.jpg)
    ![Nuts used as spacers on the screws of the 3D-printed model, to adjust the height and angle of the camera modules above the QR-codes](../resources/images/step-7-cameras/screw-nuts-used-as-spacers-to-orient-cameras.jpg)

## Validating the installation

The game's Test menu has a page dedicated to the cameras. The game looks for **three video streams** there, two of which must film the default QR-codes [SDEZ01](../resources/images/step-7-cameras/SDEZ01.svg) and [SDEZ02](../resources/images/step-7-cameras/SDEZ02.svg). Those two cameras are recognized automatically thanks to their QR-code, and the remaining camera is assigned to the players.

**If all three cameras are recognized in the right order, congratulations, the installation is complete!**

---

Have you finished all the steps? Head to the [conclusion](conclusion.md)!
