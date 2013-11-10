Python Code Golf - Lösungen

Python User Group, Göttingen 31.10.2013

http://www.goepy.de

== Aufgabe  - Code Golf Challenge  - Saving Time ==

http://codegolf.com/saving-time

== Erste Lösung: 630 Zeichen ==

from math import *
import sys
r=round
f=range
[h,m]=map(int,sys.argv[1].split(':'))
m=r(m/5-0.499)
h=h%12
xs,ys=10,17
pos=[]
def xy(z):
  return (r(xs-xs/(2+0.1*cos(z/6*pi))*(1+cos((z/6*pi)))),r(ys/2*(1+sin((z/6*pi)))))
for a in f (0,12):
  pos.append(xy(a))
o=''
for i in f(0,xs+1):
    o+='\n'
    for j in f(0,ys+1):
        c=0
        if ((i,j) in pos):
            if ((i,j)==xy(h)):
                o+='h'
            elif ((i,j)==xy(m)):
                o+='m'
            else:
                o+='o'
            c+=1
            if(c==2 or i==0 or i==xs):
                break
        else:
            o+=' '
print(o)

== Zweite Lösung: 510 Zeichen ==

import sys
r=lambda s,h,n:s.replace(h,n)
t=sys.stdin.readline().split(':')
h,m=int(t[0])%12,int(t[1])/5
d=' '*13
a,b,c,x,n=d[:8],d[:4],d[:7],str,'\n\n'
if m==10:
    m="a"
if m==11:
    m="b"
if h==10:
    h="a"
if h==11:
    h="b"
s = a+"0\n"+b+"b"+c+"1"+n+" a"+d+"2"+n+"9"+a+c+"3"+n+" 8"+d+"4"+n+b+"7"+c+"5\n"+a+"6"
m,h=x(m),x(h)
for i in '0123456789ab':
    i=x(i)
    if i==m and i == h:
        s=r(s,i,"x")
    if i==h:
        s=r(s,i,"h")
    if i==m:
        s=r(s,i,"m")
    s=r(s,x(i), "o")
print s

== Dritte Lösung und somit der Gewinner: 177 Zeichen ==

h,m=map(int,input().split(':'))
d=list(('.'*17+'\n')*11)
l=[8,30,69,106,141,174,188,166,128,91,56,22]
for p in range(12):d[l[p]]='ohmx'[(h%12==p)+(m//5==p)*2]
print(''.join(d))

 
