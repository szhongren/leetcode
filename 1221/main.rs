fn main() {
    println!("{:?}", Solution::balanced_string_split("RLRRLLRLRL".to_string()));
    println!("{:?}", Solution::balanced_string_split("RLLLLRRRLR".to_string()));
    println!("{:?}", Solution::balanced_string_split("LLLLRRRR".to_string()));
    println!("{:?}", Solution::balanced_string_split("RLRRRLLRLL".to_string()));
}

struct Solution;

impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let mut balance_counter = 0;
        let mut substrings = 0;
        s.as_str().split("").for_each(|ch| {
            match ch {
            "R" => balance_counter += 1,
            "L" => balance_counter -= 1,
            _ => (),
        }
        if balance_counter == 0 {
            substrings += 1;
        }
        });
        substrings - 2
    }
}
