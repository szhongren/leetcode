use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    println!(
        "{:#?}",
        Solution::insert_into_bst(TreeNode::from_vec(vec![
            Option::from(4),
            Option::from(2),
            Option::from(7),
            Option::from(1),
            Option::from(3),
        ]), 5)
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
    pub fn insert_into_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        Self::insert_into_bst_recursive(root, val)
    }

    pub fn insert_into_bst_recursive(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        match root {
            None => Option::from(Rc::from(RefCell::from(TreeNode {
                val: val,
                left: None,
                right: None}))),
            Some(rc) => {
                let current_node_val = rc.borrow().val;
                let mut new_left_node = rc.borrow().left.clone();
                let mut new_right_node = rc.borrow().right.clone();
                if current_node_val < val {
                    new_right_node = Self::insert_into_bst_recursive(new_right_node, val);
                } else {
                    new_left_node = Self::insert_into_bst_recursive(new_left_node, val);
                }
                Option::from(Rc::from(RefCell::from(TreeNode {
                    val: current_node_val,
                    left: new_left_node,
                    right: new_right_node})))
            }
        }
    }
}
