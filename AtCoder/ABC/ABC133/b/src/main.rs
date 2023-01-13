#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        n: usize,
        d: usize,
        x: [[f64; d]; n]
    }
    let mut ans = 0;
    for i in 0..n {
        for j in i + 1..n {
            let mut dist = 0.0;
            for k in 0..d {
                // powi(x): x乗を計算しf64型で返す
                dist += (x[i][k] - x[j][k]).powi(2);
            }
            // fract(): 小数部分を返す
            if dist.sqrt().fract() == 0.0 {
                ans += 1;
            }
        }
    }
    println!("{}", ans);
}
