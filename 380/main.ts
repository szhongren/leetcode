class RandomizedSet {
  mapOfIndices: Map<number, number>;
  values: number[];
  constructor() {
    this.mapOfIndices = new Map();
    this.values = [];
  }

  insert(val: number): boolean {
    let notInSet = !this.mapOfIndices.has(val);
    if (notInSet) {
      this.mapOfIndices.set(val, this.values.length);
      this.values.push(val);
    }
    // console.log(`add ${val}`);
    // console.log(this.mapOfIndices);
    // console.log(this.values);
    return notInSet;
  }

  remove(val: number): boolean {
    let inSet = this.mapOfIndices.has(val);
    if (inSet) {
      let index = this.mapOfIndices.get(val);
      let lastItem = this.values.pop();
      if (lastItem !== val) this.values[index] = lastItem;
      this.mapOfIndices.set(lastItem, index);
      this.mapOfIndices.delete(val);
    }
    // console.log(`remove ${val}`);
    // console.log(this.mapOfIndices);
    // console.log(this.values);
    return inSet;
  }

  getRandom(): number {
    return this.values[Math.floor(Math.random() * this.values.length)];
  }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */

// approach insert // basically pretty regular
Math.random();

// have a map and a list
// when inserting, insert into map (val, index)
// when removing,
// look for index of val
// remove from list
// swap with last val in list
// update map of last val's index to new index
