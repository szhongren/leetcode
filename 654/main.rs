use std::cell::RefCell;
use std::cmp::Ordering;
use std::rc::Rc;

fn main() {
    println!("{:#?}", Solution::construct_maximum_binary_tree(vec![]));
    println!("{:#?}", Solution::construct_maximum_binary_tree(vec![0]));
    println!("{:#?}", Solution::construct_maximum_binary_tree(vec![1]));
    println!(
        "{:#?}",
        Solution::construct_maximum_binary_tree(vec![3, 2, 1, 6, 0, 5])
    );
}

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

struct Solution;

impl Solution {
    pub fn construct_maximum_binary_tree(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::construct_maximum_binary_tree_recursive(&nums[..])
    }

    pub fn construct_maximum_binary_tree_recursive(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
        match nums.len() {
            0 => None,
            1 => Option::from(Rc::from(RefCell::from(TreeNode {
                val: nums[0],
                left: None,
                right: None,
            }))),
            _ => {
                let index_of_max = nums
                    .iter()
                    .enumerate()
                    .max_by(|(_, a), (_, b)| a.partial_cmp(b).unwrap_or(Ordering::Equal))
                    .map(|(index, _)| index)
                    .unwrap();
                Option::from(Rc::from(RefCell::from(TreeNode {
                    val: nums[index_of_max],
                    left: Self::construct_maximum_binary_tree_recursive(&nums[..index_of_max]),
                    right: Self::construct_maximum_binary_tree_recursive(&nums[index_of_max + 1..]),
                })))
            }
        }
    }
}
