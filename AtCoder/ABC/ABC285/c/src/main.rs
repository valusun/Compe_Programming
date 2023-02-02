#![allow(non_snake_case)]
use proconio::{input, marker::Chars};

#[proconio::fastout]
fn main() {
    input! {
        S: Chars
    }
    let mut ans = 0;
    for c in S.into_iter() {
        let n = c as usize - 'A' as usize;
        ans *= 26;
        ans += n + 1;
    }
    println!("{}", ans);
}
