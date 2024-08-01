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
function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
  if (head === null) return null;
  let buffer: ListNode[] = [];
  let currNode: ListNode | null = head;
  for (let i = 0; i < k; i++) {
    if (currNode === null) break;
    buffer.push(currNode);
    currNode = currNode?.next;
  }
  if (buffer.length != k) return head;
  for (let i = buffer.length - 1; i > 0; i--) {
    buffer[i].next = buffer[i - 1];
  }
  buffer[0].next = reverseKGroup(currNode, k);
  return buffer[buffer.length - 1];
}

// reverse first k, then recur on sublist 1 - first k
