An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


class Solution:
     def isAnagram(self, s: str, t: str) -> bool:
         return Counter(s) == Counter(t)str, t: str) -> bool:
        