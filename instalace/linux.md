# Instalace pro Linux

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
 - nainstalovaný prohlížeč [Chrome verze 54 nebo vyšší](https://www.google.com/chrome/browser/desktop/index.html)
 - účet na [GitHubu](https://github.com/)
 - máš v počítači nainstalovaný [Git](http://pyladies.cz/v1/s001-install/git.html) a [Editor](http://pyladies.cz/v1/s002-hello-world/editor.html)
 - zmáknutý pohyb v Terminálu cd, ls nebo dir, nano, mkdir, rm, ovladat šipku nahoru a TAB (pokud máš nastavené autodoplňování na TAB)
 - zmáknutou základní práci s [Git](http://pyladies.cz/v1/s009-git/git.html) a [posíláním commitů na GitHub](http://pyladies.cz/v1/s005-modules/opensource.html)
 - základní znalost konceptů programování v Pythonu - for cyklus, if, def
 - umíš na svém počítači udělat screenshot obrazovky i s výřezem (budeme při kurzu uplatňovat) a víš, kde poté soubory jsou
 - máš nějaké hrubé základy HTML/CSS - div, class ...

***

## Instalace Selenia

Pro automatické testování budeme používat nástroj Selenium. Je to skvělý nástroj pro automatické testování webových aplikací. 
Má podporu pro Firefox, Chrome, Internet Explorer i Safari. Na tomto [odkazu](https://pypi.python.org/pypi/selenium) 
najdeš příkaz, kterým jej nainstaluješ v příkazové řádce.

**Nezapomeň, že bys měl/a mít před instalacemi spuštěné virtuální prostředí.**

![Instalace Selenia](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/all_os_selenium_install.png)

***

## Instalace ovladače

Teď si nainstalujeme ovladač (driver) pro Chrome - Google Chrome Driver.

Balík s ovladačem chromedriver stáhneme z [webu](https://sites.google.com/a/chromium.org/chromedriver/downloads/) pomocí příkazu `wget`

* pro Linux 32bit:
```
wget https://chromedriver.storage.googleapis.com/2.27/chromedriver_linux32.zip
```
* pro Linux 64bit:
```
wget https://chromedriver.storage.googleapis.com/2.27/chromedriver_linux64.zip
```

Rozbalíme ho pomocí `unzip`

* pro Linux 32bit:
```
unzip chromedriver_linux32.zip
```
* pro Linux 64bit:
```
unzip chromedriver_linux64.zip
```

## Nastavení cesty (PATH) k ovladači

Aby byl ovladač spustitelný z prográmků, které budeme tvořit, je třeba ho přidat do proměnné prostředí `$PATH`. Nainstalovaný ovladač chromedriver proto přesuneme do `/usr/local/bin/`: 
```
sudo mv chromedriver /usr/local/bin/
```

Ověříme, že je na správném místě a že je spustitelný: 
```
which chromedriver
```

## Spuštění zkušebního testu

Uděláme si test, který nám pomůže ověřit, že máme vše připravené k testování na Chrome.

Naklonuj si repozitář TestLadies k sobě do počítače do složky TestLadies. Ano, ve složce TestLadies tedy po naklonování budeš mít další složku `TestLadies`. 
Repozitář naklonuješ pomocí příkazu:

```
git clone https://github.com/PyLadiesCZ/TestLadies
```

Ve složce `instalace` najdeš hotový soubor `test_installation.py`. Nastavení ovladače v tomto souboru řeší řádek `browser = webdriver.Chrome('chromedriver')`.

Spusť soubor pomocí `python test_installation.py` (ano, v zapnutém virtuálním prostředí). 
Pokud je vše v pořádku, spustí se prohlížeč, provede se test, prohlížeč se opět vypne a v příkazové řádce se vypíše výsledek testu.
Pokud máš vše nainstalováno správně, v Terminálu se vypíše `Test OK`, pokud je něco špatně, test spadne 
(v tu chvili je něco špatně s instalacemi a je nutné to vyřešit před kurzem), případně vypíše `Sorry, it didn't work`.

Pokud něco nedopadlo správně a potřebuješ poradit. Napiš nám na praha@pyladies.cz, nejlépe udělej screenshot chyby a pošli ho v příloze.

***

**Oficiální dokumentace k Seleniu**

https://seleniumhq.github.io/selenium/docs/api/py/api.html

**Neoficiální dokumentace k Seleniu**

http://selenium-python.readthedocs.io

