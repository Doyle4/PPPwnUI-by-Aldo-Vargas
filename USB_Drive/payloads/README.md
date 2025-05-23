# PS4HEN v2.1.5

Copy the payload file `ps4-hen-xxxx-PPPwn-vtx.bin` corresponding to the PS4 firmware to the root directory of USB drive exFAT.

Rename the payload file to `payload.bin`.

Insert the USB drive with the payload into the PS4 USB port 0, 1 or 2.

Start PPPwn with the stage2 from PS4HEN VTX or NOBD in PPPwnUI (NOBD is now also handled by stage2 in PS4HEN VTX)

## Github Repository
https://github.com/EchoStretch/ps4-hen-vtx

## Features
- Current Supports 7.00 - 11.00
- Homebrew Enabler
- Jailbreak
- Sandbox Escape
- Debug Settings
- External HDD Support
- VR Support
- Remote Package Install
- Rest Mode Support
- External HDD Format 7.xx Support
- Bypass Firmware Checks
- Debug Trophies Support
- sys_dynlib_dlsym Patch
- UART Enabler
- Never Disable Screenshot
- Remote Play Enabler

## Contributors
Massive credits to the following:
- [qwertyoruiopz](https://twitter.com/qwertyoruiopz)
- [Specter](https://twitter.com/SpecterDev) 
- [flat_z](https://twitter.com/flat_z)
- [idc](https://twitter.com/3226_2143)
- [Joonie](https://github.com/Joonie86/)
- [Vortex](https://github.com/xvortex)
- [zecoxao](https://twitter.com/notzecoxao)
- [SiSTRo](https://github.com/SiSTR0)
- [SocraticBliss](https://twitter.com/SocraticBliss)
- [ChendoChap](https://github.com/ChendoChap)
- [Biorn1950](https://github.com/Biorn1950)
- [Al-Azif](https://github.com/Al-Azif)
- Anonymous

## Helped With Porting
Massive Thanks to the following:
- [BestPig](https://twitter.com/BestPig)
- [LM](https://twitter.com/LightningMods)
- [Al-Azif](https://github.com/Al-Azif)
- [zecoxao](https://twitter.com/notzecoxao)
- [illusion0001](https://twitter.com/illusion0002)

## Changelog:

### PPPwn-1.0333
Update 750.h Fix

### PPPwn-1.0332
Fix offsets for 10.00 and 10.01

### PPPwn-1.0331
Added support for more payloads using Payload Guest application.

### PPPwn-1.0329
Fixed 9.00

### PPPwn-1.0328
Added patches from mira

Added more patches from the mira project with hope of fixing some issues
Thanks Mira Team
https://github.com/OpenOrbis/mira-project
Thanks @BestPig for help with offsets

### PPPwn-1.0324
Fixed FW 8.52

### PPPwn-1.0323
Payload Guest Fix Thanks @BestPig

### PPPwn-1.0322
Reverted to 1.0320

### PPPwn-1.0321
block up fix?

### PPPwn-1.0320
Fixed a compilation warning

### PPPwn-1.0319
Tried to fix rest mode, but it's not very effective.

### PPPwn-1.0318
Updating the submodule PPPwn to the latest version

### PPPwn-1.0317
Eliminated old files and utilizes the SDK

### PPPwn-1.0312
PPPwn Update By @BestPig, Can now load more then once

### PPPwn-1.0310-1.0311
Fixed Offsets For 7.xx

### PPPwn-1.0309
Add some syscalls for Apollo compatibility
Added 7xx Firmwares

Huge thanks to everyone involved with ps4debug, and special appreciation to @bestpig for figuring this out!
https://github.com/BestPig/ps4-hen-vtx
