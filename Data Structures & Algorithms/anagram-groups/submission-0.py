from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouppedAnagrams = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            grouppedAnagrams[key].append(word)
        return list(grouppedAnagrams.values())

        