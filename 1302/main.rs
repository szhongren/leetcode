use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    println!(
        "{:?}",
        Solution::deepest_leaves_sum(TreeNode::from_vec(vec![
            Option::from(1),
            Option::from(2),
            Option::from(3),
            Option::from(4),
            Option::from(5),
            None,
            Option::from(6),
            Option::from(7),
            None,
            None,
            None,
            None,
            None,
            None,
            Option::from(8),
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
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let queue = vec![root];
        Self::deepest_leaves_sum_recursive(queue, 0)
    }

    pub fn deepest_leaves_sum_recursive(
        queue: Vec<Option<Rc<RefCell<TreeNode>>>>,
        previous_sum: i32,
    ) -> i32 {
        let mut sum = 0;
        let mut all_none = true;
        let mut new_queue = Vec::new();
        queue
            .iter()
            .for_each(|maybe_treenode| match maybe_treenode {
                None => (),
                Some(rc) => {
                    sum += rc.borrow().val; // auto deref the Rc, borrow from RefCell
                    new_queue.push(rc.borrow().left.clone()); // auto deref the Rc, borrow from RefCell
                    new_queue.push(rc.borrow().right.clone()); // auto deref the Rc, borrow from RefCell
                    all_none = false;
                }
            });
        if all_none {
            previous_sum
        } else {
            Self::deepest_leaves_sum_recursive(new_queue, sum)
        }
    }
}
