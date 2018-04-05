import random
import sys
import os

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print(grocery_list)
print ('First Item', grocery_list[0])
grocery_list[0] = "Butter"
print('First Item')
# print a range of grocery list
print(grocery_list[1:3])

other_events = ["wash_car", 'pick up kids', 'cash_check']
#create a list and add above two list inside another list
to_do_list = [other_events,grocery_list]

print((to_do_list[1][1]))

print(to_do_list)

grocery_list.insert(1, "pickle")
grocery_list.remove("pickle")
grocery_list.sort()
grocery_list.reverse()

del grocery_list[3] #delete the 5th element
print(to_do_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

