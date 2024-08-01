function longestConsecutive(nums: number[]): number {
  let longestConsecutive = 0;
  let mapOfGroups = new Map();
  for (let n = 0; n < nums.length; n++) {
    let num = nums[n];
    if (mapOfGroups.has(num)) continue;
    if (
      !mapOfGroups.has(num - 1) &&
      !mapOfGroups.has(num) &&
      !mapOfGroups.has(num + 1)
    ) {
      mapOfGroups.set(num, { min: num, max: num });
    }
    if (mapOfGroups.has(num - 1) && mapOfGroups.has(num + 1)) {
      // get min of the range to the right, then get the object pointed to by the actual min, and change that max
      mapOfGroups.get(mapOfGroups.get(num - 1).min).max = mapOfGroups.get(
        num + 1
      ).max;
      // get min of the range to the right, then get the object pointed to by the actual min, and change that max
      mapOfGroups.get(mapOfGroups.get(num + 1).max).min = mapOfGroups.get(
        num - 1
      ).min;
      mapOfGroups.set(num, {
        min: mapOfGroups.get(num - 1).min,
        max: mapOfGroups.get(num + 1).max,
      });
    } else if (mapOfGroups.has(num - 1)) {
      // -1 0 1
      //  3 ^ 0
      mapOfGroups.get(mapOfGroups.get(num - 1).min).max = num;
      mapOfGroups.set(num, mapOfGroups.get(mapOfGroups.get(num - 1).min));
    } else if (mapOfGroups.has(num + 1)) {
      mapOfGroups.get(mapOfGroups.get(num + 1).max).min = num;
      mapOfGroups.set(num, mapOfGroups.get(mapOfGroups.get(num + 1).max));
    }

    longestConsecutive = Math.max(
      longestConsecutive,
      mapOfGroups.get(num).max - mapOfGroups.get(num).min + 1
    );
    // console.log(mapOfGroups);
  }
  return longestConsecutive;
}

// longestConsecutive
// mapOfMaxSize
// for number in nums
// if number not in mapOfMaxSize
// mapOfMaxSize = 1 + mapOfMaxSize[number - 1] + mapOfMaxSize[number + 1]
// longestConsecutive = max(longestConsecutive, mapOfMaxSize[number])

console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));
console.log(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]));
console.log(longestConsecutive([1, 2, 0, 1]));
console.log(
  longestConsecutive([
    -4, -1, 4, -5, 1, -201, -6, 9, -6, -202, 0, 2, 2, 7, -203, 0, 9, -3, 8, 9,
    -2, -6, 5, 0, 3, 4, -2, -200,
  ])
);

console.log(
  longestConsecutive([
    4, 2, 2, -4, 0, -2, 4, -3, -4, -4, -5, 1, 4, -9, 5, 0, 6, -8, -1, -3, 6, 5,
    -8, -1, -5, -1, 2, -9, 1,
  ])
);

console.log(
  longestConsecutive([
    7, -9, 3, -6, 3, 5, 3, 6, -2, -5, 8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0,
  ])
);
