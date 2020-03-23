fn main() {
    println!("{:?}", Solution::count_negatives(vec![
        vec![4, 3, 2, -1],
        vec![3, 2, 1, -1],
        vec![1, 1, -1, -2],
        vec![-1, -1, -2, -3],
    ]));
    println!("{:?}", Solution::count_negatives(vec![
        vec![3, 2],
        vec![1, 0],
    ]));
    println!("{:?}", Solution::count_negatives(vec![
        vec![1, -1],
        vec![-1, -1],
    ]));
    println!("{:?}", Solution::count_negatives(vec![
        vec![-1],
    ]));
}

struct Solution;

impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let total_numbers = grid.len() * grid[0].len();
        if total_numbers == 0 {
            0
        } else {
            let mut total_negatives = 0;
            let mut current_pointer = 0;
            for row in grid.iter() {
                let negatives_in_row = Self::count_negatives_for_row(row.to_vec(), &mut current_pointer);
                total_negatives += negatives_in_row;
            }

            total_negatives
        }
    }

    pub fn count_negatives_for_row(row: Vec<i32>, current_pointer: &mut usize) -> i32 {
        if *current_pointer == row.len() {
            *current_pointer -= 1;
        }
        while *current_pointer != 0 && row[*current_pointer] < 0 {
            *current_pointer -= 1;
        }
        while *current_pointer != row.len() && row[*current_pointer] >= 0 {
            *current_pointer += 1
        }
        (row.len() - *current_pointer) as i32
    }
}
