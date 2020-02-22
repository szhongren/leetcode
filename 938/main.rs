use std::rc::Rc;
use std::cell::RefCell;

fn main() {
    println!("{:?}", Solution::range_sum_bst(None));
}

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>
}

impl TreeNode {
    #[inline]
    fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }

    fn from_vec(vec: Vec<i32>) -> Option<Rc<RefCell<Self>>> {
        let mut current_node = None;
        for value in vec.into_iter().rev() {
            current_node = Option::from(Box::new(ListNode {
                next: current_node,
                val: value
            }));
        }
        current_node
    }
}

struct Solution;

impl Solution {
    pub fn range_sum_bst(head: Option<Box<ListNode>>) -> i32 {
        let mut current_node = head;
        let mut total = Vec::new();
        while let Some(node) = current_node {
            if (*node).val == 1 {
                total.push((*node).val);
            }
            current_node = (*node).next;
            total = total.into_iter().map(|val| val * 2).collect();
        }
        total.into_iter().sum::<i32>() / 2
    }
}
