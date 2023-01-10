#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        n: usize,
        p: [i32; n]
    }
    let mut cnt = 0;
    for i in 0..n - 2 {
        if p[i] < p[i + 1] && p[i + 1] < p[i + 2] || p[i] > p[i + 1] && p[i + 1] > p[i + 2] {
            cnt += 1;
        }
    }
    println!("{}", cnt);
}
