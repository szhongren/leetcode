fn main() {
    println!("{:?}", Solution::maximum69_number(6));
    println!("{:?}", Solution::maximum69_number(9));
    println!("{:?}", Solution::maximum69_number(66));
    println!("{:?}", Solution::maximum69_number(69));
    println!("{:?}", Solution::maximum69_number(96));
    println!("{:?}", Solution::maximum69_number(99));
    println!("{:?}", Solution::maximum69_number(666));
    println!("{:?}", Solution::maximum69_number(669));
    println!("{:?}", Solution::maximum69_number(696));
    println!("{:?}", Solution::maximum69_number(699));
    println!("{:?}", Solution::maximum69_number(966));
    println!("{:?}", Solution::maximum69_number(969));
    println!("{:?}", Solution::maximum69_number(996));
    println!("{:?}", Solution::maximum69_number(999));
}

struct Solution;

impl Solution {
    pub fn maximum69_number(n: i32) -> i32 {
        let mut number_decrementer = n;
        let mut reverse_index = Option::None;
        let mut previous_6_index = Option::<i32>::None;
        while number_decrementer != 0 {
            let digit = number_decrementer % 10;
            number_decrementer /= 10;
            reverse_index = match reverse_index {
                None => Option::from(0),
                Some(index) => Option::from(index + 1),
            };
            match digit {
                6 => previous_6_index = Option::from(reverse_index.unwrap()),
                _ => (),
            };
        }
        match previous_6_index {
            None => n,
            Some(index) => n + 9 * 10_i32.pow(index as u32) - 6 * 10_i32.pow(index as u32),
        }
    }
}
