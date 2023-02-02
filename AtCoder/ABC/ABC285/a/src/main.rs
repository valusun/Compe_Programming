#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        a: i32,
        b: i32
    }
    if a * 2 == b || a * 2 + 1 == b {
        println!("Yes");
    } else {
        println!("No");
    }
}
