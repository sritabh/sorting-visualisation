a = [16, 19, 11, 15, 10, 12, 14]

#iterating over a
for i in range(0,len(a)):
    j = i
    print(j)
    #i is not the first element
    while j>0:
        #not in order
        if a[j-1] > a[j]:
            #swap
            a[j-1],a[j] = a[j],a[j-1]
        else:
            #in order
            break
        j = j-1
print (a)