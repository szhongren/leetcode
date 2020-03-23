use std::cmp::min;

fn main() {
    println!(
        "{:?}",
        Solution::min_time_to_visit_all_points(vec![vec![1, 1], vec![3, 4], vec![-1, 0]])
    );
    println!(
        "{:?}",
        Solution::min_time_to_visit_all_points(vec![vec![3, 2], vec![-2, 2]])
    );
}

struct Solution;

impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut total_time = 0;
        let mut current_point = &points[0];
        for point in points.iter() {
            let delta_x = (current_point[0] - point[0]).abs();
            let delta_y = (current_point[1] - point[1]).abs();
            total_time += min(delta_x, delta_y) + (delta_x - delta_y).abs();
            current_point = point;
        }
        total_time
    }
}
