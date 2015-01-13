# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 12:12:24 2015


from xml.dom import minidom

xmldoc = minidom.parse("scraping/data/h-tk-20132014-40-1.xml")


op = xmldoc.getElementsByTagName("oficiele-publicatie")[0]

handelingen = op.getElementsByTagName("handelingen")[0]

opening = handelingen.getElementsByTagName("opening")[0]

tekst= opening.getElementsByTagName("tekst")[0]

ag= tekst.getElementsByTagName("al-groep")[2]

al=ag.getElementsByTagName("al")[0].firstChild.data

print al 
"""


from xml.dom import minidom

xmldoc = minidom.parse("scraping/data/h-tk-20132014-40-1.xml")

al =xmldoc.getElementsByTagName("al")
print al

for el in al:
    print el.firstChild.data

print 'hello'