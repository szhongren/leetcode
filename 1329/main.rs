fn main() {
    println!("{:#?}", Solution::diagonal_sort(
        vec![
            vec![3, 3, 1, 1],
            vec![2, 2, 1, 2],
            vec![1, 1, 1, 2]]));
}

struct Solution;

impl Solution {
    pub fn diagonal_sort(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows = mat.len();
        let cols = mat.get(0).unwrap_or(&vec![]).len();
        println!("{}, {}", rows, cols);
        vec![]
    }
}
