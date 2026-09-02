---
title: "📷 7 - Cameras (optional)"
---

# 📷 Step 7: Cameras (Optional)

--8<-- "includes/wip-en.md"

If you want to finish your cabinet so it is perfect, you can add the cameras. However, the game is perfectly functional without them.

## 1. Player camera (in-game photos)

Take a very basic, cheap webcam. Print a 3D mount to fix it to the top of the cabinet, on the acrylic glass.

* **Connection:** on the *ALLS* computer lying flat, this webcam must be plugged into the USB port located **at the bottom right** *([manual](../resources/pdfs/maimai-dx-manual-full.pdf), page 128)*.
  Two dedicated LEDs also need to be wired to the IO4. On the CN9 connector, in position 7 "CAMERA LED WARM" and in position 8 "CAMERA LED RED". *(See [manual](../resources/pdfs/maimai-dx-manual-full.pdf), page 194)*.
* Most private networks do not handle the camera, so its use will boil down to the in-game display.

## 2. QR-code reader cameras

On *DX*, players can scan cards with QR codes.

* For this to work, you must use webcams capable of recording in **UVC 640x480 format**.
* **Lighting:** the game requires these cards to be lit with white LEDs (powered at 12V). These LEDs are controlled by the IO4, via pins 55 and 56. *(See [manual](../resources/pdfs/maimai-dx-manual-full.pdf), page 194)*.
* **Connection:** on a real *DX* cabinet, these cameras are connected to the same USB hub as the cabinet's lights. You can do the same using a simple USB hub plugged into the PC. On the *ALLS* computer lying flat, the hub must be plugged into the USB port located at the **top right** *([manual](../resources/pdfs/maimai-dx-manual-full.pdf), page 128)*.

!!! tip "Diffuse lighting"
    Do not point the LEDs directly at the camera lens. Instead, light the plastic wall so that the light bounces diffusely onto the card.

!!! question "Do you really need to install the QR-code cameras?"
    It is entirely optional. Unless you have access to another very specific cabinet (the *Sega CardMaker*) to print your cards, they will be of no use to you. On top of that, most private networks virtually grant a "DX Pass" to every player, unlocking the features without needing to scan cards.

    Note that when registering your cabinet on a private network, it is often possible to ask the administrator to completely disable the search for these cameras if you do not want to install them.

---

Have you finished all the steps? Head to the [conclusion](conclusion.md)!
