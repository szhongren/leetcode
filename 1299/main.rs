fn main() {
    println!("{:#?}", Solution::replace_elements(vec![17, 18, 5, 4, 6, 1]));
}

struct Solution;

impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        let mut result = vec![];
        let mut current_max: i32 = -1;
        for val in arr.iter().rev() {
            result.push(current_max);
            current_max = if *val > current_max {*val} else {current_max};
        }
        result.reverse();
        result
    }
}
