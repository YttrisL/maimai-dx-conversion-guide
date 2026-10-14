---
title: "Error codes"
---

# 🚨 Error codes

This page gathers the error codes documented in the [official manuals](official-manuals.md), with their cause and the remedy recommended by the manufacturer.

Sources used:

* [Service Manual *ALLS HX2*](../resources/pdfs/alls-hx2-service-manual-full.pdf), chapter 4 (English): the **system errors**, common to every game running on an *ALLS HX2*. This is the main source.
* [Service Manual *maimai DX*](../resources/pdfs/maimai-dx-service-manual-full.pdf), chapter 5 (Japanese): the ***maimai DX* specific errors**.
* [Instruction Manual *maimai DX*](../resources/pdfs/maimai-dx-instruction-manual-full.pdf): no code table, only a few isolated mentions (see the last section).

!!! info "Before reading the tables"
    * The Japanese texts are translated here. The **original English titles** are kept in the *ALLS HX2* tables so you can look a code up in the manual.
    * To restart after an error, the *DX* manual asks you to switch off the cabinet's **sub power switch**, wait a moment, then switch it back on. Do not repeatedly toggle the power in quick succession.

## 1. *ALLS HX2* system errors

### Keychip (license key)

| Code | Title | Cause | Remedy given |
|---|---|---|---|
| 0001 | Keychip Not Found | There is no keychip, or the keychip is not connected correctly. | Check that the keychip is connected correctly. |
| 0002 | Keychip Not Available | The keychip is not supported. | Check the keychip and installation media (such as the DVD) combination. |
| 0004 | Game Program Not Acceptable | The keychip is not supported. | Check that a keychip from a different system is not inserted. |
| 0008 | Keychip Access Failed | The keychip could not be accessed. | Turn the power off, reinsert the keychip, then restart the *ALLS HX2*. |
| 0949 | Keychip Not Found | There is no keychip or there is a defect with its connection. | Check that the keychip is connected correctly. |

### Main board and game crash

| Code | Title | Cause | Remedy given |
|---|---|---|---|
| 0010 | Unexpected Game Program Failure | The game program crashed due to an unexpected error. | Turn the power off and restart the *ALLS HX2*. |
| 0021 | Main board Malfunctioning | The main board does not recognize itself. | Turn the power off and restart. |
| 0028 / 0029 / 0032 | Main board Malfunctioning | Failed to access the main board. | Turn the power off and restart. |
| 0912 | Unexpected Game Program Failure | The graphics board was unable to continue rendering. | Turn the power off and restart. |

### Game installation (DVD, USB, LAN server)

| Code | Title | Cause | Remedy given |
|---|---|---|---|
| 0022 | Game Program Not Found on Storage Device | There is no game program on the storage device. | Reinstall the game from the installation media. |
| 0041 | Game Program Not Found on Install Media | There is no game program on the installation media. | Check that the game on the media and the keychip correspond to each other. |
| 0042 | Game Program Not Found on Install Media | Some part of the game program is missing. | Check how the game was installed. |
| 0049 / 0052 | Install Media Access Failed | Failed to access the installation media. | Check that the DVD is not scratched, damaged or dirty, and that the DVD drive is connected correctly. |
| 0055 | Game Program Verify Error | The installed game program is not working correctly. | Reinstall the game from the installation media. |
| 0064 | Game Program Not Found on Server | No game program on the LAN install server. | Check that the game on the LAN install server and the keychip correspond to each other. |
| 0066 | Game Program Verify Error | The installed game program is not working correctly. | Reinstall the game from the installation media. |
| 0088 | System Program Verify Error | The installed system program is not working correctly. | Reinstall from the installation media. |
| 0917 | USB Flash Drive Remain Error | The installation USB flash drive was left connected. | Remove the USB flash drive. |
| 0919 | DVD Drive Remain Error | The installation DVD drive was left connected. | Remove the DVD drive. |

### Storage (main SSD and sub storage)

