# TestLadies
Web testing course for beginners.

Work in progress.

***

##Instalace
Nejprve musíme vše správně nainstalovat a nastavit. Pokud máš již v počítači nainstalovaný Python 3 a umíš vytvořit virtuální prostředí pro práci v Pythonu, máš na půl vyhráno. Pokud s tím potřebuješ pomoci, tak nejlépe postupuj podle materiálů [instalace Pythonu a venv vytvořených pro PyLadies.](http://pyladies.cz/v1/s001-install/instalace.html)

Než budeš instalovat dál, předpokladem je, že máš:

 - nainstalovanou poslední stabilní verzi Python 3
 - vytvořené virtuální prostředí
 - spuštěné virtuální prostředí
 - kromě primárního prohlížeče:

	>  - pro Windows - Internet Explorer 
	>  - pro macOS - Safari
	>  - pro Linux - již běžně Firefox či Chrome

si doinstaluj ještě Firefox a Chrome (automatické testy budeme psát na všechny, abychom si byli jistí, že naše webová aplikace funguje ve všech prohlížečích stejně)

***

## Instalace Selenia

Pro automatické testování budeme používat nástroj Selenium.  Je to skvělý nástroj pro automatické testování webových aplikací. Má podporu pro Firefox, Chrome, Internet Explorer i Safari. Můžeš si tak vybrat podle platformy i prohlížeče, který používáš a také využít všech možností pro komplexní automatizaci a testování. Na tomto [odkazu](https://pypi.python.org/pypi/selenium) najdeš příkazy, kterými jej nainstaluješ v příkazové řádce. Postup se pro Windows, macOS a Linux nijak neliší.

![Použij jednotlivé příkazy.](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/all_os_selenium_install.png)

## Instalace ovladačů
Teď si nainstalujeme ovladače (drivery) pro jednotlivé prohlížeče. 
Nezapomeň je nainstalovat pro všechny prohlížeče, na kterých budeš testovat. Pro *Windows* tedy Internet Explorer, Firefox, Chrome. Na *macOS* pro Safari, Firefox a Chrome. Na *Linux* Firefox a Chrome.
Ovladače:
 pro Firefox - Mozzila GeckoDriver
 pro Safari - SafariDriver
 pro IE - Microsoft Edge Driver
 pro Chrome -  Google Chrome Driver

Instalace ovladačů najdeš [zde].(http://docs.seleniumhq.org/download/)
Stáhni si je a nainstaluj poklepáním.

![Ovladače najdeš na stránce až po scrollování kousek níž.](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/all_os_drivers_install.png)

 
XXX Doplnit k cemu drivery slouzi.

## Nastavení cesty pro každý prohlížeč zvlášť

XXX poladit cesty k browseru pro kazdy prohlizec na kazdem systemu zvlast TODO Veronika a Magda
http://stackoverflow.com/questions/40269229/python-selenium-3-0-firefox-47-0-1-installed-in-default-location-is-not-identi

### Windows

*Internet Explorer*
*Firefox*
*Chrome*

### macOS

*Safari*

Nastavení pro Safari je naštěstí velmi jednoduché. Řeší to přidání dvou řádků do scriptu s testem. 

`browser = webdriver.Safari()`

`browser.get('http://seleniumhq.org/')`

![Náhled nastavení pro Safari.](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/macos_safari_path.png)

*Firefox*

*Chrome*

### Linux

*Firefox*
*Chrome*

***

**Oficiální dokumentace k Seleniu**

https://seleniumhq.github.io/selenium/docs/api/py/api.html

**Neoficiální dokumentace k Seleniu**

http://selenium-python.readthedocs.io
