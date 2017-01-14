Tipy a triky - MacOS
--------------------

_by @lsdpv_

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

<br>
<br>
<br>
<br>

Tipy a triky - Windows
----------------------

Nástroj na screenshoty - greenshot


Tipy a triky - Linux
--------------------

...

---------------------

Motivaci je sdelit, ze kdyz se nekdo chce zivit sezenim u pocitace, tak by ho mel nalezite umet ovladat. To zejmena znamena nepreskakovat z klavesnice na mys a zpet, kdyz to neni nutne.


zatim me napadlo:

- spusteni, prepinani programu (browser, terminal, editor)
- resize okna - maximalizace, split screen
- prepinani klavesnic, kdyz se pise cesky se specialnimi znaky
- screenshoty - kam se ukladaji, jak udelat vyrez pro vlozeni do githubu

Prosim abyste si pripravili cca 10 min. live ukazku + cheat sheet, ktery dostanou ucastnice vytisteny (bud vygooglit existujici, nebo nahrubo napsat do google docu - projde grafickou upravou)

nase gdrive slozka ke kurzu (komu by chybel pristup, tak se prihlasi)
https://drive.google.com/drive/folders/0B7k_vjnqkd63SFFtZy1FeGdtakU?usp=sharing


---------------------


Alt tab, alt shift tab

V prohlížeči Ctrl+T, Ctrl+Shift+T, Ctrl+Shift+N

terminál - šipka nahoru, tabulátor

cs klávesnice - eng znaky pomocí Alt


---------------------


Inspektor prohlížeče
--------------------

 - skladba Webu DOM, XPath

https://developers.google.com/web/tools/chrome-devtools/


XPath
-----

...


Nástroj na capture videa
------------------------

easy screen cast recorder

jde to i do animovaneho gifu



Zalozit issue na github
-----------------------

Zvládneš to teď lépe než ráno?

