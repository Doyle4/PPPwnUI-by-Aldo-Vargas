# PPPwnUI
PPPwnUI is a program that adds an UI to the exploit [PPPwn](https://github.com/TheOfficialFloW/PPPwn/) created by [TheFlow](https://github.com/TheOfficialFloW/).

![image](https://github.com/user-attachments/assets/cb51cdc6-2958-49a6-9a19-9dd68802c171)

## Installation

- Clone the repository:

```git clone https://github.com/aldostools/PPPwnUI```

- Install the requirements:

```pip install -r requirements.txt```

- On Windows: download & install [Packet capture library for Windows](https://npcap.com/dist/npcap-1.79.exe)

## Usage

- Launch the app with

  **Windows :**

  ```PPPwnUI.bat```

  **Linux :**

  ```sh
  chmod +x PPPwnUI.sh
  ```

  Then :

  ```sh
  ./PPPwnUI.sh
  ```

- Select your Interface using the drop-down menu

- Choose PPPwn (7.00 to 11.00)

- Or Choose the Goldhen PPPwn (9.00, 9.50, 9.51, 9.60, 10.00, 10.01, 10.50, 10.70, 10.71 & 11.00)

- Or use PS4HEN VTX with USB payload.bin Loader (7.00 to 11.00)

- Or Choose the PPPwn Linux Payloads (Available only for 11.00)

- You can also add your own custom Payloads.

- Click on **Start PPPwn** to start the Exploit


### PPPwn (7.00 to 11.00)
PPPwn is a kernel remote code execution exploit for PlayStation 4 up to FW 11.00.
The exploit only prints PPPwned on your PS4 as a proof-of-concept. In order to launch homebrew, use GoldHEN, VTX HEN or a custom stage2.bin payload.
Credits to TheFlow0 and devs that contributed to his repository https://github.com/TheOfficialFloW/PPPwn

PPPwn is available for the following 23 firmwares:
* 7.00, 7.01, 7.02
* 7.50, 7.51, 7.55
* 8.00, 8.01, 8.03
* 8.50, 8.52
* 9.00
* 9.03, 9.04
* 9.50, 9.51, 9.60
* 10.00, 10.01
* 10.50, 10.70, 1071
* 11.00

### Goldhen PPPwn (9.00, 9.60, 10.00, 10.01, 10.50, 10.70, 10.71 & 11.00)
Put golden.bin in the root of USB Drive and plug it in USB port before start the payload.
If found, it is copied to the internal HDD at this path: /data/GoldHEN/payloads/goldhen.bin.
After the installation, the file is not longer needed in the USB drive.
Check the folder USB Drive (GoldHEN_v2.4b18) for additional information.

Using stage2 version 1.03 by SiSTR0. GoldHEN is still in development for 9.50, 9.51 (TBD).
Next fw version to be added will be 9.03. A lite version for 9.00 is included.

Credits to SiSTR0 and devs that contributed to his repository https://github.com/SiSTR0/PPPwn

### PS4HEN VTX  (7.00 to 11.00)
Stage2 by @LightningMods & @EchoStrech with BinLoader integraded for normal and NOBD consoles.
PS4HEN is available for the 23 firmwares supported by PPPwn.

PS4HEN VTX payloads by @EchoStrech & @BestPig include Homebrew Enabler, Jailbreak, Debug Settings, Remote Package Install among other features found in Goldhen.
It doesn't include FTP Server, BinLoader, FPS Counter, Integrated Cheat Menu, FW Update Block, Plugins Support, Internal pkg installation among other features.
This is only an alternative method to GoldHEN and a temporary solution specially for the firmware versions not supported yet by GoldHEN payload.

PPPwnUI now copies the PS4-HEN-PPPwn-VTX payload to "USB Drive" folder. Or rename the one of the payloads in "Additional Payloads" by LightningMods as `payload.bin`
Copy `payload.bin` to the root directory of USB EXFAT drive and start PPPwn from PS4HEN VTX or PS4HEN NODB tabs.

Credits to all contributors in ps4-hen-vtx.
Special thanks to xVortex, SiSTR0, EchoStrecth and BestPig for his releases in Discord and https://github.com/EchoStretch/ps4-hen-vtx

### PPPwn Linux Payloads (Available only for 11.00)
This payload lets run PS4 Linux on 11.0 firmware. If you're on 9.00, it's recommended to stay in that version.
Check https://ps4linux.com/ps4-linux-11-0-payloads-pppwn-tutorial/ for detailed information.

Credits to EinTim23, LightningMods, sleirsgolvy, the Psxita Team, TheFlow0 and all the contributos to https://github.com/EinTim23/PS4-Linux-Loader

## PPPwn Usage

On your PS4:

- Go to `Settings` and then `Network`
- Select `Set Up Internet connection` and choose `Use a LAN Cable`
- Choose `Custom` setup and choose `PPPoE` for `IP Address Settings`
- Enter anything for `PPPoE User ID` and `PPPoE Pasword`
- Choose `Automatic` for `DNS Settings` and `MTU Settings`
- Choose `Do Not Use` for `Proxy Server`
- Click `Test Internet Connection` to communicate with your computer

If the exploit fails or the PS4 crashes, you can skip the internet setup and simply click on `Test Internet Connection`. If the script fail or is stuck waiting for a request/response, abort it and run it again on your computer, and then click on `Test Internet Connection` on your PS4.

### Goldhen Usage

On your Computer:

- Copy `goldhen.bin` to the root directory of an exfat/fat32 USB and insert it into your PS4.

#### Example run

```sh
[+] PPPwn - PlayStation 4 PPPoE RCE by theflow
[+] args: interface=enp0s3 fw=1100 stage1=stage1/stage1.bin stage2=stage2/stage2.bin

[+] STAGE 0: Initialization
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634beba00
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] Source MAC: 07:ba:be:34:d6:ab
[+] AC cookie length: 0x4e0
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...
[*] Waiting for interface to be ready...
[+] Target IPv6: fe80::2d9:d1ff:febc:83e4
[+] Heap grooming...done

[+] STAGE 1: Memory corruption
[+] Pinning to CPU 0...done
[*] Sending malicious LCP configure request...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...
[+] Scanning for corrupted object...found fe80::0fdf:4141:4141:4141

[+] STAGE 2: KASLR defeat
[*] Defeating KASLR...
[+] pppoe_softc_list: 0xffffffff884de578
[+] kaslr_offset: 0x3ffc000

[+] STAGE 3: Remote code execution
[*] Sending LCP terminate request...
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634beba00
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] Source MAC: 97:df:ea:86:ff:ff
[+] AC cookie length: 0x511
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Triggering code execution...
[*] Waiting for stage1 to resume...
[*] Sending PADT...
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634be9200
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] AC cookie length: 0x0
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...

[+] STAGE 4: Arbitrary payload execution
[*] Sending stage2 payload...
[+] Done!
```

This Program was originally made with ❤️ by [Memz](https://github.com/B-Dem) for [Sighya](https://sighya.fr).

If you find this program helpful, leave a star on the repo!

And if you got any feedback, open an issues !
