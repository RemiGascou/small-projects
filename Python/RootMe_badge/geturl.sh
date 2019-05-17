#!/usr/bin/env bash
PSEUDO=Podalirius
curl "https://www.root-me.org/$PSEUDO?inc=score" -o out.html

echo "$(cat out.html)" | grep "<h1 itemprop=\"givenName\">" > data
#echo "$(cat out.html)" | grep "&nbsp;Points&nbsp;" > data
#echo "$(cat out.html)" | grep "<span class=\"gris\">" > data


wget "https://www.root-me.org/local/cache-vignettes/L64xH64/auton139707-7dc56.jpg" -O $PSEUDO.jpg
wget "https://www.root-me.org/local/cache-vignettes/L48xH48/rblackGrand48-0dba3.png" -O rootmeskull.png
