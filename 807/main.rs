use std::cmp::{max, min};

fn main() {
    println!(
        "{:?}",
        Solution::max_increase_keeping_skyline(vec![
            vec![3, 0, 8, 4],
            vec![2, 4, 5, 7],
            vec![9, 2, 6, 3],
            vec![0, 3, 1, 0]
        ])
    );
}

struct Solution;

impl Solution {
    pub fn max_increase_keeping_skyline(grid: Vec<Vec<i32>>) -> i32 {
        let num_x = grid.len();
        if num_x == 0 {
            return 0
        }
        let mut x_max_heights = vec![0; num_x];
        let num_y = grid[0].len();
        let mut y_max_heights = vec![0; num_y];
        for (i, col) in grid.iter().enumerate() {
            for (j, val) in col.iter().enumerate() {
                x_max_heights[i] = max(x_max_heights[i], *val);
                y_max_heights[j] = max(y_max_heights[j], *val);
            }
        }
        let mut max_increase = 0;
        for (i, col) in grid.iter().enumerate() {
            for (j, val) in col.iter().enumerate() {
                let increase = min(x_max_heights[i], y_max_heights[j]) - val;
                max_increase += increase;
            }
        }
        max_increase
    }
}
