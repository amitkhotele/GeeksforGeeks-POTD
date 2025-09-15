class Solution:
    def stringStack(self, pat, tar):
        i = len(pat) - 1
        j = len(tar) - 1
        skip = 0

        while i >= 0:
            if skip > 0:
                # this character will be consumed by a delete to the right
                skip -= 1
            elif j >= 0 and pat[i] == tar[j]:
                # use this push to match tar[j]
                j -= 1
            else:
                # mark this position as a delete operation (it will remove one push to the left)
                skip += 1
            i -= 1

        return j < 0
