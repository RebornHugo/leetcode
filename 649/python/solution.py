class Solution:
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        dict_buffer = {
            'D': 'R',
            'R': 'D'
        }

        list_buffer = list(senate)
        while len(set(list_buffer)) != 1:
            i = 0
            while i < len(list_buffer):
                if dict_buffer[list_buffer[i]] in list_buffer[i + 1:]:
                    list_buffer.pop(list_buffer.index(dict_buffer[list_buffer[i]], i))
                elif dict_buffer[list_buffer[i]] in list_buffer[:i]:
                    list_buffer.pop(list_buffer.index(dict_buffer[list_buffer[i]]))
                else:
                    break
                i += 1
        return 'Dire' if set(list_buffer) == {'D'} else 'Radiant'


if __name__ == '__main__':
    s = Solution()
    print(s.predictPartyVictory('RDR'))
