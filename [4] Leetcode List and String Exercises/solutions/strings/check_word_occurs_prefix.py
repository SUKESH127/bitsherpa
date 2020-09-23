class Solution:
    # QUESTION: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
    # APPROACH: very straightforward, we just need to split the sentence into words (split by whitespace), 
    # and then check, for each word, if the beginning of the word is the same as the searchWord.

    # Runtime analysis: tokenizing takes o(n) time, where n is the number of words in the sentence.
    # Then we have to check n words in the worst case. For each word, we have to check if the prefix string equals the search string
    # - which takes o(m) time where m is the length of the search word (think about why this is the case for checking string equality)
    # Thus the algorithm really takes o(mn) time, not o(n).
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        tokens = sentence.split()
        for i, word in enumerate(tokens):
            if word[0:len(searchWord)] == searchWord:
                return i+1
        return -1