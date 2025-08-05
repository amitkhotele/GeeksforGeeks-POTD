import re

class Solution:
    def isPalinSent(self, s):
        # Step 1: Convert to lowercase
        s = s.lower()
        
        # Step 2: Remove all non-alphanumeric characters using regex
        cleaned = re.sub(r'[^a-z0-9]', '', s)
        
        # Step 3: Check if cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]
