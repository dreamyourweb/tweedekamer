
#scraping tweede kamer handelingen. 
#meldingen dat bestanden niet bestaan eruit filteren op de een of andere manier.
jaartallen variabelen van maken
#year=20132014 or 20142015
#meet_numb = voor 20132014: 40-108
#meet_numb = voor 20142015: 1-33
#i = 1-40? of hoger? 


import urllib2

#onderstaande draait nu:
for meet_numb in range(40,109):  
	for i in range(1,40): 
  		print 'h-tk-20132014-%d-%d' % (meet_numb,i)
		resp = urllib2.urlopen ("https://zoek.officielebekendmakingen.nl/" +'h-tk-20132014-%d-%d.xml' % (meet_numb,i), 'h-tk-20132014-%d-%d' % (meet_numb,i)+".xml")
		print resp.headers["content-type"]


for meet_numb in range(1,33):  
	for i in range(1,40): 
   		print 'h-tk-20142015-%d-%d' % (meet_numb,i)
		import urllib
		urllib.urlretrieve ("https://zoek.officielebekendmakingen.nl/" +'h-tk-20142015-%d-%d' % (meet_numb,i), 'h-tk-20142015-%d-%d' % (meet_numb,i)+".xml")



