# PS4 HEN v2.2.0 BETA
https://github.com/Scene-Collective/ps4-hen/releases
https://github.com/Scene-Collective/ps4-hen-plugins/releases

# Features
- Current Supports 4.74 - 12.52
  4.74, 5.00, 5.01, 5.03, 5.05, 5.07, 5.50, 5.53, 6.72,
  7.00, 7.01, 7.02, 7.50, 7.51, 7.55, 8.00, 8.01, 8.03, 8.50, 8.52,
  9.00, 9.03, 9.04, 9.50, 9.51, 9.60, 10.00, 10.01, 10.50, 10.70, 10.71,
  11.00, 11.02, 11.50, 11.52,  12.00, 12.02, 12.50, 12.52

  WIP: 5.55, 5.56, 6.00, 6.02, 6.20, 6.50, 6.51, 6.70, 6.71

- Homebrew Enabler
- Plugins System
  - Patches ShellUI to allow more features.
    - Features:
      - More details at plugin_mono page
  - Load PRX into ScePartyDaemon
    - (Starts kernel log server on port 3232, based on klogsrv)
    - (Starts FTP server on port 2121, based on ftpsrv)
      - Note: No SELF decryption yet.
  - Load PRX into retail apps (on startup in CRT _init_env) (You can make your own, the bundled one only prints to TTY for now)
- Jailbreak
- Sandbox Escape
- Debug Settings
- External HDD Support
- VR Support
- Remote Package Install
- Rest Mode Support
- External HDD Format Support
- Bypass Firmware Checks
- Debug Trophies Support
- sys_dynlib_dlsym Patch
- UART Enabler
- Never Disable Screenshot
- Remote Play Enabler
- Disable ASLR

# Changelog

pre-release-main-151
Clean.sh: delete only files in `tmp` (#34)

## pre-release-main-149
Delete old file on write (#33)
When updating config files on old version, it doesn't get overwritten for some reason.

## pre-release-exploit_fixes-146
Reparse config after notification (#32)
Fixes wrong version number in notification

## pre-release-main-143
Install shellcode for shellcore to load prx (#31)

Will be used in the future for game patch plugin.
Must have `skip_patches` disabled to use this feature.

## pre-release-main-140
Add more FW support (#30) (Merging now to fix build errors)

### Current support

- 4.74-5.53
- 6.72-12.52

### WIP

- 5.55-6.71

### Why 4.74?

Starting with firmware version 5.00, Sony introduced a requirement for a
**working Blu-ray drive** to perform console firmware updates. While
this restriction can be bypassed, it requires HEN and custom patches
applied to the system.

By targeting firmware back to at least 4.74, we ensure:

**Universal Compatibility** - Works on consoles with broken or missing
BD drives
**Maximum Accessibility** - Available to the widest range of users
**Flexible Options** - Users can choose to:
  - Stay on their current firmware with HEN
  - Use the homebrew update method to update their firmware

## pre-release-main-130
Enable exploit fixes by default (#25)

## pre-release-main-129
[DRAFT] WIP NoBD Support (#26)

## pre-release-main-124
Reparse config after updating it (#23)

## pre-release-main-123
Fix warn about missing default value usage

## pre-release-main-119
Link shellui to plugin mono section in plugins (#22)

## pre-release-main-118
Exploit fixes (#21)

## pre-release-main-115
Check if HEN is already installed (#20)
Skip reinstalling if it is

## pre-release-main-113
Load ShellUI Plugin (#18)

Needs testing on other firmwares
Plugin source:
https://github.com/Scene-Collective/ps4-hen-plugins/tree/main/plugin_mono/source

### Confirmed working firmwares

- 5.05
- 6.72
- 9.00
- 11.00
- 12.02

## pre-release-exploit_fixes-105
How the... more off by ones

## pre-release-exploit_fixes-104
Unpatch last bytes of copyin, copyout, copinstr

## pre-release-exploit_fixes-100
Add 12.50 support (#19) by Al-Azif

## pre-release-exploit_fixes-94
Should be "done" with fixes, just needs testing/verification

## pre-release-exploit_fixes-93
Update comment for exploit_fixes in the ini

## pre-release-exploit_fixes-92
Add exploit_fixes" for 5.05
- Now to test all of them and find patches made outside of these that are wrong

## pre-release-exploit_fixes-91
Add exploit_fixes for 6.72-8.52

## pre-release-exploit_fixes-90
Going back and adding these anyway

## pre-release-exploit_fixes-89
"exploit_fixes" for 9.00-12.02

We assume they have allow calling syscalls everywhere and syscall 11 patched correctly before we could even reach this code, so we won't include those.
pre-release-main-88
Determine proc struct p_comm/path offset at runtime, should enable support for firmwares with a different size/layout for it's proc structure... like 5.05.

pre-release-main-85
Refactor

- Add missing screenshot enabler patch (Probably got deleted onaccident)
- Order SceShellCore patches to be the same as the offset files
- Match formatting up
- Adjust/cast some types to clear warnings
- Use same header guard style everywhere
- Update Makefiles
- Split up files more
- More config options (Check hen.ini, just have it on the root of your flash drive when you run HEN)
  - Toggle old features
  - Enable/Disable plugin system
- Skip SSC, SSU, and RemotePlay patches (Testkits should work with HEN now)
- Config is now passed to kpayload as well
- Add min/max FW check
- Add .clang-format

# Building
Instructions provided are for Debian based systems. (Tested on Ubuntu)

Install ps4-payload-sdk:
```
git clone https://github.com/Scene-Collective/ps4-payload-sdk.git
sudo ./install.sh
```
Clone the repository:
```
git clone https://github.com/Scene-Collective/ps4-hen.git
```
Compile the payload:
```
./build.sh
```
#Contributors
Massive credits to the following:

- qwertyoruiopz
- Specter
- flat_z
- idc
- Joonie
- Vortex
- zecoxao
- SiSTRo
- SocraticBliss
- ChendoChap
- Biorn1950
- Al-Azif
- Anonymous
- illusiony

# Helped With Porting
Massive Thanks to the following:

- BestPig
- LM
- Al-Azif
- zecoxao
