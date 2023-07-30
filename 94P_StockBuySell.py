class OmniCreate:
	"""
	Sure, here's a question on the "Best Time to Buy and Sell Stock" problem:

	Problem:
	You are given an array prices where prices[i] is the price of a given stock on the i-th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Write a function maxProfit(prices) that returns the maximum profit you can achieve.

	Note: You cannot sell a stock before you buy one.

	Example:
	Input: prices = [7, 1, 5, 3, 6, 4]
	Output: 5
	"""
	def BuySell(self, ekahs):
		maxProfit = 0

		minBuy = min(ekahs)
		minIndex = ekahs.index(minBuy)
		print(len(ekahs), minIndex)
		if minIndex < len(ekahs) - 1:
			maxSell = max(ekahs[minIndex+1:])
			maxProfit = maxSell - minBuy

		return maxProfit
  	
	def maxProfit(self, prices):
	    minPrice = float('inf')
	    maxProfit = 0
	    
	    for price in prices:
	        potentialProfit = price - minPrice
	        maxProfit = max(maxProfit, potentialProfit)
	        minPrice = min(minPrice, price)
	    
	    return maxProfit


if __name__ == "__main__":
    create = OmniCreate()
    print(create.maxProfit([7, 6, 4, 3, 1]))
