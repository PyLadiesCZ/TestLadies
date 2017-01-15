Zdrojové kódy automatizovaných testů

Instalace
---------

Nejdříve je trěba mít nainstalované selenium ve virtual envu a ten musí být zapnutý, viz kapitola [instalace](../instalace)

`pip install`

Vytvoř soubor s proměnnýma `variables.json`

```
{
  "username": "xxx",
  "password": "yyy",
  "invalid_username": "asdf@asdf.cz",
  "invalid_password": "asdf",
  "category": "Clothing",
  "product_name": "Django T-shirt"
  "first_name": "aaa",
  "last_name": "bbb",
  "address_line1": "ccc",
  "city": "ddd",
  "zip_code": 11111,
  "country": "CZ"
}
```


Spuštění
--------

Rozmanitá konfigurace se po spuštění načte z [pytest.ini](pytest.ini), to nám ušetří vypisování parametrů do terminálu.

Vlastní spuštění testů se dělá v adresáři `src` se zapnutým `venv` pomocí příkazu

`(venv) src $ pytest`

V konzoli vidíme, jak to dopadlo. Pokud nás zajímají detaily (včetně screenshotů), tak ty najdeme ve vygenerovaném HTML reportu v `src/report/index.html`.


Ten si můžeme otevřít v tzv. "lokálně". V okně prohlížeče `Soubor > Otevřít` nebo `Ctrl`+`O` a pak najít soubor, nebo elegantně z terminálu příkazem.

`(venv) src $ google-chrome report &`


