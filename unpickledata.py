import pickle
myimfo=open("storedata.txt","rb")
data=pickle.load(myimfo)
for p in data:
    print(p)
myimfo.close()

