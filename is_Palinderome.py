def is_Palindrome(s):
    for i in range(len(s)/2):
        if s[i] != s[~i]:
           return False
    return True


if __name__ == '__main__':
   a = [1,2,1]
   b = "1221"
   c = '1232123'
   print is_Palindrome(a)
   print is_Palindrome(b)
   print is_Palindrome(c)
