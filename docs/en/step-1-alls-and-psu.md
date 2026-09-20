---
title: "🛠️ 1 - Central PC (ALLS)"
---

# 🛠️ Step 1: Replacing the Central PC (ALLS)

--8<-- "includes/wip-en.md"

The old *RingEdge 2* PC is not powerful enough to run *DX*. You need an **ALLS HX2** PC.
Alternatively, it is often easier (and cheaper) to find **ALLS MX2** PCs, and those can be modified (downgraded) to match the exact specifications of an HX2.

* **Storage:** the HX2 comes by default with a 128 GB SSD and a 512 GB hard drive. For a private-server install, these drives are enough.

Here is the plate from the official *SEGA* manual detailing the full set of connectors on the back of an ALLS HX2, handy for identifying each plug before redoing the *RingEdge 2*'s original wiring:

[![Rear view of an ALLS HX2 and detail of its connectors: 4 D-SUB9P/stereo mini-jack connectors [SIDE] at the top, 2 HDMI/DVI connectors, 3 stereo mini-jack connectors [C/W] [FRONT] [REAR], 5 LAN/USB connectors [IO]/[USB HUB]/[P CAMERA]/[INSTALL], 1 D-SUB9P connector [COM1], and the power cord connector at the bottom](../resources/images/step-1-alls-and-psu/alls-hx2-rear-connectors-en.jpg)](../resources/images/step-1-alls-and-psu/alls-hx2-rear-connectors-en.jpg)
_(Plate extracted from the [official maimai DX manual](../resources/pdfs/maimai-dx-instruction-manual-full.pdf), page 128.)_

!!! warning "Power supply"
    The internal power supply of the *RingEdge 2* directly provided the voltages needed by various components of the *FiNALE* cabinet. The Molex connector on the front of the *RingEdge 2* supplies 12V, 5V and 3.3V to the rest of the cabinet. The new *ALLS* PC does not have similar power connectors. **The ideal solution** is to add a small secondary power supply (arcade PSU), separate from the *ALLS* PC's own, to power the PCBs and the lights. A 12V/5V supply will be enough; no component of the *FiNALE* cabinet uses 3.3V.

---

Let's move on to [Step 2: HDX Display and Touchscreens](step-2-touchscreen-display.md).
