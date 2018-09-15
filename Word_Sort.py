#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open(r"D:\all the things\python\corpara\1.txt",'r',encoding='UTF-8').read()
f = f.replace(',','').replace(':','').replace('"','').replace('.','').replace('&','').replace(';','').replace('”','').replace('“','').replace('’','').replace('?','')
f = f.lower()
text=f.split()
dic={}
for i in text:
    count = text.count(i)
    dic[i]=count

dic1=sorted(dic.items(),key=lambda d:d[1],reverse= True)
dic2=sorted(dic.items(),key=lambda d:d[1],reverse= False)

i=0
j=0

print("freq*\tword")
print("-----\t-----")

for key in dic1:
    print(str(key[1])+"\t"+key[0]);
    i += 1;
    if(i == 10):
        break;
        
print("-----\t-----")

for key in dic2:
    print(str(key[1])+"\t"+key[0]);
    j += 1;
    if(j == 10):
        break;


# In[ ]:




