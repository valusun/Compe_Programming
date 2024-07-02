class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null, isIncrement?: boolean): ListNode | null {
  const a = isIncrement === true ? 1 : 0;
  const ans = (l1?.val ?? 0) + (l2?.val ?? 0) + a;
  const val = ans % 10;
  const _isIncrement = ans > 9;
  const l1_next = l1 == null ? null : l1.next;
  const l2_next = l2 == null ? null : l2.next;
  if (l1_next == null && l2_next == null) {
    const next = _isIncrement == true ? new ListNode(1, null) : null;
    return new ListNode(val, next);
  }
  return new ListNode(val, addTwoNumbers(l1_next, l2_next, _isIncrement));
}

// debug用

class ListNodeUtils {
  constructor(protected arr: number[]) {}

  private generate(prevNode: ListNode, idx: number): ListNode {
    if (idx < 0) return prevNode;
    const nowNode = new ListNode(this.arr[idx], prevNode);
    return this.generate(nowNode, idx - 1);
  }

  public toListNode(): ListNode {
    const endNode = new ListNode(this.arr[this.arr.length - 1], null);
    return this.arr.length === 1 ? endNode : this.generate(endNode, this.arr.length - 2);
  }
}

const show = (node: ListNode | null) => {
  if (node == null) {
    console.log("---");
    return;
  }
  console.log("val: ", node.val);
  show(node.next);
};

const check1_l1 = new ListNodeUtils([2, 4, 3]).toListNode();
const check1_l2 = new ListNodeUtils([5, 6, 4]).toListNode();
show(addTwoNumbers(check1_l1, check1_l2));
const check2_l1 = new ListNodeUtils([0]).toListNode();
const check2_l2 = new ListNodeUtils([0]).toListNode();
show(addTwoNumbers(check2_l1, check2_l2));
const check3_l1 = new ListNodeUtils([9, 9, 9, 9, 9, 9, 9]).toListNode();
const check3_l2 = new ListNodeUtils([9, 9, 9, 9]).toListNode();
show(addTwoNumbers(check3_l1, check3_l2));
const check4_l1 = new ListNodeUtils([2, 4, 9]).toListNode();
const check4_l2 = new ListNodeUtils([5, 6, 4, 9]).toListNode();
show(addTwoNumbers(check4_l1, check4_l2));
