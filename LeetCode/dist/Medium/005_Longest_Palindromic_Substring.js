"use strict";
function longestPalindrome(s) {
    const n = s.length;
    let dp = [];
    for (let i = 0; i < n; i++) {
        let tmp = [];
        for (let j = 0; j < n; j++) {
            tmp.push(false);
        }
        dp.push(tmp);
    }
    let mx = 0, left = 0, right = 0;
    for (let i = n - 1; i >= 0; i--) {
        for (let j = i; j < n; j++) {
            if (j - i <= 1) {
                dp[i][j] = (s[i] == s[j]);
            }
            else {
                dp[i][j] = dp[i + 1][j - 1] && (s[i] == s[j]);
            }
            if (dp[i][j] && mx < j - i + 1) {
                mx = j - i + 1;
                left = i;
                right = j;
            }
        }
    }
    console.log(dp);
    return s.slice(left, right + 1);
}
;
console.log(longestPalindrome("babad"));
