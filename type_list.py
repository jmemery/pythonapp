x = 12
y = 12
print ' ',
for fact in range(1, x+1):
    str(fact).rjust(6),
for fact in range(1, y+1):
    print
    print fact,
    for i in range(1,y+1):
        product = i * fact
        print str(product).rjust(3),
    print
