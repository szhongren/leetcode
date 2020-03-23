// use std::borrow::Borrow;
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    println!(
        "{:?}",
        Solution::sum_even_grandparent(TreeNode::from_vec(vec![
            Option::from(6),
            Option::from(7),
            Option::from(8),
            Option::from(2),
            Option::from(7),
            Option::from(1),
            Option::from(3),
            Option::from(9),
            None,
            Option::from(1),
            Option::from(4),
            None,
            None,
            None,
            Option::from(5)
        ]))
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
    pub fn sum_even_grandparent(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::sum_even_grandparent_recursive(&root)
    }

    fn get_maybe_node_val(maybe_root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match maybe_root {
            None => 0,
            Some(rc) => rc.borrow().val
        }
    }

    fn get_maybe_node_children_val(maybe_root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match maybe_root {
            None => 0,
            Some(rc) => {
                let left_child_maybe_treenode = &rc.borrow().left;
                let right_child_maybe_treenode = &rc.borrow().right;
                let left_child_val = Self::get_maybe_node_val(&left_child_maybe_treenode);
                let right_child_val = Self::get_maybe_node_val(&right_child_maybe_treenode);
                left_child_val + right_child_val
            }
        }
    }

    pub fn sum_even_grandparent_recursive(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(rc) => {
                let left_maybe_treenode = &rc.borrow().left;
                let right_maybe_treenode = &rc.borrow().right;
                let recursive_sum = Self::sum_even_grandparent_recursive(&left_maybe_treenode) + Self::sum_even_grandparent_recursive(&right_maybe_treenode);
                if rc.borrow().val % 2 != 0 {
                    recursive_sum
                } else {
                    let left_grandchildren_sum = Self::get_maybe_node_children_val(&rc.borrow().left);
                    let right_grandchildren_sum = Self::get_maybe_node_children_val(&rc.borrow().right);
                    left_grandchildren_sum + right_grandchildren_sum + recursive_sum
                }
            }
        }
    }
}
