PS4 HEN
https://github.com/Scene-Collective/ps4-hen/releases

pre-release-exploit_fixes-92
Add exploit_fixes" for 5.05
- Now to test all of them and find patches made outside of these that are wrong

pre-release-exploit_fixes-91
Add exploit_fixes for 6.72-8.52

pre-release-exploit_fixes-90
Going back and adding these anyway

pre-release-exploit_fixes-89
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

PS4 Firmware support
6.72, 7.55, 9.00, 9.60, 10.00, 10.01, 10.50, 10.70, 10.71, 11.00, 11.02, 11.50, 11.52, 12.00, 12.02

Tested
9.00, 9.60, 10.00, 10.50, 11.00, 11.02, 11.50, 12.00
