Zdrojové kódy automatizovaných testů

instalace
---------

Nejdříve je trěba mít nainstalované selenium ve virtual envu a ten musí být zapnutý, viz [../instalace]

`pip install`

Vytvoř soubor s proměnnýma `variables.json`

```
{
  "username": "xxx",
  "password": "yyy"
}
```


spuštění
--------

`pytest --driver Chrome -v --variables variables.json`

`pytest --driver Chrome -v --variables variables.json --html=report/index.html`
