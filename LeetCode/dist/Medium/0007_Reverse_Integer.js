"use strict";
function reverse(x) {
    let absX = Math.abs(x);
    let ans = 0;
    while (absX > 0) {
        ans = ans * 10 + absX % 10;
        absX = Math.trunc(absX / 10);
    }
    if (x < 0) {
        ans *= -1;
    }
    return (-(2 ** 31) <= ans && ans <= 2 ** 31 - 1) ? ans : 0;
}
console.log(reverse(123));
console.log(reverse(-123));
console.log(reverse(120));
