class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isUnique(s):
            chars = []
            for c in s:
                if c in chars:
                    return False
                else:
                    chars += c
            return True

        lengths = []
        start_pointer = 0
        end_pointer = 1
        char_counts = {}
        if len(s) in [0,1]:
            return len(s)
        while end_pointer != len(s):
            substr = s[start_pointer:end_pointer]
            if isUnique(substr):
                lengths.append(len(substr))
            else:
                start_pointer += 1
            end_pointer += 1
        substr = s[start_pointer:end_pointer]
        if isUnique(substr):
            lengths.append(len(substr))
        return max(lengths)
        
