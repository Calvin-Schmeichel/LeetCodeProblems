class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CurrentSubString = []
        FinalSubString = []

        for n in range (0, len(s)):
            if (s[n] in CurrentSubString) == False:
                CurrentSubString.append(s[n])
            elif (len(CurrentSubString)) >= (len(FinalSubString)):
                FinalSubString = CurrentSubString
                CurrentSubString = CurrentSubString[(CurrentSubString.index(s[n]))+1:]
                CurrentSubString.append(s[n])
            else:
                CurrentSubString = CurrentSubString[(CurrentSubString.index(s[n]))+1:]
                CurrentSubString.append(s[n])
            
        if (len(CurrentSubString)) >= (len(FinalSubString)):
                    FinalSubString = CurrentSubString
                    
        return len(FinalSubString)


print(Solution.lengthOfLongestSubstring(Solution, "pwwkew"))
