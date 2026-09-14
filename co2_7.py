s=input("enter a string:")
length=len(s)
if length > 2:
    if s[-3:] == "ing":
        print(s + "ly")
    else:
        print(s + "ing")
else:
    print("string is too short to modifys")
