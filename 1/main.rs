use std::collections::HashMap;

fn main() {
    println!("{:#?}", Solution::two_sum(vec![2, 7, 11, 15], 9));
}

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut result = vec![];
        let mut seen = HashMap::new();
        for tuple in nums.iter().enumerate() {
            let (i, val) = tuple;
            match seen.get(&(target - val)) {
                Some(&index) => {
                    result.push(index as i32);
                    result.push(i as i32);
                    break;
                }
                None => {}
            }
            seen.insert(val, i);
        }
        result
    }
}
