# PS4HEN v2.1.5

Copy the payload file `ps4-hen-xxxx-vtx.bin` corresponding to the PS4 firmware to the root directory of USB drive exFAT.

Rename the payload file to `payload.bin`.

Firmwares Supported:
5.05, 6.72
7.00, 7.01, 7.02, 7.50, 7.51-, 7.55
8.00, 8.01, 8.03, 8.50, 8.52
9.00, 9.03, 9.04, 9.50, 9.51, 9.60
10.00, 10.01, 10.50, 10.70, 10.71
11.00, 11.02, 11.50, 11.52
12.00, 12.02

## Github Repository
https://github.com/EchoStretch/ps4-hen-vtx

## Features
- Current Supports 5.05, 6.72, 7.00 - 12.02
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
- Disable ASLR

## Usage

On your computer, clone the repository:

```sh
git clone --recursive https://github.com/EchoStretch/ps4-hen-vtx.git
```

Compile the payloads:

```sh
./build.sh 900
```
For other firmwares, e.g. FW 12.02, `./build.sh 1202`.

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

### HEN-1.0374
fixed 11.00 hash

### HEN-1.0373
upload_prx_to_disk: show failure notification

### HEN-1.0372
Merge pull request #4 from illusion0001/plugin-loader
- Load PRX into `ScePartyDaemon`

### HEN-1.0366
Merge pull request from illusion0001/plugin-loader
- Load plugins from dynlib_load_prx syscall

### HEN-1.0360
Fix eventhandler_register_addr
Merge pull request from StevenMiller123/fix-offsets

### HEN-1.0358
Update 1200-1202.h

### HEN-1.0357
Fix 1200-1202

### HEN-1.0356
Fixed offset RsaesPkcs1v15Dec2048CRT_addr for 11.02

### HEN-1.0355
Fixed offset DT_HASH_SEGMENT_addr for 11.02

### HEN-1.0354
added back 5.05 fix

### HEN-1.0353
fix oom

### HEN-1.0352
Updated main.c

### HEN-1.0350/51
Updated README.md

### HEN-1.0348
Add Support For 5.05 And 6.72
Added disable ASLR (Address Space Layout Randomization)
Change directory depth limit from 9 to 64

## HEN-1.0346
Required Fix

### HEN-1.0345
Add HEN building for 12.00 / 12.02

### HEN-1.0339
Add HEN building for 12.00 / 12.02

### HEN-1.0338
Add offsets for 12.00 and 12.02

### HEN-1.0337
Update submodule to latest commit

### HEN-1.0336
Added Support For 11.02, 11.50 and 11.52 (Only Hen)
