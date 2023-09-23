'''
print ('Test 1 passing: ' + str(MultipleBrackets('(coder)[byte)]') == '0'))
print ('Test 2 passing: ' + str(MultipleBrackets('(c([od]er)) b(yt[e])') == '1 5'))
inp1 = '(hello [world])(!)'
'''

from dataclasses import dataclass
from typing import Dict, List, Any, Tuple


@dataclass	
class RemoveBrackets:
	'''
	To remove brackets and checks if uneven brackets present
	:param raw_data: Input Data 
	'''
	raw_data: str
	without_bracket: str = ''
	uneven_bracket: str = ''
	is_uneven: bool = False

	def __len__(self) -> int:
		return len(self.raw_data)

	def __str__(self) -> str:
		return self.without_bracket

	def __repr__(self) -> str:
		return self.uneven_bracket

	def remove_brackets(self) -> str:
		'''
		Extract non bracket characters 
		'''
		for word in self.raw_data:
			if word.isalpha() or word == ' ':
				self.without_bracket += word
			else:
				self.uneven_bracket += word

		return self.without_bracket

	def check_uneven_brackets(self) -> bool:
		'''
		To check if uneven brackets present
		'''
		bracket_digest = {')': '(', ']': '[', '}': '{'}
		stack_brackets = []
		if not self.uneven_bracket:
			self.remove_brackets()

		for bracket in self.raw_data:
			if bracket in bracket_digest.values():
				stack_brackets.append(bracket)
			elif bracket in bracket_digest.keys() and \
				(not stack_brackets or stack_brackets.pop() != bracket_digest[bracket]):
				return False

		return True


if __name__ == '__main__':
	non_brackets_hello = RemoveBrackets('(hello [world])(!)')
	non_brackets_short = RemoveBrackets('(coder)[byte)]')
	non_brackets_longer = RemoveBrackets('(c([od]er)) b(yt[e])')
	print(non_brackets_hello.check_uneven_brackets(), f'"{non_brackets_hello}"')
	print(non_brackets_short.check_uneven_brackets(), f'"{non_brackets_short}"')
	print(non_brackets_longer.check_uneven_brackets(), f'"{non_brackets_longer}"')