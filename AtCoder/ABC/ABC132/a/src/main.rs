#![allow(non_snake_case)]
use proconio::{input, marker::Chars};

#[proconio::fastout]
fn main() {
    input! {
        mut S: Chars
    }
    S.sort();
    if S[0] == S[1] && S[1] != S[2] && S[2] == S[3] {
        println!("Yes");
    } else {
        println!("No");
    }
}
