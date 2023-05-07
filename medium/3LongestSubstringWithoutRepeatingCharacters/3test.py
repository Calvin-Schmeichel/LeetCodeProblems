class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CurrentSubString = []
        FinalSubString = []

        for n in range (0, len(s)):
            print(f"Round: {n}")
            print(f"Current Sub String: {CurrentSubString}")
            print(f"Letter Checking {s[n]}")
            if (s[n] in CurrentSubString) == False:
                CurrentSubString.append(s[n])
                print(f"{s[n]} was not in the substring so we add it and Continue")
                print(f"Current Sub String: {CurrentSubString}")
                
            else:
                print(f"Current Sub String: {CurrentSubString}")
                print(f"Current Final String: {FinalSubString}")
                if (len(CurrentSubString)) >= (len(FinalSubString)):
                   

                    print(f"{s[n]} was already found in the substring at index {CurrentSubString.index(s[n])}")


                    print("Current Substring was bigger then the final")
                    FinalSubString = CurrentSubString
                    CurrentSubString = CurrentSubString[(CurrentSubString.index(s[n]))+1:]
                    CurrentSubString.append(s[n])
                else:
                    print(f"{s[n]} was already found in the substring at index {CurrentSubString.index(s[n])}")
                    print("Current Substring was smaller then the final")
                    CurrentSubString = CurrentSubString[(CurrentSubString.index(s[n]))+1:]
                    CurrentSubString.append(s[n])
            
            print()
                    

        if (len(CurrentSubString)) >= (len(FinalSubString)):
                    print(CurrentSubString)
                    print(FinalSubString)
                    print("Reset")
                    FinalSubString = CurrentSubString
                    
            

        return FinalSubString




print(Solution.lengthOfLongestSubstring(Solution, "ggububgvfk"))
