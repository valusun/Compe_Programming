#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        n: usize
    }
    for i in (0..n+1).rev() {
        println!("{}", i);
    }
}