| Code | Title | Cause | Remedy given |
|---|---|---|---|
| 0081 | Invalid Storage Format | The main storage (SSD) format is wrong. | Contact support. |
| 0082 | Game Program Access Failed | The main storage (SSD) cannot be recognized. | Reinstall the game from the installation media. |
| 0083 | Storage Device Not Acceptable | The main storage (SSD) does not have enough space. | Run "UNINSTALL" via "STORAGE INFORMATION" in system test mode, then reinstall (manual 3-2, p. 8). |
| 0084 | Storage Device Malfunctioning | The main storage (SSD) may be broken. | Turn the power off and restart. |
| 0085 | Invalid Storage Format | The main storage (SSD) format is wrong. | Contact support. |
| 0086 | Invalid Storage Format | The sub storage format is wrong. | Format it from "Storage information" in system test mode. |
| 0087 | Storage Device Malfunctioning | The sub storage may be malfunctioning. | Turn the power off and restart the cabinet. |
| 0909 | Not Enough Storage Device | The game program does not have enough storage. | Contact support. |
| 0915 | Wrong Storage Device | Sub storage is not connected. | Contact support. |
| 0916 | Wrong Storage Device | Unnecessary sub storage (HDD) is connected. | Contact support. |

### Compatibility, memory and hardware

!!! tip "Tip"
    For these hardware errors, **very often** it is enough to remove the component concerned (board, memory module, cable...) and then **reinstall it in its socket**. For example, removing the graphics card and putting it back in its slot can fix code 0905.

| Code | Title | Cause | Remedy given |
|---|---|---|---|
| 0091 | Too High CPU Temperature | The CPU temperature is high. | Clean the *ALLS HX2* and its installation area, and check that the airflow outlets are not blocked (chapter 5 of the manual). The manual also recommends cleaning once a year. |
| 0901 | Wrong Platform | The game program is not supported by the *ALLS HX2*. | Check the game manual and the game / *ALLS HX2* combination. |
| 0902 | Wrong System Program | Started up with an unsupported system program; the *ALLS HX2* system program must be updated. | Check how the game was installed. |
| 0904 | Wrong Platform | The installed system program is not working correctly (text as printed, it does not match the title). | Reinstall from the installation media. |
| 0905 | Graphic Function Not Found | The game program does not support the graphics function. | Contact support. |
| 0906 | Sound Function Not found | The *ALLS HX2* sound function cannot be recognized. | Contact support. |
| 0907 | Not Enough System Memory | The game program does not have enough memory. | Contact support. |
| 0918 | Not Enough System Memory Module | The number of memory modules required for the game program is insufficient. | Contact support. |
| 0920 | Wrong Coin Assignments | The game program does not support the current coin assignments. | Check "COIN ASSIGNMENTS" in system test mode (3-6, p. 14). |

### I/O board

| Code | Title | Cause | Remedy given |
|---|---|---|---|
| 6401 | I/O board is not connected to main board | (1) The I/O board is not connected. (2) Unreliable connection between the *ALLS HX2* and the I/O board. | (1) Connect the I/O board and check its power cable. (2) Reconnect or replace the USB cable between the I/O board and the *ALLS HX2*. |
| 6402 | I/O board does not fulfill the game spec | The correct I/O board is not connected. | Use an I/O board that provides the proper input/output for the game. |

### Network and ALL.Net

| Code | Title | Cause | Remedy given |
|---|---|---|---|
| 8001 | Network address error (DHCP) | The network connection settings could not be initialized. | Check the network connection and restart the *ALLS HX2* following the startup procedure. |
| 8002 | Network setting error (SYSTEM) | NETWORK SETTING in system test mode is incorrect. | Check the network settings (3-9, p. 24). |
| 8003 | Network address error (Dup.IP) | The network connection settings could not be initialized. | Check the network connection and restart. |
| 8004 | Network setting error (Dup.IP) | NETWORK SETTING in system test mode is incorrect. | Check the network settings (3-9, p. 24). |
| 8005 | Network type error (WAN) | The line type of the connected ALL.Net router is incorrect. | Check the line type of the ALL.Net router. |
| 8006 | Network timeout error (DHCP) | The network connection settings could not be initialized. | Check the network connection and restart. |
| 8007 | Network timeout error (DNS-WAN) | A connection could not be established with ALL.Net. | Check the *ALLS HX2* network connection, the in-store network and the link between the ALL.Net router and the network cable, then restart. If the error persists, check the maintenance information. |
| 8008 | Network timeout error (DNS-LAN) | A connection could not be established with the ALL.Net router. | Check the *ALLS HX2* network connection and the in-store ALL.Net connection, then restart. |
| 8009 | Network Game Disabled | The ALL.Net connection in game test mode is set to OFF. | Check the ALL.Net connection setting in game test mode. |
| 8103 | ALL.Net System error (TIMEOUT) | A connection could not be established with ALL.Net. | Same procedure as 8007. |
| 8106 | ALL.Net System Caution | A connection could not be established with ALL.Net. | Same procedure as 8007. |
| 8111 | ALL.Net System error (REG) | ALL.Net registration could not be confirmed. | Check that the ALL.Net registration (the agreement) has been successfully completed. |
| 8113 | ALL.Net System error (MODE) | The ALL.Net settings could not be confirmed. | Contact support. |
| 8114 | ALL.Net System error (RTC) | A connection could not be established with ALL.Net. | Same procedure as 8007. |
| 8201 | ALL.Net System error (TIMEOUT) | A connection could not be established with ALL.Net. | Same procedure as 8007. |
| 8202 | ALL.Net System error (REG) | ALL.Net registration could not be confirmed. | Check that the ALL.Net registration (the agreement) has been successfully completed. |
| 8301 | Network error (GAME-LAN) | The connection with the devices that make up this game could not be confirmed. | Check the network connection and restart. |
| 8302 | Maintenance time (GAME) | The server is currently undergoing maintenance. | Wait until the server maintenance is complete. |
| 8303 | Network error (GAME) | A connection could not be established with ALL.Net. | Same procedure as 8007. |
| 8304 | Network failed (GAME) | An unrecoverable network failure occurred. | Same procedure as 8007. |

