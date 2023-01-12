#![allow(non_snake_case)]
use proconio::input;
use std::cmp;

#[proconio::fastout]
fn main() {
    input! {
        n: i32,
        a: i32,
        b: i32
    }
    println!("{}", cmp::min(n * a, b));
}
