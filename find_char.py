#newlist=""
#a = list1 = ['hello','world','my','name','is','Anna']
#a = { i:i.count('o') for i in list1 if i.count('o') > 0}
#for o in a:
    #newlist += o
    #print newlist



#new
newstr =""
letters = set('o')
wordlist = ['hello','world','my','name','is','Anna']
for word in wordlist:
    if letters & set(word):
        newstr = newstr+" "+word
print newstr
