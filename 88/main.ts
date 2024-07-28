/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  // do nothing
  if (m === 0) {
    // [], [...]
    for (let i = 0; i < n; i++) {
      nums1[i] = nums2[i];
    }
    return;
  }
  if (n === 0) return;

  // from the back so we don't have to move
  let i = m - 1;
  let j = n - 1;
  let current_spot = m + n - 1;

  while (current_spot >= 0) {
    console.log(i, j, current_spot);
    console.log(nums1);
    if (i >= 0 && j >= 0) {
      if (nums1[i] >= nums2[j]) {
        nums1[current_spot] = nums1[i--];
      } else {
        nums1[current_spot] = nums2[j--];
      }
    } else {
      if (i < 0) {
        nums1[current_spot] = nums2[j--];
      } else if (j < 0) {
        nums1[current_spot] = nums1[i--];
      }
    }

    current_spot--;
  }
}
