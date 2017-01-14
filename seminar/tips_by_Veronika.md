# Alias
## Ukázka pro Linuxáře a Mackaře
```
nano ~/.bash_profile
alias documents='cd /Documents'
```

## Ukázka pro Windowsáře
```
doskey ..=cd ..\..
```

# Automatizované spouštění - vykradeno z zive.cz
## Ukázka pro Windowsáře
Schelude Task - schtasks.exe     https://msdn.microsoft.com/en-us/library/windows/desktop/bb736357(v=vs.85).aspx




### A
Chci zapnout outlook po prichodu do prace
```
schtasks /create /tn SpustitOutlookPoPrihlaseni /sc onlogon /tr "c:\program files\microsoft office 15\root\office15\outlook.exe"
```

`CREATE – budu vytvářet novou úlohu`
`TN SpustitOutlookPoPrihlaseni – Task Name, tedy název úlohy`
`SC onlogon – Schedule, tedy spouštěč úlohy; v tomto případě okamžik přihlášení`
`TR „c:\....“ – Task Run, tedy program, který má úloha spustitVíce na: http://www.zive.cz/clanky/zacnete-skutecne-ovladat-pc-pouzivejte-prikazovou-radku/sc-3-a-173241/default.aspx`

### B
Chci vedet, ze mam jit z prace domu
```
schtasks /create /tn HuraDomu /sc daily /st 18:30 /tr "sounder c:\windows\media\alarm01.wav"
```

`ST – Start Time, tedy čas začátku ve formátu HH:MMVíce na: http://www.zive.cz/clanky/zacnete-skutecne-ovladat-pc-pouzivejte-prikazovou-radku/sc-3-a-173241/default.aspx`



## Ukázka pro Linuxáře a Mackaře
Cron 
