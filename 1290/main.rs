fn main() {
    println!("{:?}", Solution::get_decimal_value(Option::None));
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![0, 0]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![0, 1]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![1, 0]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![1, 1]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![0, 0, 0]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![0, 0, 1]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![0, 1, 0]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![0, 1, 1]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![1, 0, 0]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![1, 0, 1]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![1, 1, 0]))
    );
    println!(
        "{:?}",
        Solution::get_decimal_value(ListNode::from_vec(vec![1, 1, 1]))
    );
}

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }

    fn from_vec(vec: Vec<i32>) -> Option<Box<Self>> {
        let mut current_node = None;
        for value in vec.into_iter().rev() {
            current_node = Option::from(Box::new(ListNode {
                next: current_node,
                val: value,
            }));
        }
        current_node
    }
}

struct Solution;

impl Solution {
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
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
