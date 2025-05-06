function goodDaysToRobBank(security: number[], time: number): number[] {
  let forwardGoodDay: number[] = [];
  let backwardGoodDay: number[] = [];
  for (let i = 0; i < security.length; i++) {
    if (i == 0) {
      forwardGoodDay.push(0);
      continue;
    }
    if (security[i - 1] >= security[i]) {
      forwardGoodDay.push(forwardGoodDay[i - 1] + 1);
    } else {
      forwardGoodDay.push(0);
    }
  }
  for (let i = security.length - 1; i >= 0; i--) {
    if (i == 0) {
      backwardGoodDay.push(0);
      continue;
    }
    if (security[i] <= security[i + 1]) {
      backwardGoodDay.push(backwardGoodDay[backwardGoodDay.length - 1] + 1);
    } else {
      backwardGoodDay.push(0);
    }
  }
  backwardGoodDay = backwardGoodDay.reverse();
  //   console.log(forwardGoodDay);
  //   console.log(backwardGoodDay);
  //   console.log("-------------------------------");
  let result: number[] = [];
  for (let i = 0; i < security.length; i++) {
    if (forwardGoodDay[i] >= time && backwardGoodDay[i] >= time) result.push(i);
  }
  return result;
}

console.log(goodDaysToRobBank([5, 3, 3, 3, 5, 6, 2], 2));
console.log(goodDaysToRobBank([1, 1, 1, 1, 1], 0));
console.log(goodDaysToRobBank([1, 2, 3, 4, 5, 6], 2));

[true, false];
