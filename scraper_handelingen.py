
#from datetime import datetime

#def generate_url(meet_numb, year, hand_numb): return
#"https://zoek.officielebekendmakingen.nl/h-tk-(year)-(meet_numb)-(hand_numb).xml"


#year=20132014 or 20142015
#meet_numb = voor 20132014: 40-108
#meet_numb = voor 20142015: 1-33
#hand_numb = 1-15? of hoger? 

#def run():
#	output = open('', 'a')
#	for meet_numb, year, hand_numb in 
#	print 
#	url= generate_url(meet_numb, year, hand_numb)
#

#import urllib
#urllib.urlretrieve ("https://zoek.officielebekendmakingen.nl/h-tk-20142015-33-13.xml", "h-tk-20142015-33-13.xml")

#for meet_numb in range(40,109):  #to iterate between 10 to 20
 #  for i in range(1,6): #to iterate on the factors of the number
  #     print 'h-tk-20132014-%d-%d' % (meet_numb,i)

#output= open('h-tk-20142015-33-13.xml', 'wb')

#import urllib2
#response = urllib2.urlopen("https://zoek.officielebekendmakingen.nl/h-tk-20142015-33-13.xml", "h-tk-20142015-33-13.xml")
#html = response.read()

for meet_numb in range(40,109):  #to iterate between 10 to 20
	for i in range(1,6): #to iterate on the factors of the number
   		print 'h-tk-20132014-%d-%d' % (meet_numb,i)
		import urllib
		urllib.urlretrieve ("https://zoek.officielebekendmakingen.nl/" +'h-tk-20132014-%d-%d' % (meet_numb,i), 'h-tk-20132014-%d-%d' % (meet_numb,i)+".xml")

