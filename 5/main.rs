
fn main() {
    println!("{:#?}", Solution::longest_palindrome("babad".to_string()));
    println!("{:#?}", Solution::longest_palindrome( "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa".to_string()));
}

struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
                if s.len() <= 1 { return s; }
        
        let (mut start, mut end): (usize, usize) = (0, 0); 
        let bytes = s.as_bytes();
        let len = s.len() as i32;
        
        for i in 0..s.len() { 
            let (mut left, mut right) = (i as i32, i as i32);
            
			//  solve edge cases such as "baab" when index i points to the first a 
            while right < len - 1 && bytes[right as usize] == bytes[right as usize + 1] {
                right += 1;
            }
            
            while left >= 0 && (right as usize) < s.len() && bytes[left as usize] == bytes[right as usize] {
                if ((right - left) as usize) > end - start { 
                    start = left as usize; 
                    end = right as usize; 
                }
                
                left -= 1; 
                right += 1; 
            }
        }
        
        String::from_utf8(s.as_bytes()[start..=end].to_vec()).unwrap()
    }
}
