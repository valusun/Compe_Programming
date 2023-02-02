#![allow(non_snake_case)]
use proconio::{input, marker::Chars};

#[proconio::fastout]
fn main() {
    input! {
        n: usize,
        mut S: Chars
    }
    for i in 1..n {
        let mut cnt = 0;
        for j in 0..n {
            if i + j == n {
                break;
            }
            if S[j] == S[i + j] {
                break;
            }
            cnt += 1;
        }
        println!("{}", cnt);
    }
}
