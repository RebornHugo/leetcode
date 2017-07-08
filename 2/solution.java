import jdk.nashorn.internal.objects.NativeUint8Array;

/**
 * Created by CSLab on 2017/7/6.
 */
public class solution {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            if (l1 == null || l2 == null) {
                return null;
            }
            ListNode result = new ListNode(0);
            ListNode p = result;
            ListNode c1 = l1, c2 = l2;
            int sum, flag = 0;
            while (c1 != null || c2 != null) {
                sum = 0;
                if (c1 != null) {
                    sum = flag + c1.val;
                    c1 = c1.next;
                } else {
                    sum = flag;
                }
                if (c2 !=null){
                    sum += c2.val;
                    c2 = c2.next;
                }
                flag = sum / 10;
                sum = sum % 10;
                p.val = sum;
                if (c1 != null || c2 != null) {
                    p.next = new ListNode(0);
                    p = p.next;
                }
                }
        if (flag == 0) {
            return result;
        } else {
                p.next = new ListNode(1);
                p = p.next;
                return result;
        }
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(9);
//        l1.next = new ListNode(8);
//        l1.next.next = new ListNode(3);
        ListNode l2 = new ListNode(4);
//        l2.next = new ListNode(6);
//        l2.next.next = new ListNode(4);

        ListNode l3 = addTwoNumbers(l1, l2);
        while (l3 != null) {
            System.out.println(l3.val);
            l3 = l3.next;
        }
    }
}



