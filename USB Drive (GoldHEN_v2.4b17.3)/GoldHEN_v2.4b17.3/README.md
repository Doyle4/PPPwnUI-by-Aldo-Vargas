# GoldHEN - PS4 Homebrew Enabler
```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  _________________  .____  ________    ___ ______________ _______
 /  _____________  \ |    | \______ \  /   |   \_   _____/ \      \
/   \  ___  /   |   \|    |  |    |  \/    ~    \    __)_  /   |   \
\    \_\  \/    |    \    |__|    `   \    Y    /        \/    |    \
 \______  /\_______  /_______ \_____  /\___|_  /_______  /\____|__  /
        \/         \/        \/     \/       \/        \/         \/
                              Coded By
        _________.__  ____________________________ ________
       /   _____/|__|/   _________    _________   \\_____  \
       \_____  \ |  |\_____  \   |    |  |       _/ /   |   \
       /        \|  |/        \  |    |  |    |   \/    |    \
      /_______  /|__/_______  /  |____|  |____|_  /\_________/
              \/            \/                  \/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
## Supported Firmware

- 5.05
- 6.71 / 6.72
- 9.00
- 9.60
- 10.00 / 10.01
- 11.00

## Features

- Homebrew Enabler
- Debug Settings
- VR Support
- Remote Package Install
- Rest Mode Support
- External HDD Support
- Official External HDD Format Support
- Debug Trophies Support
- sys_dynlib_dlsym Patch
- UART Enabler
- Never Disable Screenshot
- Remote Play Enabler
- FW Update Block
- FTP Server on 2121 port (Thanks to [hippie68](https://github.com/hippie68))
- BinLoader Server on 9090 port
- Klog Server on 3232 port
- CE-30391-6 Error CMOS Fix
- Integrated Cheat Menu
- Integrated FPS Counter
- Plugins support
- TitleId label feature
- Scanlines overlay
- Internal pkg installation support (/data/pkg) (Thanks to [OSM](https://github.com/OSM-Made))

### Notes

This new release supports both the previous WebKit exploits and the new pppwn, but for this it requires a custom stage2 that I wrote and released the [code](https://github.com/SiSTR0/PPPwn)

### :warning: Warnings

The BinLoader server is in an experimental phase but in any case there are several payloads around, some even not very well done, which can also be harmful and in the best case only crash the console. So use it with caution.
I have tried to work out to support all payloads possible but no guarantees can be given on this. Obviously I do not take any responsibility in case of use of payloads not made by me.

### :warning: Cheat Menu

The Cheat Menu is experimental, use with caution.
Please report cheat related issues to the cheat author(s).

Read CHEATMENU.md

### Credits

Coded by [SiSTRo](https://github.com/SiSTR0)

Cheat Menu coded by:
- [ctn123](https://github.com/ctn123)
- [Shinigami](https://github.com/ScriptSK)
- [SiSTRo](https://github.com/SiSTR0)

[Cheat Manager](https://github.com/GoldHEN/GoldHEN_Cheat_Manager) coded by:
- [bucanero](https://github.com/bucanero)

[Plugin SDK](https://github.com/GoldHEN/GoldHEN_Plugins_SDK) coded by:
- [bucanero](https://github.com/bucanero)
- [ctn123](https://github.com/ctn123)
- [jocover](https://github.com/jocover)
- [nik](https://github.com/nkrapivin)
- [OSM](https://github.com/OSM-Made)
- [SiSTRo](https://github.com/SiSTR0)

Plugin SDK uses [OpenOrbis-PS4-Toolchain](https://github.com/OpenOrbis/OpenOrbis-PS4-Toolchain) so thanks to all [OpenOrbis](https://github.com/OpenOrbis) devs

Special thanks:
- [golden](https://github.com/jogolden)
- [Joonie](https://github.com/Joonie86)
- [Kameleon](https://github.com/kmeps4)
- [OSM](https://github.com/OSM-Made)

Greeting to other devs:
- [Al-Azif](https://github.com/Al-Azif)
- [ChendoChap](https://github.com/ChendoChap)
- [flat_z](https://github.com/flatz)
- [idc](https://github.com/idc)
- [kiwidoggie](https://github.com/kiwidoggie)
- [qwertyoruiop](https://twitter.com/qwertyoruiopz)
- [sleirsgoevy](https://github.com/sleirsgoevy)
- [Specter](https://github.com/Cryptogenic)
- [SocraticBliss](https://github.com/SocraticBliss)
- [Vortex](https://github.com/xvortex)
- [zecoxao](https://twitter.com/notzecoxao)
- [Znullptr](https://github.com/dmiller423)

Greeting to QA/Testers:
- [Arczi](https://www.psxhax.com/members/archi55.566599)
- [Big_Wadger](https://twitter.com/big_wadger)
- [Brandon Alberhasky](https://twitter.com/alberhasky)
- [Echo Stretch](https://twitter.com/StretchEcho)
- [Marcus Andre](https://github.com/marcussacana)
- [MGS_PS4_PS5_HB_Tester](https://twitter.com/MSZ_MGS)
- [Pharaoh2k](https://github.com/Pharaoh2k)

Greeting Notes:
I'd like to take this opportunity to thank the people without whom we wouldn't have this (and other) release today:
- TheFlow for releasing his exploit (and not just this one) to everyone.
- flat_z for conceiving and publishing the hen for ps4 with a writeup.
- vortex for implementing the first versions of the hen.
- golden for creating projects that helped me understand many things.
- OSM for his cool Orbis Toolbox.
- Hippie68 for his work on the new FTP server.
- Al_Azif for providing various necessary resources.
- SocraticBliss for his RE scripts.
- Illusion for his game patches and more.
- bucanero for his work on the cheat manager.
- All the cheat developers who shared their trainers with everyone.

Thanks to the testers who had so much patience:
- Big_Wadger
- EchoStretch
- Opoisso893
- mbcrumb
- MODDED WARFARE
- vapour

Last but not least, my friends ctn and Kameleon for their continuous support, not only technical!

Thanks also to everyone who supported my project on kofi.

### Note
Project source code is currently private because over time I have seen a sad abuse of the source code that I, like the previous devs who worked on it, have been pleased to make it available to everyone to study and maybe improve it.

### Donations
Consider [donating](https://goldhen.github.io/support) if you like GoldHEN and want to support my work

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/SiSTRo)