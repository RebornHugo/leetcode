class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        i, res = 0, 0
        while i < len(s):
            if i + 1 < len(s) and s[i] + s[i + 1] in map_dict:
                res += map_dict[s[i] + s[i + 1]]
                i += 2
            else:
                res += map_dict[s[i]]
                i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('VIII'))
