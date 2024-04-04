int maxDepth(char* s) {
    //  Accumulator
    //  - increment when '('
    //  - decrement when ')'
    int count = 0;

    int max_count = 0;  //  Max of count

    for (int i = 0; s[i] != 0; i++) {
        int c = s[i];

        if (c == 40)       //  '('
            count++;
        else if (c == 41)  //  ')'
            count--;
        
        if (count > max_count)
            //  when 'count' overtakes
            //  'max_count'
            max_count++;
    }

    return max_count;
}