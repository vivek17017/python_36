#Q1
"""
def remove(l1):
    l1=list(set(l1))
    return l1
print(remove([2,3,5,3,'w',5,'w',6,2]))


#Q2

def freq(l1):
    d1={}
    l2=list(set(l1))
    for e in l2:
        d1[e]=l1.count(e)
    return d1
print(freq([5,6,7,6,7,4,'a',3,'a']))



#Q3
def text(s1):
    l1=[]
    l2=[eval(e) for e in s1.split(' ')]
    for e in l2:
        for i in e.split(','):
            if type(i)==int:
                l1.append(i)
    return l1
print(text("i want to add 5,6,7 and 56 to get 5"))


#Q4
def largest(l1):
    i=0
    for e in l1:
        l1[i]=sorted(e)
        i+=1
    j=0
    a=[]
    for e in l1:
        if j<len(e):
            j=len(e)
            a=e
    return a
        



l1=[[1,4,2],[3,6,2,8,9],[4,2,4,8],[5]]
print(largest(l1))

#Q5

def check(l1,l2):
    if set(l1)==set(l2):
        return True
    else:
        return False
print(check([1,2,3,4],[4,3,2,11]))
"""

#Q3
def extraNumbersFromText(text):
    num=[]
    for word in text.split(' '):
        for x in word.split(','):
            if type(eval(x))==int or type(eval(x))==float:
                num.append(float(x))
    return num
print(extraNumbersFromText("i want to add 4,4,45 to get 456"))