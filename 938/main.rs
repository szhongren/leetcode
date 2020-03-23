use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    println!("{:?}", Solution::range_sum_bst(None, 1, 2));
    println!(
        "{:?}",
        Solution::range_sum_bst(
            TreeNode::from_vec(vec![
                Option::from(10),
                Option::from(5),
                Option::from(15),
                Option::from(3),
                Option::from(7),
                None,
                Option::from(18)
            ]),
            7,
            15
        )
    );
}

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    fn from_vec(vec: Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        Self::from_vec_recursive(&vec, 0)
    }

    fn from_vec_recursive(vec: &Vec<Option<i32>>, i: usize) -> Option<Rc<RefCell<TreeNode>>> {
        if i < vec.len() {
            match vec[i] {
                // just fucking construct a new thing to get around immutability
                None => None,
                Some(value) => Option::from(Rc::from(RefCell::from(TreeNode {
                    val: value,
                    left: Self::from_vec_recursive(vec, 2 * i + 1),
                    right: Self::from_vec_recursive(vec, 2 * i + 2),
                }))),
            }
        } else {
            None
        }
    }
}

struct Solution;

impl Solution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, l: i32, r: i32) -> i32 {
        Self::range_sum_bst_recursive(&root, l, r)
    }

    pub fn range_sum_bst_recursive(root: &Option<Rc<RefCell<TreeNode>>>, l: i32, r: i32) -> i32 {
        match root {
            None => 0,
            Some(rc) => {
                let recursive_sum = Self::range_sum_bst_recursive(&rc.borrow().left, l, r)
                    + Self::range_sum_bst_recursive(&rc.borrow().right, l, r);
                let current_val = if rc.borrow().val >= l && rc.borrow().val <= r {
                    rc.borrow().val
                } else {
                    0
                };
                recursive_sum + current_val
            }
        }
    }
}
