import numpy as np
from array import *


numb_of_days = int(input("How many days temperature: "))

temp_array = array("i", [])

for anim in range(0, numb_of_days):
    iter_value = int(input(f"Day {anim+1}'s high temperature: "))
    temp_array.append(iter_value)

# count = 0
# while True:

#     count = count + 1
#     iter_value = int(input(f"Day {count}'s high temperature: "))
#     mark_temp.append(iter_value)
#     numb_of_days = numb_of_days - 1
#     if numb_of_days == 0: break


temp_temp_list = temp_array.tolist()

print(f"Raw data of {numb_of_days} of temperature are {temp_temp_list}")

avg_temp = sum(temp_temp_list) / len(temp_temp_list)

print(f"Average temperature for {numb_of_days} days is {avg_temp}")

temp_greater_avg = list()

for anim in temp_temp_list:
    if anim > avg_temp:
        temp_greater_avg.append(anim)


print(
    f"Total number of days that has Temperature higher than average are {len(temp_greater_avg)} with values as {temp_greater_avg}"
)
