#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        n: usize,
        mut a: [i32; n],
        q: usize
    }
    for _ in 0..q {
        input! { num: usize}
        if num == 1 {
            input! {
                k: usize,
                x: i32,
            }
            a[k - 1] = x;
        } else {
            input! {
                k: usize
            }
            println!("{}", a[k - 1]);
        }
    }
}
