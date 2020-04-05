l=[]
p=[]
n=int(input("Enter Number of Elements in List: "))
for i in range(n):
    e=int(input("Enter The Element: "))
    l.append(e)
print("Input: ",l)
for i in l:
    if(i>0):
        p.append(i)
print("Output: ",p)
