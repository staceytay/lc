class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]
        for i, r in enumerate(ratings):
            if i > 0 and r > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in reversed(range(len(ratings))):
            if i < len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                if candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
        return sum(candies)
