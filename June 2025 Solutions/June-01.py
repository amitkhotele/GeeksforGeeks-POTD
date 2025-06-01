class Solution:
    def countPairs(self, mat1, mat2, x):
        n = len(mat1)
        count = 0
        # Flatten mat2 and store frequency in dictionary
        mat2_set = {}
        for i in range(n):
            for j in range(n):
                mat2_set[mat2[i][j]] = mat2_set.get(mat2[i][j], 0) + 1

        # Traverse mat1 and check for (x - a) in mat2_set
        for i in range(n):
            for j in range(n):
                complement = x - mat1[i][j]
                if complement in mat2_set:
                    count += mat2_set[complement]
        
        return count
