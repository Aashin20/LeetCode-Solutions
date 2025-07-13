# Last updated: 7/13/2025, 10:33:48 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i=0
        j=0
        matching = 0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                matching+=1
                i+=1
                j+=1
            else:
                j+=1
        return matching