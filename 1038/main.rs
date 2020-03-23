use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    println!("{:#?}", Solution::bst_to_gst(None));
    println!(
        "{:#?}",
        Solution::bst_to_gst(
            TreeNode::from_vec(vec![
                Option::from(4),
                Option::from(1),
                Option::from(6),
                Option::from(0),
                Option::from(2),
                Option::from(5),
                Option::from(7),
                None,
                None,
                None,
                Option::from(3),
                None,
                None,
                None,
                Option::from(8)
            ])
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
    pub fn bst_to_gst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let i = Self::bst_to_gst_recursive(&root, 0);
        root
    }

    // returns total sum of entire tree
    pub fn bst_to_gst_recursive(root: &Option<Rc<RefCell<TreeNode>>>, carried_sum: i32) -> i32 {
        match root {
            None => 0,
            Some(rc) => {
                // this is the total sum of the right subtree
                let right_tree_sum = Self::bst_to_gst_recursive(&rc.borrow().right, carried_sum); 
                // +             sum of right subtree
                // + sum of other values to the right
                let total_larger_than_current = right_tree_sum + carried_sum;
                // +                 current node val
                // +             sum of right subtree
                // + sum of other values to the right
                // =                     new node val
                rc.borrow_mut().val += total_larger_than_current;
                // this is the total sum of the left subtree
                let left_tree_sum = Self::bst_to_gst_recursive(&rc.borrow().left, rc.borrow().val);
                // +                 current node val
                // +             sum of right subtree
                // + sum of other values to the right
                // +              sum of left subtree
                // - sum of other values to the right
                // =        total sum of current tree
                rc.borrow().val + left_tree_sum - carried_sum
            }
        }
    }
}
