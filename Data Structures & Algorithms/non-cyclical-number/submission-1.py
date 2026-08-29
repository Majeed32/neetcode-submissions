class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            res = 0
            while num > 0:
                temp = num % 10
                res += temp*temp
                num = num // 10
            return res
        slow = square(n)
        fast = square(square(n))
        while slow != fast and fast != 1:
            slow = square(slow)
            fast = square(square(fast))
        return fast == 1
        