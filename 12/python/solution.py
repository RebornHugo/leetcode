class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        map_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        num_str = str(num)[::-1]
        res = ''
        for i, c in enumerate(num_str):
            cur = 10 ** i * int(c)
            if map_dict.get(cur, None):
                cur = map_dict[cur]
            else:
                if cur < 4:
                    cur = cur * map_dict[1]
                elif cur < 9:
                    cur = map_dict[5] + (cur - 5) * map_dict[1]
                elif cur < 40:
                    cur = int(c) * map_dict[10]
                elif cur < 90:
                    cur = map_dict[50] + (int(c) - 5) * map_dict[10]
                elif cur < 400:
                    cur = int(c) * map_dict[100]
                elif cur < 900:
                    cur = map_dict[500] + (int(c) - 5) * map_dict[100]
                elif cur > 1000:
                    cur = int(c) * map_dict[1000]
            res = cur + res
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(1994))
