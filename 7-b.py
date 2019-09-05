fname=input("enter the file name")
fn=open(fname,'r')
c=w=l=0
for line in fn:
    l=l+1
    words=line.split()
    for word in words:
        w=w+1
        for ch in word:
            c=c+1
print("no of lines=",l)
print("no of words=",w)
print("no of characters",c)
fn.close()
                 
