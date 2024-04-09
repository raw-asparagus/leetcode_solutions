int timeRequiredToBuy(int* tickets, int ticketsSize, int k) {
    //  Iterate and increase 'time' if person
    //  still has tickets to purchase (tracked by
    //  'cycle'). Return when person buys last
    //  ticket
    int time = 0;

    for (int i = 1; i <= tickets[k]; i++) {
        for (int j = 0; j < ticketsSize; j++) {
            if (tickets[j] >= i) {
                time++;
                if (j == k && i == tickets[k])
                    return time;
            }
        }
    }

    return 0;
}