function convert(s: string, numRows: number): string {
  const memo: string[] = [];
  const loopIdx = numRows === 1 ? 1 : numRows + numRows - 2;
  for (let row = 0; row < numRows; row++) {
    let idx = row;
    const step1 = row === numRows - 1 ? loopIdx : loopIdx - row * 2;
    while (idx < s.length) {
      memo.push(s[idx]);
      if (loopIdx !== step1 && idx + step1 < s.length) {
        memo.push(s[idx + step1]);
      }
      idx += loopIdx;
    }
  }
  return memo.join("");
}

console.log(convert("PAYPALISHIRING", 3));
console.log(convert("PAYPALISHIRING", 4));
console.log(convert("PAYPALISHIRING", 1));
