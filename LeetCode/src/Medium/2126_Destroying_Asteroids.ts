/**
 * @param mass 初期質量
 * @param asteroids 各小惑星の質量
 *
 * 考察:
 * [直感的] 上回ればいいので、質量が小さい順から衝突させていけばいいのではないか？
 * ex1の場合: 3や5が最後にあっても、そりゃ壊れるでしょう。逆に大きい数値が最初にあったら壊れないでしょう。
 * よって、
 * ex: mass < min(asteroids) => 小惑星を壊せない
 * ex: mass >= max(asteroids) => どうやっても小惑星を壊せる
 * 困るパターンを考えてみる。 -> 色々考えたが出てこない… -> 多分大丈夫そう
 */

function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
  const sortedAsteroids = asteroids.sort((a, b) => a - b);
  let currentMass = mass;
  for (const asteroid of sortedAsteroids) {
    if (currentMass < asteroid) return false;
    currentMass += asteroid;
  }
  return true;
}

console.log(asteroidsDestroyed(10, [3, 9, 19, 5, 21])); // true
console.log(asteroidsDestroyed(5, [4, 9, 23, 4])); // false
