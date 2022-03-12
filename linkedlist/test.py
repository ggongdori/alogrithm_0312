from linkedlist import prac
from linkedlist import structures

p = prac
s = structures
l1 = s.LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = s.LinkedList()
for num in [1, 2]:
    l2.append(num)


# assert isPalindrome(l1.head)
# assert not isPalindrome(l2.head)

print(p.isPalindrome(l1.head))
print(p.isPalindrome(l2.head))