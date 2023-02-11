#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        n: i32
    }
    for i in 0..n {
        print!("{}", (b'A' + i) as char);
    }
}
