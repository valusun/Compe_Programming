/**
 * 円の中に長方形がいるかどうか、という観点で調べてみる
 * 半径が x ということは、円の原点から x 離れた距離が円の範囲
 * -> 長方形がその中に属していれば良い。つまりは、円に一番近い点を求めて、それが半径に属していればよさそう
 * どう求めるか
 * 1. 長方形の取り得る座標で全探索 → 出来るが、O(n^2)で嬉しくはない
 * 2. 外周座標の全探索 + 長方形内に円が収まっているかのチェック → 1より良さそう
 * -> それでも無駄なところまで見てしまう
 * 長方形と円の中心の位置でx,y座標が特定できないか
 * -> 円の中心が長方形の左側にあるのであれば、x1 右側であれば x2 になる → yも似たようなことが言える
 * -> O(1)で済む
 */
function checkOverlap(
  radius: number,
  xCenter: number,
  yCenter: number,
  x1: number,
  y1: number,
  x2: number,
  y2: number,
): boolean {
  const x = Math.max(x1, Math.min(xCenter, x2));
  const y = Math.max(y1, Math.min(yCenter, y2));
  const dx = x - xCenter;
  const dy = y - yCenter;

  return Math.sqrt(dx ** 2 + dy ** 2) <= radius;
}

console.log(checkOverlap(1, 0, 0, 1, -1, 3, 1));
console.log(checkOverlap(1, 1, 1, 1, -3, 2, -1));
console.log(checkOverlap(1, 0, 0, -1, 0, 0, 1));
