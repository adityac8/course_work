# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:00:41 2017

@author: aditya
"""

def eucl(b,n):
    r1=n
    r2=b
    t1=0
    t2=1
    print 'q\tr1\tr2\tt1\tt2\tt'
    q="X"
    t="X"
    print "{}\t{}\t{}\t{}\t{}\t{}".format(q,r1,r2,t1,t2,t)
    while r2>0:
        q=r1/r2
        r=r1-q*r2
        r1=r2
        r2=r
        t=t1-q*t2
        t1=t2
        t2=t
        print "{}\t{}\t{}\t{}\t{}\t{}".format(q,r1,r2,t1,t2,t)
    if r1==1:
        mi=t1
    else:
        mi=0
    return mi%26
    
    
#b=int(raw_input('Enter value for b'))
#n=int(raw_input('Enter value for n'))
b=25
n=26

mi=eucl(b,n)

print "Multiplicative inverse of {} is {} under {}".format(b,mi,n)