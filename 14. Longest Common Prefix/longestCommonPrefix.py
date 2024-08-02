class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Initialize the longest common prefix (lcp) to the first string in the list.
        lcp = strs[0]
        
        # Iterate over all strings in the list.
        for word in strs:
            # If the current word is the same as the current lcp, skip to the next word.
            if word == lcp:
                continue
            
            # Determine the lengths of the current word and the current lcp.
            len_word = len(word)
            len_lcp = len(lcp)
            
            # Compare lengths and initialize a new variable to build the new lcp.
            if len_word < len_lcp:
                # If the word is shorter than the current lcp, check up to the length of the word.
                new_lcp = ""
                for i in range(len_word):
                    if word[i] == lcp[i]:
                        new_lcp += word[i]
                    else:
                        break
                lcp = new_lcp
            else:
                # If the word is not shorter, or is the same length, check up to the length of the current lcp.
                new_lcp = ""
                for i in range(len_lcp):
                    if word[i] == lcp[i]:
                        new_lcp += word[i]
                    else:
                        break
                lcp = new_lcp

        # Return the longest common prefix after examining all words.
        return lcp
