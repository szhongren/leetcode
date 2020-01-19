fn main() {
    println!("{}", Solution::defang_i_paddr("127.0.0.1".to_string()));
}

struct Solution;

impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        str::replace(&address[..], ".", "[.]")
    }
}
