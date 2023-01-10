#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        n: usize,
        mut d: [i32; n],
    }
    d.sort();
    println!("{}", d[n / 2] - d[n / 2 - 1]);
}
