# PS4 HEN
https://github.com/Scene-Collective/ps4-hen/releases

# Features
- Current Supports 5.05 - 12.50
  5.05, 6.72, 7.55, 9.00, 9.60, 10.00, 10.01, 10.50, 10.70, 10.71, 11.00, 11.02, 11.50, 11.52, 12.00, 12.02, 12.50
- Homebrew Enabler
- Plugins System
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

git clone https://github.com/Scene-Collective/ps4-payload-sdk.git
sudo ./install.sh
Clone the repository:

git clone https://github.com/Scene-Collective/ps4-hen.git
Compile the payload:

./build.sh
