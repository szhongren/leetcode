/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  if (head === null) return null;
  let prevPointer = new ListNode(-1, head);
  let slowPointer = head;
  let fastPointer = head;
  for (let i = 0; i < n; i++) {
    fastPointer = fastPointer.next;
  }
  while (fastPointer !== null) {
    prevPointer = prevPointer.next;
    slowPointer = slowPointer.next;
    fastPointer = fastPointer.next;
  }
  prevPointer.next = slowPointer.next;
  return prevPointer.val === -1 ? prevPointer.next : head;
}
