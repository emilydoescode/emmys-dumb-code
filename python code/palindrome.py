def isPalindrome(txt):
    return txt == txt[::-1]

txt = input("Please increase a word, do not use capital letters: ")
ans = isPalindrome(txt)

if ans:
    print("Yes")
else:
    print("No")