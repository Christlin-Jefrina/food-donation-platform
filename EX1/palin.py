def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

# Test cases
print(is_palindrome("madam") == True)
print(is_palindrome("12321") == True)
print(is_palindrome("hello") == False)
print(is_palindrome("!@#@!") == True)
