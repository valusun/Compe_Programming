function maxArea(height: number[]): number {
    const n = height.length;
    let ans = 0, left = 0, right = n - 1;
    while (left < right) {
        const res = Math.min(height[left], height[right]) * (right - left);
        ans = Math.max(ans, res);
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return ans;
}

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
console.log(maxArea([1, 1]))