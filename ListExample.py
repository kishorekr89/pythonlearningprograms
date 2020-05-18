#intializing list in python
"""bank_list=list(["SBI","Allabad bank","Bank of India","Andhra bank","HDFC Bank","ICICI Bank"])
print(bank_list)
print(len(bank_list))# Returns Total no of elements in List
print(bank_list[0])# Accessing elements from positive index or position
print(bank_list[-1])#Accessing elements from negative index or position
print(bank_list[1:4])
check=[10,20,30,40,50,60]
print(check[1:len(check)])
print(check[:5])
print(check[:-4])
check[0]=1
print(check)
check[1:4]=[2,3,4]
print(check)
check.append(70)
print(check)
check.extend([80,90,100])
print(check)
grp2=[101,102,103]
print(check + grp2)
print(check*2)
print(check*4)"""
mylist=[10,20,30,40]
mylist.insert(0,200)
mylist.insert(1,105)
print(mylist)
mylist[1:2]=[100,200,300,400]
print(mylist)
