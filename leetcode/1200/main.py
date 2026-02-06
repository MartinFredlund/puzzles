class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sortarr = sorted(arr)
        result = []
        min_diff = float("inf")
        for i in range(len(sortarr) - 1):
            diff = sortarr[i + 1] - sortarr[i]

            if diff < min_diff:
                min_diff = diff
                result.clear()
                result.append([sortarr[i], sortarr[i + 1]])
            elif diff == min_diff:
                result.append([sortarr[i], sortarr[i + 1]])
        return result
