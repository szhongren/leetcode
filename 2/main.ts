class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  if (l1 === null) return l2;
  if (l2 === null) return l1;
  return addTwoNumbersRecur(l1, l2, false);
}

function addTwoNumbersRecur(
  l1: ListNode | null,
  l2: ListNode | null,
  carry: boolean
): ListNode | null {
  if (l1 === null && l2 === null) return carry ? new ListNode(1) : null;
  if (l1 === null) {
    let sum = l2?.val + (carry ? 1 : 0);
    return new ListNode(
      sum % 10,
      addTwoNumbersRecur(null, l2?.next, sum >= 10)
    );
  }
  if (l2 === null) {
    let sum = l1?.val + (carry ? 1 : 0);
    return new ListNode(
      sum % 10,
      addTwoNumbersRecur(l1?.next, null, sum >= 10)
    );
  }
  let sum = l1.val + l2.val + (carry ? 1 : 0);
  return new ListNode(
    sum % 10,
    addTwoNumbersRecur(l1.next, l2.next, sum >= 10)
  );
}

// node(7) -> node(0)
