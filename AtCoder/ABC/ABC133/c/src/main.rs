#![allow(non_snake_case)]
use proconio::input;
use std::cmp;

#[proconio::fastout]
fn main() {
    input! {
        L: i64,
        R: i64
    }
    let mut ans = 2019;
    for i in L..R + 1 {
        for j in i + 1..R + 1 {
            ans = cmp::min(ans, i * j % 2019);
            if ans == 0 {
                println!("{}", ans);
                return;
            }
        }
    }
    println!("{}", ans);
}
