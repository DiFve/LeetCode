
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseBetween(self, head, left: int, right: int):

        if left-right == 0:
            return head
        
        count = 1
        ans = None
        while head != None:
            if count == left:
                rev = None
                while count <= right:
                    currRev = head
                    head = head.next
                    currRev.next = rev
                    rev = currRev
                    count += 1
                if ans == None:
                    ans = rev
                else:
                    currrr = ans
                    while currrr.next != None:
                        currrr = currrr.next
                    currrr.next = rev

            else:
                
                if ans == None:
                    ans = ListNode(head.val)
                    head = head.next
                    count+=1
                else:
                    
                    curr = ans
                    while curr.next != None:
                        curr = curr.next
                    curr.next = ListNode(head.val)
                    head = head.next 
                    count+=1

        return ans



inp = [int(x) for x in input().split(' ')]
left = int(input())
right = int(input())


head = ListNode(inp[0])
curr = None
for i in range(1,len(inp)):
    
    if head.next == None:
        head.next = ListNode(inp[i])
    else:
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = ListNode(inp[i])



s1 = Solution()
x = s1.reverseBetween(head,left,right)

while x!=None:
    print(x.val)
    x = x.next