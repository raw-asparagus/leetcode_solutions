char* makeGood(char* s) {
    //  =====
    //  Stack
    //  =====

    //  Pop last and skip next if next-last pair
    //  makes the string bad, else appends next
    //  character
    
    int s_len = strlen(s);
    char* stack = (char*) malloc((s_len + 1) * sizeof(char));
    int stack_ptr = 1;

    stack[0] = s[0];

    for (int i = 1; i < s_len; i++) {
        if (stack_ptr > 0 && abs(stack[stack_ptr - 1] - s[i]) == 32) {
            stack_ptr--;
            continue;
        }

        stack[stack_ptr++] = s[i];     
    }

    stack[stack_ptr] = '\0';

    return stack;
}