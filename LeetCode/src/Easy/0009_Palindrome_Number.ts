// Memo: String -> split / String -> split -> reverse 
function isPalindrome(x: number): boolean {
    const strX = String(x);
    const n = strX.length
    for (let idx = 0; idx < n; idx++) {
        if (strX[idx] !== strX[n - idx - 1]) {
            return false;
        }
    }
    return true;
}

console.log(isPalindrome(121))
console.log(isPalindrome(-121))
console.log(isPalindrome(10))