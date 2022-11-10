

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseList(self, head) :
        
        prev = None
        while head!=None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev


        


inp = [int(x) for x in input().split()]

head = ListNode(inp[0])
for i in range(1,len(inp)):
    if head.next == None:
        head.next = ListNode(inp[i])
        curr = head.next
    else:
        curr.next = ListNode(inp[i])


s1 = Solution()
x=s1.reverseList(head)


    