


def reverse(text):
   return text[::-1]

usertext=raw_input("Enter the text to check palindrome")
#print("Entered text is",text)
#usertext1 =str(usertext)

pal=reverse(usertext)

if(usertext==pal):
    print("Yes it is palindrome")
else:
    print("No it is not palindrome")
