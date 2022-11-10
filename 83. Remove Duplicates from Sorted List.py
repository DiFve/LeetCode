
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head) :
        curr = head
        while curr!=None:
            while curr.next!=None and curr.next.val == curr.val :
                curr.next = curr.next.next
            curr = curr.next
        

        return head


inp = [int(x) for x in input().split()]

head = ListNode(inp[0])
for i in range(1,len(inp)):
    if head.next == None:
        head.next = ListNode(inp[i])
        curr = head.next
    else:
        curr.next = ListNode(inp[i])

# curr = head
# while curr != None:
#     print(curr.val)
#     curr = curr.next

s1 = Solution()
s1.deleteDuplicates(head)
