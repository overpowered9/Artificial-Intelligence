def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]
print(is_palindrome('dad'))  #True
print(is_palindrome('aibohphobia'))  #True
print(is_palindrome('Hello'))  #False