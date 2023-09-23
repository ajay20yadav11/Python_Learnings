"""
# Input:str is "(hello [world])(!)
# Output:1 3
# Have the function  MultipleBrackets(str) take the str 
# parameter being passed and return 1 #ofBrackets if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is 
# "(hello [world])(!)", then the output should be 1 3 because all the brackets are matched and there are 3 pairs of brackets,
#  but if str is "((hello [world])" the the output should be 0 because the brackets do not correctly match up. Only "(", ")", "[", and "]" will be used as brackets. If str contains no brackets return 1.
 
 
#  # keep this function call here
# print ('Test 1 passing: ' + str(MultipleBrackets("(coder)[byte)]") == '0'))
# print ('Test 2 passing: ' + str(MultipleBrackets("(c([od]er)) b(yt[e])") == '1 5'))
"""


inp1 = "(hello [world])(!)"
# output = 1, 3

_data = ['(', ')', '[', ']']

# dummpy = {}

# for anim in inp1:
# 	if anim in _data:
# 		print(anim)
# 		dummpy.append(anim)

# print(dummpy)

def MultipleBrackets(inp1: str) -> int:


	dummp = {}

	# for anim in inp1:
	# 	if anim in _data:
	# 		dummp.append(anim)

	# if len(dummp) % 2 == 0:
	# 	return 1
	# else:
	# 	return 0

	_data = {'(':')', '[':']'}

	for anim in inp1:
		if _data[anim] == anim:
			print(anim)

	for anim in inp1:
		if _data.get(anim, 0):
			if not (_data.get(anim, 0)) in dummp:
				dummp[((_data.get(anim, 0)))] = 0
			else:
				dummp[((_data.get(anim, 0)))] += 1


	print(dummp)



print(MultipleBrackets("(hello [world])(!)"))
# print(MultipleBrackets("(c([od]er)) b(yt[e])"))
# print(MultipleBrackets("(coder)[byte)]"))
# print(MultipleBrackets("[)]("))