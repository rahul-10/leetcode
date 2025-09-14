class Solution:
    def is_alpha_numeric(self, char: str) -> bool:
        return (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9')

    def isPalindrome(self, s: str) -> bool:
        left = 0;
        right = len(s)-1

        while(left < right):
            if not self.is_alpha_numeric(s[left]):
                left += 1
            elif not self.is_alpha_numeric(s[right]):
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


        