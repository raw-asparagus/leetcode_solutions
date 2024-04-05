int maxDepth(char* s) {
    //  ===========================
    //  Stack -- Last in, First out
    //  ===========================

    //  Increment/decrement count on '(' / ')',
    //  tracking max in max_count
    int count = 0;
    int max_count = count;

    for (int i = 0; s[i] != 0; i++) {
        int c = s[i];

        if (c == 40)
            max_count < ++count ? max_count = count : 0;
        else if (c == 41) count--;
    }

    return max_count;
}