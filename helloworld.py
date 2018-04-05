import random
import sys
import os

#Dictiontionaries and maps
''' cannot join Disctionaries like we can join a list. '''

hp_chars = {'Harry':'Potter',
				'Ron':'Wisely',
				'Hermoine':'Granger',
				'Albus':'Dumbledore'}

print(hp_chars['Harry'])
del hp_chars['Albus']
hp_chars['Albus'] = 'Percivic'

print (len(hp_chars))

print (hp_chars.get("Harry"))

print(hp_chars.keys())

print(hp_chars.values())
	


