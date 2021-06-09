fn main() {
    println!(
        "{:?}",
        Solution::is_sum_equal("acb".to_string(), "cba".to_string(), "cdb".to_string())
    );
    println!(
        "{:?}",
        Solution::is_sum_equal("aaa".to_string(), "a".to_string(), "aab".to_string())
    );
    println!(
        "{:?}",
        Solution::is_sum_equal("aaa".to_string(), "a".to_string(), "aaaa".to_string())
    );
}

struct Solution;

impl Solution {
    pub fn is_sum_equal(first_word: String, second_word: String, target_word: String) -> bool {
        let first_word_value = Solution::get_word_value(first_word);
        let second_word_value = Solution::get_word_value(second_word);
        let target_word_value = Solution::get_word_value(target_word);
        first_word_value + second_word_value == target_word_value
    }

    fn get_word_value(word: String) -> u32 {
        word.chars()
            .map(|ch: char| ch as u32 - 97)
            .reduce(|a, b| a * 10 + b)
            .unwrap()
    }
}
