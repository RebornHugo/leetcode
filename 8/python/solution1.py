class Solution:
    def myAtoi(self, string):
        """
        :type string: str
        :rtype: int
        """

        def handle_after_sign(string2):
            if not string2[0].isdecimal(): return 0
            end = 1
            while end <= len(string2):
                if not string2[:end].isdecimal():
                    res = int(string2[:end - 1])
                    break
                end += 1
            else:
                res = int(string2[:end])
            return min(res, 2 ** 31)

        string = string.strip()
        if not string:
            return 0
        if string[0] in '+-':
            if len(string) > 1 and string[1].isdecimal():
                return min(int(string[0] + str(handle_after_sign(string[1:]))), 2 ** 31 - 1)
            else:
                return 0
        elif string[0].isdecimal():
            return min(handle_after_sign(string), 2 ** 31 - 1)
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("    +11191657170"))
