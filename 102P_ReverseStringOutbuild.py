

animated = [1, 2, 3, 4, 5]

left, right = 0, len(animated)-1


while left <= right:
	animated[left], animated[right] = animated[right], animated[left]
	left += 1
	right -= 1

print(animated)