fn main() {
    println!(
        "{:?}",
        Solution::add_two_numbers(
            ListNode::from_vec(vec![2, 4, 3]),
            ListNode::from_vec(vec![5, 6, 4])
        )
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

pub fn new_with_next(val: i32, next: Option<Box<ListNode>>) -> ListNode {
    ListNode { next, val }
}

struct Solution;

impl Solution {
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        Solution::add_two_numbers_recursive(l1, l2, 0)
    }

    pub fn add_two_numbers_recursive(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
        carry: i32,
    ) -> Option<Box<ListNode>> {
        if l1.is_none() && l2.is_none() {
            if carry != 0 {
                Option::from(Box::new(ListNode::new(carry)))
            } else {
                None
            }
        } else if l1.is_none() && l2.is_some() {
            Solution::add_two_numbers_recursive(l2, l1, carry)
        } else if l1.is_some() && l2.is_none() {
            let listnode = l1.unwrap().clone();
            let next = listnode.next;
            let value = listnode.val + carry;
            Option::from(Box::new(new_with_next(
                value % 10,
                Solution::add_two_numbers_recursive(next, None, value / 10),
            )))
        } else {
            let listnode1 = l1.unwrap().clone();
            let listnode2 = l2.unwrap().clone();
            let next1 = listnode1.next;
            let next2 = listnode2.next;
            let value = listnode1.val + listnode2.val + carry;
            Option::from(Box::new(new_with_next(
                value % 10,
                Solution::add_two_numbers_recursive(next1, next2, value / 10),
            )))
        }
    }
}
