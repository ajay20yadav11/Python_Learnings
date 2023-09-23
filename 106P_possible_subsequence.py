"""
Given an integet array nums, generate all the subsets (subsequences).

e.g. big_data = [1, 2, 3], if size = n, then no. f subsets = 2^n

output = [[], [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3]]

"""

# Taking Recursion/Backtracking approach

from dataclasses import dataclass
from typing import List


@dataclass
class SubSequences:
	big_data: List
	possible_subseq = []

	def __str__(self):
		return f'Subsequences are {self.possible_subseq}'

	def sub_sequences(self) -> List:
		def backtrack(index, array, path):
			if index >= len(self.big_data):
				if path not in self.possible_subseq:
					self.possible_subseq.append(path)

			for current_index in range(index, len(array)):
				if [self.big_data[current_index]] not in self.possible_subseq:
					self.possible_subseq.append([self.big_data[current_index]])
				backtrack(current_index+1, self.big_data, path+[self.big_data[current_index]])
				# backtrack(current_index+1, self.big_data, [self.big_data[current_index]])

		backtrack(0, self.big_data, [])

		return self.possible_subseq

	def backtracking_method_sub_sequences(self) -> List[List[int]]:
		def backtrack(index, path):
			self.possible_subseq.append(path[:])

			for current_index in range(index, len(self.big_data)):
				path.append(self.big_data[current_index])
				backtrack(current_index+1, path)
				path.pop()


		backtrack(0, [])
		return self.possible_subseq


if __name__ == '__main__':
	create_subsequence = SubSequences([1, 2, 3])
	print(create_subsequence.backtracking_method_sub_sequences())

