#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        a: u32,
        b: u32
    }
    println!("{}", a.pow(b));
}
