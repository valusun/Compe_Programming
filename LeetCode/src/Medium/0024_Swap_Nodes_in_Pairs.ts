export class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * @param head 隣接リストの先頭
 * `[0]`と`[1]`, `[2]`と`[3]`のペアで要素を入れ替える
 * 厄介なのは、隣接リスト形式（ListNode）なので、どう操作をするべきか直感ではイメージがつきづらい
 * `[0]`を操作したあと、`[2]`に飛ぶように、`currentNode.next.next`とすればよい
 * あとは記録してListNodeに変換して返すだけ
 *
 * ただ、letを使っているのが気になる...
 */
function swapPairs(head: ListNode | null): ListNode | null {
  const results: number[] = [];
  if (head == null) return null;

  // 1つ飛ばしで辿って入れ替え
  let currentNode: ListNode | null = head;
  while (currentNode != null) {
    if (currentNode.next == null) {
      results.push(currentNode.val);
      break;
    }
    results.push(currentNode.next.val);
    results.push(currentNode.val);
    currentNode = currentNode.next.next;
  }

  // nestの関係上、逆順からくみ上げる
  const reversed = results.reverse();
  let r = new ListNode(reversed[0]);
  for (let i = 1; i < reversed.length; i++) {
    r = new ListNode(reversed[i], r);
  }
  return r;
}

/** 別解 */
function swapPairs2(head: ListNode | null): ListNode | null {
  if (head == null) return null;

  // prev -> a -> b -> next を prev -> b -> a -> next にする
  // dummyを使って先頭の入れ替えも可能としている
  const dummy = new ListNode();
  dummy.next = head;

  let prev = dummy;
  while (prev.next != null && prev.next.next != null) {
    const a: ListNode = prev.next;
    const b: ListNode = a.next as ListNode; // whileチェック済み
    const next: ListNode | null = b.next;

    // prev -> b -> a -> next
    prev.next = b;
    b.next = a;
    a.next = next;
    prev = a;
  }
  return dummy.next;
}

console.dir(swapPairs(new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))))), { depth: null }); // [2, 1, 4, 3]
console.dir(swapPairs(null)); // [] / null

console.dir(swapPairs2(new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))))), { depth: null }); // [2, 1, 4, 3]
console.dir(swapPairs2(null)); // [] / null
