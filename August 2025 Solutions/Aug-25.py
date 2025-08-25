import bisect

class Solution:
    def maximizeMedian(self, arr, k):
        arr.sort()
        n = len(arr)

        # Odd n: classic "raise the middle via suffix leveling" with binary search
        if n % 2 == 1:
            m = n // 2
            low, high, ans = arr[m], arr[m] + k, arr[m]
            while low <= high:
                mid = (low + high) // 2
                cost = 0
                for i in range(m, n):
                    if arr[i] < mid:
                        cost += (mid - arr[i])
                        if cost > k:
                            break
                if cost <= k:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        # Even n: maximize floor((b[p-1] + b[p]) / 2)
        p = n // 2
        m1, m2 = p - 1, p

        right = arr[m2:]                # p elements
        pref = [0]
        s = 0
        for v in right:
            s += v
            pref.append(s)

        def cost_raise_right(U: int) -> int:
            """Cost to make all right-half elements >= U."""
            idx = bisect.bisect_left(right, U)  # elements < U
            return idx * U - pref[idx]

        def feasible(M: int) -> bool:
            S = 2 * M
            u0 = (S + 1) // 2                 # ceil(S/2)
            minRight = right[0]

            candidates = {
                u0,
                max(u0, S - arr[m1]),
                max(u0, minRight),
                max(u0, minRight + 1)
            }

            for U in candidates:
                # Left-mid requirement (p+1 elements >= S-U): raise arr[m1] to S-U
                left_need = S - U
                cost = 0
                if left_need > arr[m1]:
                    cost += left_need - arr[m1]
                # Right-half requirement: all p right elements >= U
                cost += cost_raise_right(U)
                if cost <= k:
                    return True
            return False

        low = (arr[m1] + arr[m2]) // 2
        high = arr[m2] + k  # average can’t exceed the (raised) right middle
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if feasible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
