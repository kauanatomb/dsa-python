class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        original = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        if original == rev:
            return True
        return False

# Test
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))