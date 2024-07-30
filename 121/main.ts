function maxProfit(prices: number[]): number {
  let minimumIndex = 0;
  let maxProfit = 0;
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] - prices[minimumIndex] > maxProfit) {
      maxProfit = maxProfit;
    }
    if (prices[i] < prices[minimumIndex]) {
      minimumIndex = i;
    }
  }
  return maxProfit;
}

// for each val in prices
// if smaller than minimum
// set new minimum
// if difference larger than max
// set new max
// return max
