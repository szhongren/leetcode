use std::cmp::max;
use std::collections::HashMap;

fn main() {
    println!(
        "{:#?}",
        Solution::length_of_longest_substring(String::from("abcabcbb"))
    );
    println!(
        "{:#?}",
        Solution::length_of_longest_substring(String::from("bbbbb"))
    );
    println!(
        "{:#?}",
        Solution::length_of_longest_substring(String::from("pwwkew"))
    );
    println!(
        "{:#?}",
        Solution::length_of_longest_substring(String::from("tmmzuxt"))
    );
}

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut result: i32 = 0;
        let mut trailing_i: i32 = -1;
        let mut last_seen: HashMap<char, i32> = HashMap::new();
        for (i, ch) in s.chars().enumerate() {
            let i: i32 = i as i32;
            let val_option = last_seen.get_mut(&ch);
            if let Some(val) = val_option {
                if trailing_i < *val {
                    trailing_i = *val;
                }
            }
            result = max(result, i - trailing_i);
            last_seen.insert(ch, i);
        }
        result
    }
}
