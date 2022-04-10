from array import *


#1. Create an Array for integer type of element
animated_array = array('i', [1, 2, 3, 4, 5])

#2. Access every element in an Array (Traverse an Array)
new_array = list()
for anim in animated_array:
    new_array.append(anim)

#3. Access individual elements through indexes

acc_array_element = animated_array[2]

#4. Append any value to the array using append() method
# Using Append element can only be added at end of the array. Time complexity of append() O(1) as elements are added at end.

animated_array.append(7)

#5. Insert value using insert() method. We need to provide two values, first will be the index position and second will be the value and this is time consuming process.

animated_array.insert(1, 20)

#6. Extend python array using extend() method

banimated_array = array('i', [100, 200, 300, 400, 500, 600 , 700])

animated_array.extend(banimated_array)


#7. Add items from list into array using fromlist() method


animated_list = [11, 12, 13, 14]

animated_array.fromlist(animated_list)

#8. Remove any array element using remove() method by value and pop() by index value

animated_array.remove(7) 

animated_array.pop(7)

#9. Fetch any element in an array through its index value

animated_array.index(100)

animated_reverse_array = animated_array

animated_reverse_array.reverse()

#10. Get array buffer information through buffer_info() method

animated_array.buffer_info()

#11. Check for number of occurance of an element using count() method

animated_array.count(20)

#12. Convert array to string

animated_converted_to_string = animated_array.tobytes()
print(animated_converted_to_string)

to_check_for_convert = array('i')

to_check_for_convert.frombytes(animated_converted_to_string)

#13. Convert array elements into List

animated_converted_to_list = animated_array.tolist()

