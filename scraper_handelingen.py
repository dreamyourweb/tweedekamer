
"""scraping tweede kamer handelingen. 
Hoe meldingen dat bestanden niet bestaan ("De pagina die u zocht kon niet worden gevonden")
eruit filteren?
meet_numb = voor 20132014: 40-108
meet_numb = voor 20142015: 1-33
i = 1-40? of hoger? 
20132014-variabele maken 
"""


import urllib2


for meet_numb in range(40,109):  
	for i in range(1,40): 
  		print 'h-tk-20132014-%d-%d' % (meet_numb,i)
		response = urllib2.urlopen ("https://zoek.officielebekendmakingen.nl/" +'h-tk-20132014-%d-%d.xml' % (meet_numb,i), 'h-tk-20132014-%d-%d' % (meet_numb,i)+".xml")
		output = open('h-tk-20132014-%d-%d' % (meet_numb,i)+".xml", 'wb')
		output.write(response.read())
		output.close()

for meet_numb in range(1,33):  
	for i in range(1,40): 
  		print 'h-tk-20142015-%d-%d' % (meet_numb,i)
		response = urllib2.urlopen ("https://zoek.officielebekendmakingen.nl/" +'h-tk-20142015-%d-%d' % (meet_numb,i), 'h-tk-20142015-%d-%d' % (meet_numb,i)+".xml")
		output = open('h-tk-20132014-%d-%d' % (meet_numb,i)+".xml", 'wb')
		output.write(response.read())
		output.close()

