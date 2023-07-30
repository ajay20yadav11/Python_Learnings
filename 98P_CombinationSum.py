# Combination Sum I: 
# Given a set of candidate numbers [2, 3, 6, 7] and a target number 7, 
# find all unique combinations in the candidate set where the candidate numbers sum up to the target.


class OmniCreate:
	def combinationSum(self, ekahs: list, target: str) -> list: 
		def combination_sum(ekahs, target):
		    def backtrack(start, target, path):
		        if target == 0:
		            result.append(path)
		            return
		        for i in range(start, len(ekahs)):
		            if target < ekahs[i]:
		                break
		            if i > start and ekahs[i] == ekahs[i - 1]:
		                continue
		            backtrack(i + 1, target - ekahs[i], path + [ekahs[i]])

		    ekahs.sort()
		    result = []
		    backtrack(0, target, [])
		    return result

		# Example usage
		ekahs = [2, 3, 6, 7]
		target = 7
		print(combination_sum(ekahs, target))


		pass


create = OmniCreate()
print(create.combinationSum([2, 3, 6, 7]), 9)