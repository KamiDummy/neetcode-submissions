class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i, s in enumerate(strs):
            letters = [0] * 26
            for letter in s:
                letters[ord(letter) - ord('a')] += 1
            dict[tuple(letters)].append(s)
        
        result = []
        for value in dict.values():
            result.append(value)

        return result


