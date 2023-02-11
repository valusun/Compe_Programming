#![allow(non_snake_case)]
use proconio::{input, marker::Chars};

#[proconio::fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        s: [Chars; n],
    }
    let mut ans = 0;
    for i in 0..n {
        for j in (i+1)..n {
            if (0..m).all(|k| s[i][k]=='o' || s[j][k]=='o'){
                ans += 1;
            }
        }
    }
    println!("{}", ans);
}
