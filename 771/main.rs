fn main() {
    println!("{:?}", Solution::num_jewels_in_stones("aA".to_string(), "aAAbbbb".to_string()));
    println!("{:?}", Solution::num_jewels_in_stones("z".to_string(), "ZZ".to_string()));
}

struct Solution;

impl Solution {
    pub fn num_jewels_in_stones(j: String, s: String) -> i32 {
        s.as_str().split("").filter(|ch| j.as_str().split("").map(|jewel| if &jewel == ch {1} else {0}).sum::<i32>() != 0).count() as i32 - 2
    }
}
