import random
import sys
import os

# looping 

for x in range(0,10):
	print(x, '', end='')

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
