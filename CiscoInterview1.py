# """
# minimum coin change problem , return list of denominations , in which you have minimum coin change
# """


# coin = 43

# _cont = [1, 2, 5, 10, 20]
# output = [20, 20, 1, 2]



# class OmniCreate:

# 	def currenty_count(self, target):


# 		def counter(lind, sum, target, output):
			
# 			if sum == target:
# 				output.append(lind)

# 			for anim in range(0, len(lind)-1):
# 				# breakpoint()
# 				if lind[anim] + lind[anim+1] < target:
# 					try:
# 						counter(_count[lind+1], sum, output.append(_count[lind]))	
# 					except:
# 						breakpoint()


# 			return output

# 		_count = [1, 2, 5, 10, 20]

# 		dp = counter(_count, 0, target, [])

# 		return dp


# 		# _count = [1, 2, 5, 10, 20]
# 		# output = []
# 		# sum = 0
# 		# counter = 0
# 		# for anim in range(len(_count)-1):
# 		# 	if _count[anim] + _count[anim+1] <= target:
# 		# 		output.append(anim)

# 		# return len(output)


# create = OmniCreate()
# print(create.currenty_count(43))





num1, num2 = "01001001", "0110101"

class OmniCreate:

	def BinDeci(self, num1):

		bin_deci = [128, 64, 32, 16, 8, 4, 2, 1]

		conv = 0

		for index, value in enumerate(num1):
			# breakpoint()
			if int(value) == 1:
				conv += bin_deci[index]

		return conv

	def DeciBina(self, num):

		# breakpoint()
		if num <= 0:
			return 1

		return num % 2 + 10 * self.DeciBina(num // 2)
		

create = OmniCreate()
addition = create.BinDeci(num1) + create.BinDeci(num2)

print(create.DeciBina(addition))