## 2. *maimai DX* specific errors (*DX* service manual, chapter 5)

The manual also gives the place where the fault is located ("発生場所").

| Code | Message displayed | Location | Cause | Remedy given |
|---|---|---|---|---|
| 0951 | USB devices are insufficient | `4x RS-232 to USB adapter` | Communication with the `4x RS-232 to USB adapter` is impossible. | Restart. If that is not enough, check the connection of the `4x RS-232 to USB adapter` (`837-15067-02`) and of the USB hub (`837-20008`) (chapter 22 of the instruction manual, general wiring diagram). |
| 3100 | Connection of the code reader or the player camera cannot be confirmed | Code reader or player camera | The connection of the code reader or the player camera cannot be found. | In test mode, use the camera test to find the camera that is not recognized, then check its connection and that of the USB hub (`837-20008`) (3-6, p. 44). |
| 3101 | Code reader recognition failed | Code reader | The camera identification code of the code reader is unreadable. | Clean the camera identification code (14-2 of the instruction manual). |
| 3102 | Player camera not recognized | Player camera | The player camera is not recognized. | Restart. Otherwise, check that the camera is properly connected (chapter 22). |
| 3201 | Reference machine duplicated in the same cabinet group | *ALLS HX2* | Two "reference" machines in the same cabinet group. | Check the game settings and restart the *ALLS HX2* (3-7, p. 46). |
| 3300 | Cannot connect to touch sensor (1P) (timeout) | Touch sensor 1P | The connection to the 1P touch sensor cannot be found. | Check the 1P touch sensor connection (3-5, p. 39 and 11-4 of the instruction manual). |
| 3301 | Touch sensor (1P) initialization failed | Touch sensor 1P | Initialization of the 1P touch sensor failed. | Restart. Otherwise, replace the touch sensor (11-4). |
| 3302 | Cannot connect to touch sensor (2P) (timeout) | Touch sensor 2P | The connection to the 2P touch sensor cannot be found. | Check the 2P touch sensor connection (3-5, p. 39 and 11-4). |
| 3303 | Touch sensor (2P) initialization failed | Touch sensor 2P | Initialization of the 2P touch sensor failed. | Restart. Otherwise, replace the touch sensor (11-4). |
| 8405 | Multiple LAN install servers found (client) | *ALLS HX2* | Several LAN install servers were detected. | Check the LAN install server setting (4-2, p. 67). |
| 8406 | Multiple LAN install servers found (server) | *ALLS HX2* | Several LAN install servers were detected. | Check the LAN install server setting (4-2, p. 67). |

The titles in this section are a translation from the Japanese. Codes 3300 to 3303 concern the touch sensors, not the display screens.

## 3. Other mentions of codes in the manuals

| Code | Manual | Context |
|---|---|---|
| Error 0917 | *DX* instruction manual, PDF pages 77 and 80 (game installation) | The "USB flash drive connected" message is displayed at the end of the installation until the USB drive is removed. See code 0917 above. |
| Error 0091 | *DX* instruction manual, PDF page 151 (*ALLS HX2*) | Clean the *ALLS HX2* once a year or when this code appears. |
| "Stays on the *ALLS* logo without reaching the advertise screen (an error is displayed)" | *DX* instruction manual, PDF page 92 (troubleshooting) | Cause: bad setting or failure of the *ALLS HX2*. Remedy: see the errors chapter of the *ALLS HX2* service manual, and replace the *ALLS HX2* in case of failure. |
