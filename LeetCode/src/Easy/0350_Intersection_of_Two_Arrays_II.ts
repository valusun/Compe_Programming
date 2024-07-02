function intersect(nums1: number[], nums2: number[]): number[] {
  const res: number[] = [];
  for (const num1 of nums1) {
    const idx = nums2.indexOf(num1);
    if (idx === -1) continue;
    res.push(num1);
    nums2[idx] = -1;
  }
  return res;
}

console.log(intersect([1, 2, 2, 1], [2, 2]));
console.log(intersect([4, 9, 5], [9, 4, 9, 8, 4]));
console.log(intersect([1, 2, 2, 1], [2]));
