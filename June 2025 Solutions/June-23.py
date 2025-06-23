class Solution:
    def minSum(self, arr):
        arr.sort()
        num1 = []
        num2 = []

        # Distribute digits alternately
        for i in range(len(arr)):
            if i % 2 == 0:
                num1.append(str(arr[i]))
            else:
                num2.append(str(arr[i]))

        # Convert lists to strings
        s1 = "".join(num1)
        s2 = "".join(num2)

        # Add strings manually and return result
        return self.addStrings(s1, s2).lstrip('0') or '0'

    def addStrings(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry
            result.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1

        return "".join(result[::-1])
