: Open URL
: start https://github.com/aldostools/pppwnui/releases

: Restart Computer
: %windir%\System32\shutdown.exe -r

: Shutdown Computer
: %windir%\System32\shutdown.exe -s

: Stanby Computer [Sleep Mode]
: %windir%\System32\rundll32.exe powrprof.dll,SetSuspendState 0,1,0

: Hybernate
: %windir%\System32\rundll32.exe powrprof.dll,SetSuspendState Hibernate

: Logoff Computer
: %windir%\System32\shutdown.exe -l

: Open Application
: explorer.exe

echo PPPwned!
