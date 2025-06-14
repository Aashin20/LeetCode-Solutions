# Last updated: 6/14/2025, 10:32:10 PM
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15,celsius*1.80+32]
        