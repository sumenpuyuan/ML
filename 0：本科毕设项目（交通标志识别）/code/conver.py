#coding: utf-8
import csv
import sys
name=[]
f=[]
for i in range(0,62):
	name.append("GT-"+str(i).zfill(5)+".csv")
b=open("sum.csv","w",newline='')
writer = csv.writer(b)
sum=0
for i in range(0,62):
	c=open(name[i],"r")
	read=csv.reader(c)
	j=0
	for line in read:
		if j!=0:
			print(line[0])
			writer.writerow([line[0]])
		j=j+1
	print("operate:%d,make:%d" % (i,j))
	sum=sum+j
	#print("a=%d,b=%d" % (1,2))
	#input()
	c.close
print("sum is",sum)
