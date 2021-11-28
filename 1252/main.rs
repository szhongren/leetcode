fn main() {
    println!(
        "{:#?}",
        Solution::odd_cells(2, 3, vec![vec![0, 1], vec![1, 1]])
    );
    println!(
        "{:#?}",
        Solution::odd_cells(2, 2, vec![vec![0, 0], vec![1, 1]])
    );
}

struct Solution;

impl Solution {
    pub fn odd_cells(n: i32, m: i32, indices: Vec<Vec<i32>>) -> i32 {
        let mut odd_rows = vec![false; n as usize];
        let mut odd_cols = vec![false; m as usize];
        let mut count_rows = 0;
        let mut count_cols = 0;
        for index in indices {
            let x = *(index.get(0).unwrap()) as usize;
            let y = *(index.get(1).unwrap()) as usize;
            odd_rows[x] ^= true;
            odd_cols[y] ^= true;
            count_rows += if odd_rows[x] { 1 } else { -1 };
            count_cols += if odd_cols[y] { 1 } else { -1 };
        }
        (m - count_cols) * count_rows + (n - count_rows) * count_cols
    }
}
