# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''t,t2=l1,l2
        x,y='',''
        while t!=None:
            x+=str(t.val)
            t=t.next
        while t2!=None:
            y+=str(t2.val)
            t2=t2.next
        x,y=int(x[::-1]),int(y[::-1])
        x=int(str(x+y))
        head=ListNode(x%10)
        x//=10
        prev=head
        while(x):
            node=ListNode(x%10)
            x//=10
            prev.next=node
            prev=node
        return head'''
        t1,t2,y=l1,l2,0
        '''while t1!=None or t2!=None:
            if t1!=None and t2!=None :
                if y==1:
                    x=t1.val+t2.val+y
                else:
                    x=t1.val+t2.val
                t1,t2=t1.next,t2.next
            elif t1!=None and t2==None:
                if y==1:
                    x=t1.val+y
                else:
                    x=t1.val
                t1=t1.next
            elif t2!=None and t1==None:
                if y==1:
                    x=t2.val+y
                else:
                    x=t2.val
                t2=t2.next
            if x//10!=0:
                y,x=1,x%10
            else:
                y=0
            if t1==l1.next and t2==l2.next:
                head=ListNode(x)
                prev=head
            else:
                node=ListNode(x)
                prev.next=node
                prev=node
            #print(x,y)
        if y:
            #print(y)
            node=ListNode(y)
            prev.next=node
            prev=node
        return head'''
                
                
                
