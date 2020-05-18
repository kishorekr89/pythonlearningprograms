import pickle
student_info=[["kishore",101,3000.00],["ramesh",102,4000.00],["naresh",103,5000.00]]
myinfo=open("storedata.txt","wb")
pickle.dump(student_info,myinfo)
myinfo.close()
