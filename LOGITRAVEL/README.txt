En desarrollar el código he tardado 120 minutos. Entre búsqueda de la fuente mas factible y en el diseño e implementación del código.

Script Basado en accuweather, obteniendo desde su pagina web una plantilla XML, la cual es parseada en un array y luego obtenemos los valores necesarios.

Ejemplo de uso:
"python weathercli.py PROVINCIA"

Se encuentra soportado mezclar mayusculas y minusculas en el nombre de la provincia.

Por exemplo 

python weathercli.py madrid
python weathercli.py Barcelona
python weathercli.py PALMA


Resultados:

Walii:LOGYTRAVEL walterleonardo$ python weathercli.py madrid
SITE: Madrid, ES 
TODAY CONDITIONS:  Sunny
TODAY TEMPERATURE:  33C
TOMORROW FORECAST: High: 38 C Low: 21 C Hot with sunshine 


Walii:LOGYTRAVEL walterleonardo$ python weathercli.py Barcelona
SITE: Barcelona, ES 
TODAY CONDITIONS:  Sunny
TODAY TEMPERATURE:  30C
TOMORROW FORECAST: High: 30 C Low: 23 C Partly sunny and pleasant 


Walii:LOGYTRAVEL walterleonardo$ python weathercli.py PALMA
SITE: Palma, ES 
TODAY CONDITIONS:  Sunny
TODAY TEMPERATURE:  32C
TOMORROW FORECAST: High: 34 C Low: 19 C Mostly sunny 




