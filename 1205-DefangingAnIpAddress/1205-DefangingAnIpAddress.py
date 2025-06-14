# Last updated: 6/14/2025, 10:32:46 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')