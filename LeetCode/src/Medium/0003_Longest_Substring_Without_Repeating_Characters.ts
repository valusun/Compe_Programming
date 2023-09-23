function lengthOfLongestSubstring(s: string): number {
    const elmCounter: string[] = []
    let ans = 0, left = 0, right = 0;
    while (right < s.length) {
        if (elmCounter.indexOf(s[right]) !== -1) {
            ans = ans > right - left ? ans : right - left;
            elmCounter.splice(elmCounter.indexOf(s[left]), 1)
            left++;
        } else {
            elmCounter.push(s[right]);
            right++;
        }
    }
    return ans > s.length - left ? ans : s.length - left
}

console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("pw"))