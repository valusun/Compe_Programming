#![allow(non_snake_case)]
use proconio::{input, marker::Chars};

#[proconio::fastout]
fn main() {
    input! {
        s: Chars
    }
    if (s.len() == 8 && s[0].is_uppercase() && s[1] != '0' && (1..7).all(|i| s[i].is_numeric()) && s[7].is_uppercase()) {
        println!("Yes");
    } else {
        println!("No");
    }
}
