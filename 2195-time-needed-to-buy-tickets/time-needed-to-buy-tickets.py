class Solution:
    #   Iterate and increase 'elapsed_time' if
    #   person still has tickets to purchase
    #   (tracked by 'cycle'). Return when person
    #   buys last ticket
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        elapsed_time = 0

        for cycle in range(1, tickets[k] + 1):
            for idx, val in enumerate(tickets):
                if val >= cycle:
                    elapsed_time += 1
                    if idx == k and val == cycle:
                        return elapsed_time

        return 0
