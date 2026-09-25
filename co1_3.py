#positive iist
numbers = [-2,-1,0,1,2,3,-3,-4,4]
positive = [n for n in numbers if n > 0]
print("positive numbers",positive)

#sqr of n number
squares = [n**2 for n in numbers]
print(squares)

#list of vowels
word = "Hello world"
vowels = [char for char in word.lower() if char in'aeiou']
print(vowels)

#list ordinal value
ordinal_values = [ ord(char) for char in word ]
print(ordinal_values)