w = input("enter the word to search : ")
s = set(w)
v = {'a','e','i','o','u'}
d = s.intersection(v)
print(" the vowels present in ",w,"are",d)
