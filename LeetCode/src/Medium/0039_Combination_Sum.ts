function combinationSum(candidates: number[], target: number): number[][] {
  const ans: number[][] = [];

  const solve = (now: number[], amount: number, idx: number) => {
    if (amount === 0 || idx === candidates.length) {
      if (amount === 0) {
        ans.push(now);
      }
      return;
    }
    const loopCount = Math.floor(amount / candidates[idx]);
    solve(now, amount, idx + 1); // not selected
    const tmp = [...now];
    for (let i = 1; i <= loopCount; i++) {
      tmp.push(candidates[idx]);
      solve(tmp, amount - candidates[idx] * i, idx + 1);
    }
  };

  solve([], target, 0);
  return ans;
}

console.log(combinationSum([2, 3, 6, 7], 7));
console.log(combinationSum([2, 3, 5], 8));
console.log(combinationSum([2], 1));
