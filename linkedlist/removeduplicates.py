def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# def is_prime(n):
#     if n == 1 :
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(123456))

#complexity = O(n)
#space = O(1)

# you can use sqrt too import math, for i in range(2,floor(sqrt(n) +1) ) :