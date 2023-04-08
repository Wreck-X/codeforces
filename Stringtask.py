string = [i for i in input()]
vowels = ['A','E','I','O','U','Y','a','e','i','o','u','y']

for i,x in enumerate(string):
    if x in vowels:
        string[i] = ""
    
string = ''.join(string)
string = [i for i in string]

for i in range(0,len(string)*2,2):
    string.insert(i,'.')
for i,x in enumerate(string):
    if x == '.':
        continue
    if x.isupper():
        string[i] = x.lower()
print(''.join(string))
    

