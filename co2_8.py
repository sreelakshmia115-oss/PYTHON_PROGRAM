words=input("enter words:").split()
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print("longest word is:",longest)
print("length :",len(longest))