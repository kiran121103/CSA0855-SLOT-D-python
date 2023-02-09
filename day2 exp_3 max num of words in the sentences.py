str1=input("Enter the Sentences:")
str2=str1.split(",")
count=[]
for i in range (len(str2)):
    str3=str2[i].split(",")
    count.append(len(str3))
print(max(count))
