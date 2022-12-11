class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        
        tortoise = head
        hare = head.next

        while tortoise != hare:
            if hare == None or hare.next == None:
                return False

            tortoise = tortoise.next
            hare = hare.next.next

        return True
