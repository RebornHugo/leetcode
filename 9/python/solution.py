class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        x = str(x)
        i, j = 0, len(x) - 1
        while i != j and i + 1 != j:
            if x[i] == x[j]:
                i += 1
                j -= 1
            else:
                return False
        else:
            return i == j or x[i] == x[j]

    # def isPalindrome(self, x):
    #     # online solution
    #     return str(x)[::-1] == str(x)


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(-10201))
