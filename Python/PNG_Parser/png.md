# Format de fichier PNG

Le format PNG (Portable Network Graphics, ou format Ping) est un format de fichier graphique bitmap (raster). Il a été mis au point en 1995 afin de fournir une alternative libre au format GIF, format propriétaire dont les droits sont détenus par la société Unisys (propriétaire de l'algorithme de compression LZW), ce qui oblige chaque éditeur de logiciel manipulant ce type de format à leur verser des royalties. Ainsi PNG est également un acronyme récursif pour PNG's Not Gif.

## Caractéristiques

Le format PNG permet de stocker des images en noir et blanc (jusqu'à 16 bits par pixels de profondeur de codage), en couleurs réelles (True color, jusqu'à 48 bits par pixels de profondeur de codage) ainsi que des images indexées, faisant usage d'une palette de 256 couleurs.

De plus, il supporte la transparence par couche alpha, c'est-à-dire la possibilité de définir 256 niveaux de transparence, tandis que le format GIF ne permet de définir qu'une seule couleur de la palette comme transparente. Il possède également une fonction d'entrelacement permettant d'afficher l'image progressivement.

La compression proposé par ce format est une compression sans perte (lossless compression) 5 à 25% meilleure que la compression GIF.

Enfin PNG embarque des informations sur le gamma de l'image, ce qui rend possible une correction gamma et permet une indépendance vis-à-vis des périphériques d'affichage. Des mécanismes de correction d'erreurs sont également embarquées dans le fichier afin de garantir son intégrité.
Structure d'un fichier PNG

Un fichier PNG est constité d'une signature, permettant de signaler qu'il s'agit d'un fichier PNG, puis d'une série d'éléments appelés chunks (le terme "segments" sera utilisé par la suite). La signature d'un fichier PNG (en notation décimale) est la suivante :

```
137 80 78 71 13 10 26 10
```

La même signature en notation hexadécimale est :

```
89 50 4E 47 0D 0A 1A 0A
```

Chaque segment (chunk) est composé de 4 parties :

 - La taille, un entier non signé de 4 octets, décrivant la taille du segment
 - Le type de segment (chunk type) : un code de 4 caractères (4 octets) composés de caractères ASCII alphanumériques (A-Z, a-z, 65 à 90 et 97 à 122) permettant de qualifier la nature du segment
 - Les données du segment (chunk data)
 - Le CRC (cyclic redundancy check), un code correcteur de 4 octets permettant de vérifier l'intégrité du segment


Les segments peuvent être présents dans n'importe quel ordre si ce n'est qu'ils doivent commencer par le segment d'en-tête (IHDR chunk) et finir par le segment de fin (IEND chunk)


Les principaux segments (appelés *critical chunks*) sont :

 - IHDR Image header
 - PLTE Palette
 - IDAT Image data
 - IEND Image trailer


Les autres segments (appelés *anciliary chunks*) sont les suivants :

 - bKGD Background color
 - cHRM Primary chromaticities and white point
 - gAMA Image gamma
 - hIST Image histogram
 - pHYs Physical pixel dimensions
 - sBIT Significant bits
 - tEXt Textual data
 - tIME Image last-modification time
 - tRNS Transparency
 - zTXt Compressed textual data
