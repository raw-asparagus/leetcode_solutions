int trap(int* height, int heightSize) {
    int acc = 0;                //  Accumulator

    int i = 0;
    int left_max = height[0];   //  Left
    int j = heightSize - 1;
    int right_max = height[j];  // Right

    // Iterates until right meets left
    while (i < j) {
        //  Right is taller
        if (height[i] < height[j]) {
            //  Next left is shorter than previous
            if (height[i] < left_max)
                acc += left_max - height[i];
            //  Next left is taller than previous
            else
                left_max = height[i];
            
            i++;
        }
        //  Left is taller or both are same height
        else {
            // Previous right is shorter than next
            if (height[j] < right_max)
                acc += right_max - height[j];
            // Previous right is taller than next
            else
                right_max = height[j];
            
            j--;
        }
    }

    return acc;
}