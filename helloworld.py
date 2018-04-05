import random
import sys
import os

# for looping 

for x in range(0,10):
	print(x)

print('\n')

grocerry_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocerry_list:
	print(y)

for x in [2,4,6,8,10]:
	print (x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
	for y in range(0,3):
		print(num_list[x][y])



# While Loop : When we do not know about the range

random_num = random.randrange(0,100)

while(random_num != 15):
	print(random_num)
	random_num = random.randrange(0,100)

i=0;

while(i <= 20 ):
	if(i%2 ==0):
		print(i)
	elif(i==9):
		break
	else:
		i +=1
		continue #this will start the loop frm the begenenning

	i += 1