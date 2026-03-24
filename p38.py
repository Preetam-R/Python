def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Test
print(is_palindrome("Race Car"))   # True
print(is_palindrome("hello"))      # False
print(is_palindrome("A man a plan a canal Panama".replace(" ", "")))  # True