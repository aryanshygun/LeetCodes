class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0

        while i < len(prices):
            price = prices[i]

            j = i + 1

            while j < len(prices):
                if prices[j] <= price:
                    price -= prices[j]

                    break

                j += 1
            prices[i] = price
            i += 1
        return prices
