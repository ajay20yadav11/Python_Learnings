vowel = ['a','e','i','o','u']
output = ['']

N = int(input('Enter N: '))

while N > 0:
	output = [anim+bnim for anim in vowel for bnim in output]
	N -= 1

print(output)

# print(code(vowel, output))