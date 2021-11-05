# Aussagenlogik
Erstellen und Berechnen von logischen Aussagen
Erstellen von Wahrheitstabellen

# Installation
Lade die Datei Aussagenlogik.exe herunter und installiere sie.
Wenn du sie öffnest gelangst du in ein Terminal, in dem du deine Berechnungen anstellen kannst

# Funktionsweise
1. einer Aussage können die folgenden Werte zugeordnet werden:
   1, w, true oder 0, f, false

2. standardmäßig werden die Aussagenwerte als 0 und 1(binär) repräsentiert

3. die oben erwähnte Repräsentation von Aussagewerten kann geändert werden:
   1. zu w    und f     -> durch Eingabe von: 
      >: wf
   2. zu true und false -> durch Eingabe von: 
      >: truefalse

5. ein Aussagenwert kann als Variable abgespeichert werden:
   Eingabe: >: deinVariablenName = Wahrheitswert
   Achtung! die folgenden Variablennamen sind unzulässig:
   1, w, true, 0, f, false, nicht, und, oder, xor, folgt, (, )
   Achtung! der Variablenname darf keine Leerzeichen enthalten
   unter 1. steht welche Wahrheitswerte möglich sind

6. angelegte Variablen können mit Junktoren und Klammern zu neuen Aussagen zusammengefügt werden:
   zulässige Klammern : (, )
   zulässige Junktoren: nicht, und, oder, xor, folgt
   Wenn das Ergebnis davon nicht einer Variable zugeornet wird, wird es in der Konsole ausgegeben

7. es ist möglich Wahrheitstabellen zu erstellen:
   Eingabe: >: tafel

8. Beispiele:
   1. Änderung der Darstellung der Aussagenwerte zu w und f: 
      >>: wf
   2. Änderung der Darstellung der Aussagenwerte zu 1 und 0: 
      >: binär
   3. Änderung der Darstellung der Aussagenwerte zu true und false: 
      >: truefalse
   4. Erstellung der Aussage a mit dem Wahrheitswert w: 
      >: a = w
   5. Erstellung der Aussage alleSchlafen mit dem Wahrheitswert 0:
      >: alleSchlafen = 0
   6. Erstellung der Aussage b mit dem Wahrheitswert alleSchlafen und a
      >: b = alleSchlafen und a
   7. Ausgabe des Wahrheitswertes der Aussage a:
      >: a
   8. Ausgabe des Wahrheitswertes der Aussage alleSchlafen und nicht a
      >: alleSchlafen und nicht(a)
   9. Erstellen einer Wahrheitswertetabelle mit drei Variablen und zusätzlich den Ausdrücken nicht(A), A und B, A oder B
      >: tafel
      > 
      > Gib die Anzahl der vorkommenden Variablen ein: 3
      >
      > 1.Ausdruck: nicht(A)
      >
      > 2.Ausdruck: A und B
      >
      > 3.Ausdruck: A oder B
      >
      > 4.Ausdruck: s
   

# Befehle
>: befehle    |--> gibt alle definierten Befehle aus
>: erkläre    |--> gibt eine erklärung der Funktionsweise dieses Tools aus

>: binär      |--> ändert die Darstellung von Aussagewerten zu 0 und 1
>: wf         |--> ändert die Darstellung von Aussagewerten zu w und f
>: truefalse  |--> ändert die Darstellung von Aussagewerten zu true und false

>: [Aussagenname] = [Aussagenwert]
  -> speichert den Wert einer bestimmten Aussage
  -> über den Aussagennamen kann der Wert in weiteren Befehlen benutzt werden
  -> [Aussagenname] muss durch einen beliebigen Namen ersetzt werden
  -> [Aussagenwert] muss durch 1, w, true, 0, f, false oder einen Aussagenausdruck der sich zu einem der Werte auflösen lässt ersetzt werden 

# Junktoren
>: ... und ...
>: ... oder ...
>: ... xor ...
>: ... folgt ...
  -> verbinden zwei Aussagen zu einer neuen Aussage
>: nicht ...
  -> negiert eine Aussage

>: tafel    |--> lässt dich eine Wahrheitstafel erstellen
