"use strict";
const dfs = (mx, pattern, l_cnt, r_cnt, result) => {
    if (pattern.length == mx) {
        result.push(pattern);
        return result;
    }
    if (l_cnt > r_cnt) {
        dfs(mx, pattern + ")", l_cnt, r_cnt + 1, result);
    }
    if (l_cnt < mx / 2) {
        dfs(mx, pattern + "(", l_cnt + 1, r_cnt, result);
    }
    return result;
};
function generateParenthesis(n) {
    return dfs(n * 2, "(", 1, 0, []);
}
console.log(generateParenthesis(3));
