class MinStack {
  stack: { value: number; minBelow: number }[];

  constructor() {
    this.stack = [];
  }

  push(val: number): void {
    if (this.stack.length === 0) {
      this.stack.push({
        value: val,
        minBelow: val,
      });
    } else {
      this.stack.push({
        value: val,
        minBelow: Math.min(val, this.stack[this.stack.length - 1].minBelow),
      });
    }
  }

  pop(): void {
    this.stack.pop();
  }

  top(): number {
    return this.stack[this.stack.length - 1].value;
  }

  getMin(): number {
    return this.stack[this.stack.length - 1].minBelow;
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
