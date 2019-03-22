from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []

        def is_palindromer(word):
            return word == word[::-1]

        words = {word: i for i, word in enumerate(words)}
        for word, i in words.items():
            for j in range(len(word) + 1):
                pref = word[:j]
                suff = word[j:]
                if is_palindromer(pref):
                    temp = suff[::-1]
                    if temp != word and temp in words:
                        res.append([words[temp], i])
                if j != len(word) and is_palindromer(suff):
                    temp = pref[::-1]
                    if temp != word and temp in words:
                        res.append([i, words[temp]])
        return res

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # TLE
        def is_palindromer(word):
            return word == word[::-1]

        res = []
        words = {word: i for i, word in enumerate(words)}

        def dfs(cur: List[str]):
            if len(cur) == 2:
                temp = ''.join(cur)
                if is_palindromer(temp):
                    res.append([words[cur[0]], words[cur[1]]])
            else:
                for word in words.keys():
                    if word not in cur:
                        cur.append(word)
                        dfs(cur)
                        cur.pop()

        dfs([])
        return res
