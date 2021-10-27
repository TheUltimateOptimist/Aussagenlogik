# Aussagenlogik
Erstellen und Berechnen von logischen Aussagen
Erstellen von Wahrheitstabellen

# Installation
Lade die Datei Aussagenlogik.exe herunter und installier sie.
Wenn du sie öffnest gelangst du in ein Terminal, in dem du deine Berechnungen anstellen kannst

# Funktionsweise
1. einer Aussage können die folgenden Werte zugeordnet werden:
   1, w, true oder 0, f, false

2. standardmäßig werden die Aussagenwerte als 0 und 1(binär) repräsentiert

3. die oben erwähnte Repräsentation von Aussagewerten kann geändert werden:
   a) zu w    und f     -> durch Eingabe von: >: wf
   b) zu true und false -> durch Eingabe von: >: truefalse

4. ein Aussagenwert kann als Variable abgespeichert werden:
   Eingabe: >: deinVariablenName = Wahrheitswert
   Achtung! die folgenden Variablennamen sind unzulässig:
   1, w, true, 0, f, false, nicht, und, oder, xor, folgt, (, )
   Achtung! der Variablenname darf keine Leerzeichen enthalten
   unter 1. steht welche Wahrheitswerte möglich sind

5. angelegte Variablen können mit Junktoren und Klammern zu neuen Aussagen zusammengefügt werden:
   zulässige Klammern : (, )
   zulässige Junktoren: nicht, und, oder, xor, folgt
   Wenn das Ergebnis davon nicht einer Variable zugeornet wird, wird es in der Konsole ausgegeben

6. es ist möglich Wahrheitstabellen zu erstellen:
   Eingabe: >: tafel

7. Beispiele:
   a) Änderung der Darstellung der Aussagenwerte zu w und f:
      >: wf
   b) Änderung der Darstellung der Aussagenwerte zu 1 und 0:
      >: binär
   c) Änderung der Darstellung der Aussagenwerte zu true und false:
      >: truefalse
   d) Erstellung der Aussage a mit dem Wahrheitswert w
      >: a = w
   e) Erstellung der Aussage alleSchlafen mit dem Wahrheitswert 0:
      >: alleSchlafen = 0
   f) Erstellung der Aussage b mit dem Wahrheitswert alleSchlafen und a
      >: b = alleSchlafen und a
   g) Ausgabe des Wahrheitswertes der Aussage a:
      >: a
   h) Ausgabe des Wahrheitswertes der Aussage alleSchlafen und nicht a
      >: alleSchlafen und nicht(a)
   i) Erstellen einer Wahrheitswertetabelle mit drei Variablen und zusätzlich den Ausdrücken nicht(A), A und B, A oder B
      >: tafel
      >Gib die Anzahl der vorkommenden Variablen ein: 3
      >1. Ausdruck: nicht(A)
      >2. Ausdruck: A und B
      >3. Ausdruck: A oder B
      >4. Ausdruck: s

# Befehle
