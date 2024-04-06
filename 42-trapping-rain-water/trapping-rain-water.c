int trap(int* height, int heightSize) {
    //  ===========
    //  Two Pointer
    //  ===========

    //  Shift the left pointer and the right
    //  pointer towards each other until they
    //  meet. Each pointer tracks the max height
    //  encountered and increments accum by the
    //  difference in heights for 'valleys'
    int accum = 0;

    int i = 0;
    int left_max = height[0];
    int j = heightSize - 1;
    int right_max = height[j];

    while (i < j) {
        if (left_max < right_max) {
            left_max = left_max > height[++i] ? left_max : height[i];
            accum += left_max - height[i];
        }
        else {
            right_max = right_max > height[--j] ? right_max : height[j];
            accum += right_max - height[j];
        }
    }

    return accum;
}