class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)-97] +=1
            freq = str(freq)
            if freq in anagrams:
                anagrams[freq].append(s)
            else:
                anagrams[freq] = [s]

        return list(anagrams.values())