#![allow(non_snake_case)]
use proconio::input;

#[proconio::fastout]
fn main() {
    input! {
        n: usize,
        mut s: String,
    }
    let mut ans = String::new();
    let mut dq_cnt = 0;
    for c in s.chars() {
        if c == '"' {
            dq_cnt += 1;
        }
        if c == ',' {
            if dq_cnt % 2 == 0{
                ans.push('.');
            } else {
                ans.push(',');
            }
            continue;
        }
        ans.push(c)
    }
    println!("{}", ans);
}
