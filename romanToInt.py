class Solution(object):
    def romanToInt(self, s):

        number = 0
        index = 1
        last_element = s[len(s)-1]
        romanNumbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        while index < len(s):
            roman1 = s[index - 1]
            roman2 = s[index]

            if romanNumbers[roman1] < romanNumbers[roman2]:
                number += romanNumbers[roman2] - romanNumbers[roman1]
                index += 2
            else:
                number += romanNumbers[roman1]
                index += 1

        if index == len(s):
            number += romanNumbers[last_element]
        
        print(number)
        return number
    
dot = Solution()
dot.romanToInt('MCMXCIV')