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
        if (height[i] < height[j]) {
            if (height[i] < left_max)
                accum += left_max - height[i++];
            else left_max = height[i++];
        }
        else {
            if (height[j] < right_max)
                accum += right_max - height[j--];
            else right_max = height[j--];
        }
    }

    return accum;
}