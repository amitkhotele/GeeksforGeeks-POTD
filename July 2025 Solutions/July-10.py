class Solution:
    def longestString(self, words):
        words.sort()  # Sort to handle lexicographical order
        valid = set()
        result = ""
        
        for word in words:
            if len(word) == 1 or word[:-1] in valid:
                valid.add(word)
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        
        return result
