class Solution:
    #   Iterate and increase 'time' if person
    #   still has tickets to purchase (tracked by
    #   'cycle'). Return when person buys last
    #   ticket
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        for cycle in range(1, tickets[k] + 1):
            for idx, val in enumerate(tickets):
                if val >= cycle:
                    time += 1
                    if idx == k and val == cycle:
                        return time

        return 0
