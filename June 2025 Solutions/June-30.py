class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        def isPossible(mid):
            water_used = 0
            water_effect = [0] * (n + 1)
            curr_water = 0

            for i in range(n):
                curr_water += water_effect[i]
                actual_height = arr[i] + curr_water

                if actual_height < mid:
                    diff = mid - actual_height
                    water_used += diff
                    if water_used > k:
                        return False
                    curr_water += diff
                    if i + w < len(water_effect):
                        water_effect[i + w] -= diff

            return True

        low = min(arr)
        high = low + k
        answer = low

        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer
