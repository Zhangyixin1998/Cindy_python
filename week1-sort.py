file = open(r"D:\all the things\python\corpara\1.txt",'r').read()
file = file.replace(",","").replace(".","").replace(":","").replace(";","").replace("?","").replace('"'," ").lower()
list = file.split()

dic={}
for i in list:
    count = list.count(i)
    dic[i] = count

dic1=sorted(dic.items(),key=lambda d:d[1],reverse= True)


i=0


print("freq*\tword");

print("-----\t-----");

for key in dic1:
	print(str(key[1])+"\t"+key[0]);
	i += 1;
	if(i == 10):
            break;
        
print("-----\t-----");

dic2=sorted(dic.items(),key=lambda d:-d[1],reverse= True)

j=0
for key in dic2:
	print(str(key[1])+"\t"+key[0]);
	j += 1;
	if(j == 10):
            break;




