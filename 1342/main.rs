fn main() {
    println!("{:?}", Solution::number_of_steps(8));
    println!("{:?}", Solution::number_of_steps(14));
}

struct Solution;

impl Solution {
    pub fn number_of_steps(num: i32) -> i32 {
        let mut decrementor = num;
        let mut counter = 0;
        while decrementor != 0 {
            match decrementor % 2 {
                0 => decrementor /= 2,
                1 => decrementor -= 1,
                _ => ()
            }
            counter += 1;
        }
        return counter;
    }
}
