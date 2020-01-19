fn main() {
    println!("{:?}", Solution::subtract_product_and_sum(234));
    println!("{:?}", Solution::subtract_product_and_sum(4421));
}

struct Solution;

impl Solution {
    pub fn subtract_product_and_sum(n: i32) -> i32 {
        let mut product = 1;
        let mut sum = 0;
        let mut number_decrementer = n;
        while number_decrementer != 0 {
            let digit = number_decrementer % 10;
            product *= digit;
            sum += digit;
            number_decrementer /= 10;
        }
        product - sum
    }
}
