/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode p1 = list1;
        ListNode p2 = list2;
        ListNode cur; 
        ListNode head;

        if (p1 != null && p2 != null) {
            if (p1.val < p2.val) {
                head = p1;
                p1 = p1.next;
            } else {
                head = p2;
                p2 = p2.next;
            }
        } else if (p1 == null && p2 != null) {
            return p2;
        } else if (p1 != null && p2 == null) {
            return p1;
        } else {
            return null;
        }

        cur = head;

        while (p1 != null & p2 != null) {
            if (p1.val < p2.val) {
                cur.next = p1;
                p1 = p1.next;
            } else {
                cur.next = p2;
                p2 = p2.next;
            }
            cur = cur.next;
        }
        
        if (p1 == null) {
            cur.next = p2;
        } else {
            cur.next = p1;
        }

        return head;
    }
}