def min_ones(n):
    array = []
    array.append(0)
   #creating an array and appending it with values which are greater.
    for i in range(n):
        array.append(10000000)
    #adding the base case
    array[1] = 1
    #finding the minimum ones
    for i in range(2,n+1):
        array[i] = min(function1(array,i),function2(array,i),function3(array,i))
    
    return array[n]

def function1(a,b):
    
    #finding all the pairs of numbers for which their summation comes to n
    abc = []
    pair=[]
    for i in range(1,b+1):
        if b-i in abc or (i+i) == b:
            pair.append((i,b-i))
            if (b-i) in abc:
                abc.remove((b-i))
        if i not in abc:
            abc.append(i)
    minimum = a[b]
    for j in range(len(pair)):
        minimum = min(minimum,a[pair[j][0]]+a[pair[j][1]])
    return minimum

def function2(a,b):
    abc = []
    pair=[]
    #finding all the pairs of numbers for which their multiplication comes to n
    for i in range(1,b+1):
        if b%i==0 and b//i in abc or (i*i) == b:
            pair.append((i,b//i))
            if (b-i) in abc:
                abc.remove(b//i)
        if i not in abc:
            abc.append(i)
    minimum = a[b]
    for j in range(len(pair)):
        minimum = min(minimum,a[pair[j][0]]+a[pair[j][1]])
    return minimum

def function3(a,b):
    #
    abc = str(b)
    length_num =len(abc)
    minimum = a[b]
    if length_num == 1:
        return minimum
    #we are splitting the numbers at index position like 21 can be splitted in 2 and 1
    for i in range(1,length_num):
        #here the length cannot exceed 6 (condition given) hence a constant
        if abc[i] == 0:
            continue
        minimum = min(minimum,a[int(abc[:i])]+a[int(abc[i:])])
    return minimum
    