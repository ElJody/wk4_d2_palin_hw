# This fails with race a car being true, and unsure why... Should pop false when e and a aren't =, 
# evaluated word and character with exact same results...
# If it worked properly, I suspect 0(n) or 0(1) considering the evaluation of each character, then evaluation of each word... 
# But this happens in place if understand yesterdays lecture and makes it more efficient

def palindrome(str):
    word =""
    left = 0
    right = len(word) - 1
    
    for char in str:
        if char.isalpha():
            char = char.lower()
            word += char

    while left <= right:
        if char[left] != char[right]:
#        if word[left] != word[right]:
            return False
        else:
            right -= 1
            left += 1
    print(word)
    return True

print(palindrome('A man, a plan, a canal: Panama'))
print(palindrome('race a car'))
print(palindrome(' '))

