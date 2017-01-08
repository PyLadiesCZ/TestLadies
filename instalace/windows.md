# Instalace pro Windows

## Před instalací
Pokud nemáš ještě tolik zkušeností, bude dobré, když se budeš držet tohoto návodu včetně pojmenování složek.  
Nejprve si založ novou složku pojmenovanou `TestLadies`, ve svém počítači na místě, kde běžně vznikají tvé nové programovací projekty.

Pokud si nejsi jist/á jak se vytváří a spouští Python soubory, 
[projeď si prosím tento manuál vytvořený pro PyLadies](http://pyladies.cz/v1/s002-hello-world/hello-world.html).

***

## Instalace Pythonu, virtuálního prostředí a prohlížečů
Nejprve musíme vše správně nainstalovat a nastavit. Pokud máš již v počítači nainstalovaný Python 3 (pokud máš Python 2 a potřebuješ jej uchovat, 
vyřešíš to nainstalováním Pythonu 3 do virtualenv přímo ve složce projektu) a umíš vytvořit virtuální prostředí 
pro práci v Pythonu, máš na půl vyhráno. Pokud s tím potřebuješ pomoci, tak nejlépe postupuj 
podle materiálů [instalace Pythonu a venv vytvořených pro PyLadies.](http://pyladies.cz/v1/s001-install/instalace.html)

## Co bys měl/a před kurzem vědět, aby vše dobře probíhalo

Než budeš instalovat dál, předpokladem je, že máš:

 - nainstalovanou poslední stabilní verzi Python 3 (v době psaní tohoto textu to byla 3.5.2)
 - vytvořené virtuální prostředí
 - spuštěné virtuální prostředí - příkaz ```source venv/bin/activate```
 - nainstalovaný prohlížeč [Chrome](https://www.google.com/chrome/browser/desktop/index.html)
 - účet na [GitHubu](https://github.com/)
 - máš v počítači nainstalovaný [Git](http://pyladies.cz/v1/s001-install/git.html) a [Editor](http://pyladies.cz/v1/s002-hello-world/editor.html)
 - zmáknutý pohyb v Terminálu cd, ls nebo dir, nano, mkdir, rm, ovladat šipku nahoru a TAB (pokud máš nastavené autodoplňování na TAB)
 - základní znalost konceptů programování v Pythonu - for cyklus, if, def
 - umíš na svém počítači udělat screenshot obrazovky i s výřezem (budeme při kurzu uplatňovat) a víš, kde poté soubory jsou
 - máš nějaké hrubé základy HTML/CSS

***

## Instalace Selenia

Pro automatické testování budeme používat nástroj Selenium. Je to skvělý nástroj pro automatické testování webových aplikací. 
Má podporu pro Firefox, Chrome, Internet Explorer i Safari. Na tomto [odkazu](https://pypi.python.org/pypi/selenium) 
najdeš příkaz, kterým jej nainstaluješ v příkazové řádce.

**Nezapomeň, že bys měla mít před instalacemi spuštěné virtuální prostředí.**

![Instalace Selenia](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/all_os_selenium_install.png)

***

## Instalace ovladače

Teď si nainstalujeme ovladač (driver) pro Chrome - Google Chrome Driver

Ovladač najdeš na stránce až po scrollování kousek níž [zde](http://docs.seleniumhq.org/download/)

Stáhni si Google Chrome Driver do složky `WebDrivers`. 
![Ovladače najdeš na stránce až po scrollování kousek níž.](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/all_os_drivers_install.png)

## Nastavení cesty (PATH) k ovladači

Uděláme si test, který nám pomůže ověřit, že máme vše připravené k testování na Chrome.
Hotový soubor `test_installation.py` s testem najdeme v repozitáři TestLadies na GitHubu, [ze složky instalace.](https://github.com/PyLadiesCZ/TestLadies/tree/master/instalace) 

Naklonuj si repozitář TestLadies k sobě do počítače do složky TestLadies. Ano ve složce TestLadies tedy budeš mít po naklonování dvě složky - `WebDrivers` a `TestLadies`. 
Repozitář naklonuješ pomocí příkazu:
```git clone https://github.com/PyLadiesCZ/TestLadies```

Nastavení PATH pro Chrome na Windows je snadné. Řeší to řádek `browser = webdriver.Chrome('chrome')` v souboru `test_installation.py`. 
Driver pro Chrome musíš mít ve složce `WebDrivers`, dale již není potřeba nastavovat PATH.

***

***Ověř si, zda je vše nastaveno správně:***
V příkazové řádce spusť soubor z nově naklonované složky `TestLadies` pomocí `python test_installation.py` (ano, v zapnutém virtuálním prostředí). 
Pokud je vše v pořádku, spustí se prohlížeč, provede se test, prohlížeč se opět vypne a v příkazové řádce se vypíše výsledek testu.
Pokud máš vše nainstalováno správně, v Terminálu se vypíše `Test OK`, pokud je něco špatně, test spadne 
(v tu chvili je něco špatně s instalacemi a je nutné to vyřešit před kurzem), případně vypíše `Sorry, it didn't work`.

Pokud něco nedopadlo správně a potřebuješ poradit. Napiš nám na praha@pyladies.cz

***

**Oficiální dokumentace k Seleniu**

https://seleniumhq.github.io/selenium/docs/api/py/api.html

**Neoficiální dokumentace k Seleniu**

http://selenium-python.readthedocs.io


