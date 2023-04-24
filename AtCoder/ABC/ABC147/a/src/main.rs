#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        a: [i32; 3]
    }
    let sum: i32 = a.iter().fold(0, |sum, x| sum + x);
    if sum >= 22 {
        println!("bust");
    } else {
        println!("win")
    }
}
