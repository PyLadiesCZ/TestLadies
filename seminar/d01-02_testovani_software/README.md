
Co je to testování software
---------------------------

- co je to software?
- co je to testování?
- co je to kvalita?

> Whatever the definition, it is true that quality is something we all aspire to.

http://softwaretestingfundamentals.com/software-quality/

http://softwaretestingfundamentals.com/dimensions-of-software-quality/

http://softwaretestingfundamentals.com/software-testing-myths/


Proč je testování SW důležité?
------------------------------

V konečném důsledku způsobují chyby v SW ztráty (bohužel i ty nejhorší) https://youtu.be/TDynSmrzpXw?list=PLDC2A0C8D2EC934C7

Zkuste se zamyslet, co se může stát při kopírování souboru https://youtu.be/rFaWOw8bIMM?list=PLDC2A0C8D2EC934C7

<details>
<summary>_ORGANIZAČNÍ POZNÁMKA_</summary>
![01](01.png)
</details>



O čem je a o čem není tento kurz
--------------------------------

Testování software je mnoho různých typů.

- Praktické testování webů - __to jsme my!__
- Desktopové systémy - úzkoprofilové - korporátní starší systémy
- Embedded systémy - formální - např. vyhýbky na železnici

![logical_organization_of_testing](http://images.slideplayer.com/5/1493816/slides/slide_5.jpg)

zdroj http://slideplayer.com/slide/1493816/

![02](02.png)

zdroj https://youtu.be/n2A9OakDYcY?list=PLDC2A0C8D2EC934C7

- Unit testing - v Pythonu např. https://hypothesis.readthedocs.io/en/latest/
- Akceptace - to nás zajímá - jak se to formalizuje?

![03](03.png)


Usability testing
-----------------

testování použitelnosti - to je sranda, ale netýká se nás to - https://en.wikipedia.org/wiki/Usability_testing

![04](04.png)

zdroje https://lynnewatanabe.wordpress.com/2011/08/24/could-usability-testing-of-websites-help-non-profits-heck-yeah/ https://medium.com/@nickvanderlinde/how-we-do-user-testing-at-mirabeau-223996ad841f

Software lifecycle (životní cyklus)
-----------------------------------

interaktivní hra - seřadit fáze životního cyklu


<details>
<summary>Obrázky</summary>
![sw_lifecycle_01](sw_lifecycle_01.png)<br>
![sw_lifecycle_02](sw_lifecycle_02.png)<br>
![sw_lifecycle_03](sw_lifecycle_03.png)<br>
![sw_lifecycle_04](sw_lifecycle_04.png)
</details>

<details>
<summary>Fáze</summary>
![sw_lifecycle_05](sw_lifecycle_05.png)<br>
![sw_lifecycle_06](sw_lifecycle_06.png)<br>
![sw_lifecycle_07](sw_lifecycle_07.png)<br>
![sw_lifecycle_08](sw_lifecycle_08.png)<br>
![sw_lifecycle_09](sw_lifecycle_09.png)<br>
</details>


<details>
<summary>_ORGANIZAČNÍ POZNÁMKA_</summary>
original inspirace ![05](05.png)<br>
zdroj https://youtu.be/An7HC1LolDM?list=PLDC2A0C8D2EC934C7
</details>

Kdo co dělá?
------------

Jaké role se podílejí na jednotlivých fázích projektu?

![roles_phases](http://cycoda.com/assets/images/rup_poster_lg.jpg)



Metodiky vývoje
---------------

Waterfall, V-model, Spiral, Agile

![06](06.png)

![07](07.png)


Metodiky provozu ITIL
---------------------

continuous improvement

![09](09.png)

![08](08.png)

zdroj http://www.itsmsolutions.com/newsletters/DITYvol4iss01.htm


Jak to budeme dělat?
--------------------

Bušit, jako hluší do vrat - tzv. black box testing

Praktická ukázka, např. PSČ (najít, screenshot, založit ticket)


Co je to ten bug?
-----------------

https://en.wikipedia.org/wiki/Software_bug

![bug](https://upload.wikimedia.org/wikipedia/commons/8/8a/H96566k.jpg)


Teorie k reportování chyb
-------------------------

ruzne ukazky ticketovacich toolu

- jira
- github
- bitbucket
- trac
- redmine

![11](11.png)

zdroj: https://youtu.be/EKv85-K_6w4?list=PLDC2A0C8D2EC934C7


github.com :heart:
------------------


Repozitář kódu

Dokumentace

Ticket tool - issues


Teorie k životu issue
---------------------

![12](12.png)

zdroj https://youtu.be/NpDZ2NJmDrE?list=PLDC2A0C8D2EC934C7



Co je pod pokličkou projektu
----------------------------

- Víš jak přibližně funguje web? Jaký je rozdíl mezi hostingem a DNS jménem?

- Kde je to co testujeme - dev, qa, prod

- oddělená data
  - Aplikace | Databáze
  - https://www.google.com/search?q=web+application+schema&source=lnms&tbm=isch&sa=X#tbm=isch&q=web+application+tiers https://www.safaribooksonline.com/library/view/internet-world/9780132990455/ch17lev1sec3.html

![10](10.png)

- Co s tím budeme dělat
  - Kopie projektu s testovací databází

