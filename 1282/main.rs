use std::collections::HashMap;
use std::cell::RefCell;

fn main() {
    println!("{:?}", Solution::group_the_people(vec![3, 3, 3, 3, 3, 1, 3]));
    println!("{:?}", Solution::group_the_people(vec![2, 1, 3, 3, 3, 2]));
}

#[derive(Debug)]
struct GroupStruct {
    filled_groups: Vec<RefCell<Vec<i32>>>,
    filling_group: RefCell<Vec<i32>>
}

struct Solution;

impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut groups_map = HashMap::new();
        for (i, group_size) in group_sizes.iter().enumerate() {
            match groups_map.get_mut(group_size) {
                None => {
                    groups_map.insert(group_size, GroupStruct {
                        filled_groups: vec![],
                        filling_group: RefCell::from(vec![i as i32])
                    });
                },
                Some(group_struct) => {
                    if group_struct.filling_group.borrow().len() as i32 == *group_size {
                        group_struct.filled_groups.push(group_struct.filling_group.clone());
                        group_struct.filling_group = RefCell::from(vec![]);
                    }
                    group_struct.filling_group.borrow_mut().push(i as i32);
                },
            }
        }
        let mut result = vec![];
        for group_struct in groups_map.values() {
            for filled_group in group_struct.filled_groups.clone() {
                result.push(filled_group.clone());
            }
            result.push(group_struct.filling_group.clone());
        }
        result.into_iter().map(|refcell| refcell.into_inner()).collect()
    }
}
