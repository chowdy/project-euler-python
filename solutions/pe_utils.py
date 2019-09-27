def is_palindrome(s):
    s = str(s)
    for i in range(0, int(len(s) / 2)):
        other = len(s) - i - 1
        if s[i] != s[other]:
            return False
    return True
