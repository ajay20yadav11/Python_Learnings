# Combination Sum I: 
# Given a set of candidate numbers [2, 3, 6, 7] and a target number 7, 
# find combinations in the candidate set where the candidate numbers sum up to the target.

from dataclasses import dataclass
from typing import List
from pprint import pprint


@dataclass
class CombinationSum:
	candidates: List
	target: int
	possible_solution = 0

	def __str__(self):
		return f'Maximum number of candidates are {self.possible_solution}'

	def brute_force_sum_to_target(self) -> int:

		for i in range(len(self.candidates)):
			counter = 1
			for j in range(i, len(self.candidates)):
				if self.candidates[i] + self.candidates[j] == self.target:
					counter += 1

			if self.possible_solution < counter:
				self.possible_solution = counter

		return self.possible_solution

	def dp_sum_to_target(self) -> List:

		self.candidates.sort()
		print(self.candidates)
		dp = [0] * len(self.candidates)
		dp[0] = 1

		left_bar = self.candidates[0]

		for candidate in range(1, len(self.candidates)):
			if self.candidates[candidate] + left_bar <= self.target:
				dp[candidate] = max(dp[candidate-1], dp[candidate]+1)

		print(dp)
		self.possible_solution = dp[-1]
		return self.possible_solution

	def backtracking_method_sum_to_target_unique(self) -> int:

		def backtrack(index, target, path):
			if target == 0:
				result.append(path[:])
				return

			for current_index in range(index, len(self.candidates)):
				backtrack(current_index+1, target - self.candidates[current_index], path + [self.candidates[current_index]])

		result = []
		backtrack(0, self.target, [])
		if not result:
			return []
		print(result)
		self.possible_solution = len(result[0])
		return result[0]

	def backtracking_method_sum_to_target_duplicate(self) -> int:

		def backtrack(index, target, path):

			if index == len(self.candidates):
				if target == 0:
					result.append(path[:])
				return

			# For creating duplicate or possible subsets for candidate less than target
			if self.candidates[index] <= target:
				path.append(self.candidates[index])
				backtrack(index, target - self.candidates[index], path)
				path.pop()

			# Looking for target 
			backtrack(index + 1, target, path)


		result = []
		backtrack(0, self.target, [])
		if not result:
			return []
		print(result)
		result_set = {tuple(value) for value in result}
		to_find_min = {k: len(k) for k in result_set}
		min_a = min(to_find_min, key=to_find_min.get)
		return min_a
		# return [anim for anim in result if len(anim) == 4]
 

if __name__ == '__main__':
	maximum_sum = CombinationSum([1, 2, 5, 10, 20], 43)
	# maximum_sum = CombinationSum([2, 3, 5, 5], 10)
	# maximum_sum = CombinationSum([1, 3, 2, 2], 4)
	# maximum_sum.brute_force_sum_to_target()
	# print(maximum_sum.backtracking_method_sum_to_target_duplicate())
	# print(maximum_sum.backtracking_method_sum_to_target_unique())
	# print(maximum_sum.dp_sum_to_target())
	print(maximum_sum.brute_force_sum_to_target())
	# print(maximum_sum)

