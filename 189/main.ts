// /**
//  Do not return anything, modify nums in-place instead.
//  */
// function rotate(nums: number[], k: number): void {
//   k = k % nums.length;
//   let front = nums.slice(0, nums.length - k);
//   let back = nums.slice(nums.length - k);
//   console.log(nums.length - k, front, back);
//   for (let i = 0; i < nums.length; i++) nums[i] = back.concat(front)[i];
// }
// //  0  1  2  3  4  5  6
// // [7, 1, 2, 3, 4, 5, 6];

/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
  k = k % nums.length;
  let unvisited_indices = new Set();
  for (let i = 0; i < nums.length; i++) unvisited_indices.add(i);
  while (unvisited_indices.size !== 0) {
    let current_index = unvisited_indices.keys().next().value;
    let temp_store = [nums[current_index]];
    while (
      unvisited_indices.has(
        getIndexOfDestination(current_index, k, nums.length)
      )
    ) {
      let next_index = getIndexOfDestination(current_index, k, nums.length);
      temp_store.push(nums[next_index]);
      nums[next_index] = temp_store[0];
      temp_store = [temp_store[1]];
      current_index = next_index;
      unvisited_indices.delete(current_index);
    }
  }
}

function getIndexOfDestination(i: number, k: number, length: number) {
  return (i + k) % length;
}
//  0  1  2  3  4  5  6
// [7, 1, 2, 3, 4, 5, 6];

console.log(rotate([7, 1, 2, 3, 4, 5, 6], 3));
