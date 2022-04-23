class Solution {


    public ListNode removeElements(ListNode head, int val) {
        ListNode h = fixedHead(head,val);
        removeEle(h,val);
        return h;
    }

    public ListNode fixedHead(ListNode head,int val){
        if(head==null){
            return head;
        }
        if(head.val==val){
            return removeElements(head.next,val);
        }
        return head;
    }

    public void removeEle(ListNode node,int val){
        if (node==null){
            return;
        }
        if(node.next!=null){
            while(node.next.val==val){
                node.next = node.next.next;
                if(node.next==null){
                    break;
                }
            }
            removeEle(node.next,val);
        }
    }
}

public ListNode removeElements(ListNode head, int val) {
    if (head == null) {
        return head;
    }
    // 因为删除可能涉及到头节点，所以设置dummy节点，统一操作
    ListNode dummy = new ListNode(-1, head);
    ListNode pre = dummy;
    ListNode cur = head;
    while (cur != null) {
        if (cur.val == val) {
            pre.next = cur.next;
        } else {
            pre = cur;
        }
        cur = cur.next;
    }
    return dummy.next;
}
