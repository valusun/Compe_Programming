#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        n: usize,
        t: i64,
        song_times: [i64; n]
    }
    let time_sum: i64 = (song_times.iter().sum());
    let mut amount: i64 = t % time_sum;
    for i in 0..n {
        if song_times[i] < amount {
            amount -= song_times[i];
        } else {
            println!("{} {}", i+1, amount);
            break;
        }
    }
}
