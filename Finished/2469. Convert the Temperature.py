# https://leetcode.com/problems/convert-the-temperature/submissions/1225169674/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius*1.80 + 32]