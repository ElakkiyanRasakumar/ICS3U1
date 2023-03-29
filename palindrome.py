word = input("Enter a word")

palindrome = True
for i in range(len(word)//2):
    if word[i] != word[-1*(i+1)]:
        print("False")
        palindrome = False
        break
if palindrome:
    print("True")
