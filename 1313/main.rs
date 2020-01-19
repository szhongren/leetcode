fn main() {
    let example = vec![1, 2, 3, 4];
    println!("{:?}", Solution::decompress_rl_elist(example));
}

struct Solution;

impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        nums.chunks(2).map::<Vec<i32>, _>(
            |pair| (0..pair[0]).map(|_| pair[1]).collect()
        ).flatten().collect()
    }
}
