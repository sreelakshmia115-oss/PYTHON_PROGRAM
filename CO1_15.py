list1= input("Enter color-list1: ").split()

2 list2 = input("Enter color-list2: ").split()

3 result = [x for x in list1 if x not in list2]

4 print(result)