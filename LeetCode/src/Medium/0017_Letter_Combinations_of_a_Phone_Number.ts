type digitToAlphabetsType = {
  [digit: string]: string[];
};

const mapping = (): digitToAlphabetsType => {
  const digitToAlphabets: digitToAlphabetsType = {
    2: ["a", "b", "c"],
  };
  for (let n = 3; n <= 9; n++) {
    digitToAlphabets[n] = [];
    const prevLength = digitToAlphabets[n - 1].length;
    const prevEnd = digitToAlphabets[n - 1][prevLength - 1].charCodeAt(0);
    const alphabetLength = n === 7 || n === 9 ? 4 : 3;
    for (let i = 0; i < alphabetLength; i++) {
      digitToAlphabets[n].push(String.fromCharCode(prevEnd + i + 1));
    }
  }
  return digitToAlphabets;
};

function letterCombinations(digits: string): string[] {
  const digitToAlphabets = mapping();
  const ans: string[] = [];
  const solve = (now: string, idx: number) => {
    if (now.length === digits.length) {
      ans.push(now);
      return;
    }
    for (const a of digitToAlphabets[digits[idx]]) {
      solve(now + a, idx + 1);
    }
  };
  if (digits.length === 0) {
    return [];
  }
  solve("", 0);
  return ans;
}

console.log(letterCombinations("23"));
console.log(letterCombinations(""));
console.log(letterCombinations("2"));
