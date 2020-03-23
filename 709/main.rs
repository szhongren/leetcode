fn main() {
    println!(
        "{:?}",
        Solution::to_lower_case("Hello".to_string())
    );
    println!(
        "{:?}",
        Solution::to_lower_case("here".to_string())
    );
    println!(
        "{:?}",
        Solution::to_lower_case("LOVELY".to_string())
    );
}

struct Solution;

impl Solution {
    pub fn to_lower_case(str: String) -> String {
        str.to_lowercase()
    }
}
