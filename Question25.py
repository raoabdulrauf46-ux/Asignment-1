def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        return True
    else:
        return False

text = input("Enter string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")