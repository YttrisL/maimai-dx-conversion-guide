---
title: "📷 7 - Cameras (optional)"
---

# 📷 Step 7: Cameras (Optional)

At this point, only one feature still sets our conversion apart from a real *DX*: the cameras. The game makes very light use of them, and they are widely considered optional. If you want to get as close as possible to how a real *DX* works, they are thankfully fairly simple to install.

## Technical explanation

??? note "Click here for the technical explanation"
    There are a total of 3 cameras in a real *DX*: one points at the players, and two act as QR-code readers for the *DX Pass*.

    - The player camera: a simple USB UVC camera with a resolution of 1280x960 and a 95° HFOV. [[reference]]({{SHIKINO_PLAYER_CAMERA_REFERENCE}})
    - The QR-code reader cameras: two USB UVC cameras, recording at 640x480 with a 50° FOV.

    !!! info "The DX Pass"
        DX Passes are physical cards that players can have printed via the "Sega CardMaker" machine. This machine is quite rare to find outside Japan, and even rarer to find in working order (meaning able to print). What's more, DX Passes are now automatically linked digitally to the user's account, so the physical card is no longer needed at the cabinet. As a result, having these QR-code reader cameras is largely optional, or even pointless.

        Some in-game events only trigger by scanning specific cards via the QR-code readers, but most private servers unlock these events by default.

    For the player camera, any USB UVC camera will do. The game only uses it to display a photo of the players at the end of each song. Most players disable this option to save time. A cheap webcam is enough.

    For the QR-code reader cameras, the game is much more demanding. They absolutely must be USB UVC cameras capable of recording at 640x480. The FOV matters too, otherwise the QR-codes won't be recognized by the game.

    In both cases the game expects dedicated lighting for each camera; these LEDs are controlled by the IO4. While it isn't essential to wire them up, the QR-code readers in particular are likely to work very poorly if they aren't lit appropriately. As for the player camera, if your cabinet sits in a dark arcade room, lighting will be necessary. The game also sends a signal for a single red LED, meant to warn users that the player camera is recording.

    The cameras connect to the ALLS over USB. The player camera plugs directly into the motherboard, while the two QR-code reader cameras plug into the same USB hub that hosts the RS-232 to USB adapter for the LED controllers from [step 6](step-6-lighting.md).

## Player camera (in-game photos)

Depending on which camera model you choose, it's hard to design a universal mount. Your best option is to design a 3D-printable mount that you can install on top of the cabinet, using the existing screws for the acrylic glass.

* **Installation on the cabinet:** 3D printing.
* **Connection to the ALLS:** over USB, on port **#3**. (See [step 1](step-1-alls-and-psu.md))
* **Connection to the IO4:**
    - **CAMERA LED WARM: CN9 - Pin 7** Cathode of the ring of white LEDs that lights the area filmed by the camera.
    - **CAMERA LED RED: CN9 - Pin 8** Cathode of the single red LED that indicates to players that the camera is recording.

If you made your own wiring harness and followed the suggestion in [step 6](step-6-lighting.md), you should already have a connector ready for the IO4 connection. Alternatively, if you went with the conversion PCB, two dedicated connectors are available for these LEDs.

!!! lightbox
    ![ALLS diagram: USB port #3 used for the player camera, highlighted by the red arrow](../resources/images/step-7-cameras/alls-hx2-rear-connectors-emphasis-on-usb-no3.jpg)
    ![Conversion PCB [maiConvert-IO4]({{IO4_CONVERSION_PCB}}): location of connectors J29 (`CAMERA LED RED`) and J30 (`CAMERA LED WARM`)](../resources/images/step-7-cameras/camera-led-on-convertion-pcb.jpg)

## QR-code reader cameras

For the QR-code readers, it's best to get two small modules around 30mm by 25mm; this will let you use [the 3D model designed by SpiralGlide](spiralglide-resources.md#qr-code-reader-mount-dx-pass-reader), which mounts on the cabinet using the existing screws for the acrylic glass.

* **Installation on the cabinet:** [3D printing](spiralglide-resources.md#qr-code-reader-mount-dx-pass-reader).
* **Connection to the ALLS:** over USB, via a USB hub plugged into port **#2**. Any USB port on the hub works. (See [step 1](step-1-alls-and-psu.md))
* **Connection to the IO4:**
    - **1P CODE READER LED: CN3 - Pin 55** Common cathode for the R, G, and B signals of the LED strip lighting player 1's reader camera.
    - **2P CODE READER LED: CN3 - Pin 56** Common cathode for the R, G, and B signals of the LED strip lighting player 2's reader camera.

If you followed the suggestion in [step 3](step-3-io-board.md), you already have a connector available for these two signals. As with the previous point, these signals are also available on the conversion PCB.

For the game to identify the QR-code cameras, they must point at a QR-code reading *SDEZ01* on the player 1 side, and *SDEZ02* on the player 2 side. SpiralGlide's 3D model has a cutout sized just right for these two codes. You can print [this PDF](../resources/images/step-7-cameras/codes-for-qr-code-readers.pdf) on A4 paper with a properly calibrated printer to get the QR-codes at the right size to stick in the correct spot.

If you chose the cameras suggested in the shopping list, note that it's possible to adjust their lens to set the focus.

!!! tip "The QR-code reader LEDs"
    By default, *DX* uses a strip of RGB LEDs to light the area, but the three R, G, and B signals share a single common cathode, driven by the IO4. In practice, this means all three colors turn on at the same time at (almost) the same intensity. Functionally, you can substitute a warm-white LED strip instead, the result will be the same.

    When installing the LED strip, don't aim the LEDs directly at the camera lens. Instead, light the plastic wall so the light bounces diffusely onto the card. Otherwise, front lighting will cause a glare that blinds the camera and prevents the game from reading the QR-code.

!!! tip "Installing the camera modules"
    The game is quite demanding about the orientation of the camera module; if the angle isn't a near-perfect match for what it expects, it won't be able to read the card's QR-code. Also be careful: just because the default QR-code is easily readable doesn't mean the cards will be too, so test it. While not ideal, you can, for example, adjust the module's height and angle by adding nuts onto the screw to change its tilt.

    You can test camera detection in the game's Test menu. Unfortunately there's no better method than trial and error for this step.

!!! lightbox
    ![ALLS diagram: USB port #2 used for the QR-code reader cameras' hub, highlighted by the red arrow](../resources/images/step-7-cameras/alls-hx2-rear-connectors-emphasis-on-usb-no2.jpg)
    ![Conversion PCB [maiConvert-IO4]({{IO4_CONVERSION_PCB}}): location of connectors J25 (`1P CODE READER LED`) and J26 (`2P CODE READER LED`)](../resources/images/step-7-cameras/code-reader-led-on-convertion-pcb.jpg)
    ![Nuts used as spacers on the screws of the 3D-printed model, to adjust the height and angle of the camera modules above the QR-codes](../resources/images/step-7-cameras/screw-nuts-used-as-spacers-to-orient-cameras.jpg)

## Validating the installation

In the game's Test menu, you have access to a page dedicated to checking the cameras. The game expects to find a total of three video feeds from the cameras you just installed, and among these three feeds it looks for two that point at the default QR-codes [SDEZ01](../resources/images/step-7-cameras/SDEZ01.svg) and [SDEZ02](../resources/images/step-7-cameras/SDEZ02.svg). The QR-code cameras will be automatically recognized thanks to these, and the game assigns the remaining camera to the player camera.

If all three cameras are correctly recognized in the right order in the menu, congratulations, the installation is complete.

---

Have you finished all the steps? Head to the [conclusion](conclusion.md)!
