# Last updated: 7/13/2025, 10:34:52 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        c = 0
        players.sort()
        trainers.sort()
        for i in trainers:
            if i>=players[c]:
                c+=1
                if c==len(players):
                    break
        return c