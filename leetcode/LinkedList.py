
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self) -> None:
        current = self.head
        while current:
            print(current.val)
            current = current.next

# 示例使用
linked_list = LinkedList()
linked_list.head = ListNode(1) 
second = ListNode(2)
third = ListNode(3)

linked_list.head.next = second
second.next = third

linked_list.traverse()

# 打印输出:
# 1
# 2 
# 3

from typing import Optional, List   

class Solution:
    # https://leetcode.cn/problems/add-two-numbers/
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化链表
        head = tree = ListNode()
        val = tmp = 0
        while tmp or l1 or l2:
            val = tmp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next

            tmp = val // 10
            val = val % 10

            # 实现链表的连接
            tree.next = ListNode(val)
            tree = tree.next

        return head.next

    # https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-100-liked
    # 快慢指针
    # 我们定义快慢指针 fastfastfast 和 slowslowslow，初始时均指向 headheadhead。
    # 快指针每次走两步，慢指针每次走一步，不断循环。当快慢指针相遇时，说明链表存在环。如果循环结束依然没有相遇，说明链表不存在环。
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast != slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
        
    # https://leetcode.cn/problems/intersection-of-two-linked-lists/description/
    # 总结：快慢指针，时间复杂度 O(n), 空间复杂度 O(1)
    def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
        # p1 指向 A 链表头结点，p2 指向 B 链表头结点
        p1, p2 = headA, headB
        while p1 != p2:
            # p1 走一步，如果走到 A 链表末尾，转到 B 链表
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            # p2 走一步，如果走到 B 链表末尾，转到 A 链表
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        return p1
    
    # https://leetcode.cn/problems/middle-of-the-linked-list/
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # return slow
        
        
        count = 0
        p = head
        while p:
            count += 1
            p = p.next 
        
        mid = count // 2
        p = head
        while mid:
            mid -= 1
            p = p.next
            
        return p
        
    # https://leetcode.cn/problems/sorted-merge-lcci/
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        if m == 0:
            return B[:n]
        if n == 0:
            return A[:m]
        if A[m-1] > B[n-1]:
            A[m+n-1] = A[m-1]
            return self.merge(A, m-1, B, n)
        else:
            A[m+n-1] = B[n-1]
            return self.merge(A, m, B, n-1) 
        
        
    # https://leetcode.cn/problems/merge-two-sorted-lists/
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
    # def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    #     if len(lists) < 1:
    #         return None
    #     elif len(lists) == 1:
    #         return lists[0]
    #     else:
    #         return self.mergeTwoLists(self.mergeTwoLists(lists[0], lists[1]) , self.mergeKLists(lists[2:]))       
        
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2   # //是Python中的整数除法运算符,会自动向下取整
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return self.mergeTwoLists(left, right)

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 存放小于 x 的链表的虚拟头结点
        dummy1 = ListNode(-1)
        # 存放大于等于 x 的链表的虚拟头结点
        dummy2 = ListNode(-1)
        # p1, p2 指针负责生成结果链表
        p1, p2 = dummy1, dummy2
        # p 负责遍历原链表，类似合并两个有序链表的逻辑
        # 这里是将一个链表分解成两个链表
        p = head
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            # 不能直接让 p 指针前进，
            # p = p.next
            # 断开原链表中的每个节点的 next 指针
            temp = p.next
            p.next = None
            p = temp

        # 连接两个链表
        p1.next = dummy2.next

        return dummy1.next
    
    # https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        p1, p2 = head, head
        length = 0
        
        while p1:
            p1 = p1.next
            length += 1
        
        if n == length:
            return head.next
        
        for _ in range(length - n -1):
            p2 = p2.next
        if p2:
            p2.next = p2.next.next
        return head
    
    # https://leetcode.cn/problems/reverse-linked-list/
    # 链表反转，queue LIFO (Last In First Out) 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        p1, p2 = head, head
        queue = []
        while p1:
            queue.append(p1.val)
            p1 = p1.next
        
        while queue:
            p2.val = queue.pop()
            p2 = p2.next
        return head    
    
    # https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        
        return head
    


linked_list = LinkedList()
linked_list.head = ListNode(1) 
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(5)

linked_list.head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
                
solution = Solution()
print(solution.merge([0], 0, [1], 1))
solution.removeNthFromEnd(linked_list.head, 2)        
linked_list.traverse()