fn main() {
    let example = vec![12, 345, 2, 6, 7896];
    println!("{:?}", Solution::find_numbers(example));
}

struct Solution;

impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        nums.into_iter().filter(
            |number| {
                let mut digits = 0;
                let mut number_decrementer = *number;
                while number_decrementer != 0 {
                    number_decrementer /= 10;
                    digits += 1
                }
                digits % 2 == 0
            }
            ).count() as i32
    }
}
