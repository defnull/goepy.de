Ergebnisse Code Golf Session
###############################################################################

:date: 2013-11-10 13:45
:author: Oliver Wannenwetsch
:category: Termine
:tags: Termin

Liebe Python-Freunde,

da wir beim letzten Code Golfing so viel Spaß hatten, veröffentliche ich hier nun die Lösungen.
Die Aufgabe bestand daraus, eine ASCII-Art Uhr zu zeichnen und eine beliebige Uhrzeit anzuzeigen.

Beispielsweise die Eingabe 21:35 wird angezeigt als:

.. image:: http://goepy.de/blog/static/static/saving_time.gif


Den Aufgabentext findet man unter `codegolf.com/saving-time <http://codegolf.com/saving-time>`_

Marcel hat das Problem in Python mit 177 Zeichen gelöst::

  h,m=map(int,input().split(':'))
  d=list(('.'*17+'\n')*11)
  l=[8,30,69,106,141,174,188,166,128,91,56,22]
  for p in range(12):d[l[p]]='ohmx'[(h%12==p)+(m//5==p)*2]
  print(''.join(d))

Ein Wert von 177 Zeichen für die Lösung in Python ist schon sehr gut:

* `Link bei Stack Exchange: ca. 175 Zeichen Python <http://codegolf.stackexchange.com/questions/3679/codegolf-com-saving-time>`_
* `Drew Stephens: 244-zeichen Python <http://dinomite.net/blog/2008/code-golf-saving-time/>`_
 
Die kürzeste Lösungen, die wir finden konnten war in Perl 100 Zeichen::

 print~($x=index'DDDDDDDDDDDD',chr)?($`%12^$x?g:p)&($'/5^$x?g:u)|H.$/x(vec'FF',$x,2):$"for<>!~/:/..92

Alle Coden Golf-Ergebnisse unserer Session gibt es als download `hier <http://goepy.de/blog/static/static/codegolf1.py>`_,

Viele Grüße und bis zur nächsten Python User-Group voraussichtlich am Donnerstag, 28.11.2013.

Oliver
