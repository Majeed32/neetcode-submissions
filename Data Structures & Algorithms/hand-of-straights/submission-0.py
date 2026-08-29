class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        numMap = defaultdict(int)
        if len(hand) % groupSize != 0:
            return False
        for num in hand:
            numMap[num] += 1
        hand.sort()
        res = []
        for num in hand:
            if numMap[num] > 0:
                numMap[num] -= 1
                curr = num+1
                for _ in range(groupSize-1):
                    if numMap[curr] == 0:
                        return False
                    numMap[curr] -= 1
                    curr += 1
        return True


        